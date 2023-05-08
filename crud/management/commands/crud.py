'''


'''

import os
import django
from excellence import settings
from django.core.management.base import BaseCommand
from django.apps import apps

MANYTOMANY_STYLE = '''

    .selector {
        width: 100%;
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        justify-content: space-around;
        align-items: baseline;

    }

    .selector-chooser {
        text-align: center;
        vertical-align: middle;
        {#width: 20%;#}
        list-style-type: none;
    }

   .selector-available > a, .selector-chosen >a ,ul.selector-chooser > li > a {
        font-size: 14px;
        color: #666;
        background-color: #fff;
        background-image: none;
        text-decoration: none;

    }
   .selector .selector-filter {
        border: 0px solid #ccc;
        border-width: 0 0px;
        padding: 4px 0px 4px 0px;
   }
   .selector .selector-filter label {
        display: none;
   }

   .selector select {
        height: 17.2em;
        width: 100%; /* fix offscreen scroll-bar on selector-chosen */
        border: 10px #cccccc solid;
   }
   .selector .selector-chosen select {
        border-top: 0;
   }


    /* selector object list */
   .selector > .selector-available > select, .selector > .selector-chosen > select {
        font-size: 12px;
        color: #666;
        background-color: #fff;
        background-image: none;
        border: 1px solid #ccc;
        border-radius: 0px 0px 4px 4px;
        box-shadow: 0px 0px 1px rgba(0, 0, 0, 0.075) inset;
        transition: border-color 0.15s ease-in-out 0s, box-shadow 0.15s ease-in-out 0s;
   }
    /* selector object list items */
   .selector > .selector-available > select > option, .selector > .selector-chosen > select > option {
        padding: 6px;
        border-bottom-width: 1px;
        border-bottom-color: rgba(211, 211, 211, 0.35);
        border-bottom-style: solid
   }
    /* selector field title */
   .selector > .selector-available > h2, .selector > .selector-chosen > h2 {
        text-align: left;
        background: rgba(211, 211, 211, 0.2);
        color: #777;
        border: 1px solid #ccc;
        border-bottom: none;
        font-size: 100%;
        font-weight: 600;
        margin: 0px;
        padding: 10px 0px 6px 10px;
        height: 36px;
        border-radius: 4px 4px 0px 0px;
   }
    /* selector filter box bootstrapping */
    .selector .selector-available input {
        width: 80%;
        height: 34px;
        padding: 6px 12px;
        font-size: 14px;
        line-height: 1.42857;
        color: #777;
        background-color: #fff;
        background-image: none;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-shadow: 0px 1px 1px rgba(0, 0, 0, 0.075) inset;
        transition: border-color 0.15s ease-in-out 0s, box-shadow 0.15s ease-in-out 0s;
    }
    .selector .selector-available p {
        background: rgba(211, 211, 211, 0.2);
        border-left: 1px solid #ccc;
        border-right: 1px solid #ccc;
        padding: 0px 0px 7px 6px;
    }
    /* selector chooseall and clearall button spacing */
    a.selector-chooseall {
        padding: 0px 20px 3px 0;
    }
    a.selector-clearall {
        padding: 0px 0 3px 20px;
    }


        .selector-available {
        order: 1;
        flex-grow: 2;
        align-self: baseline;
    }
    .selector-chooser {
        order: 2;
        flex-grow: 1;
        align-self: baseline;
    }
    .selector-choosen {
        order: 3;
        flex-grow: 2;
        align-self: baseline;
    }


'''

class Command(BaseCommand):
    help = 'Create crud from '
    modelname=''
    list_extend_template = 'baseBS.html'
    app = None
    ruta_templates = 'crud'
    forms_extend_template = 'base_formBS.html'
    tabletamplate = 'django_tables2/bootstrap4.html'
    baseFields = [] ## Fields without reverse relations
    fields = []
    fieldsList = '' ## Char field list separated by coma
    pktype = None ## Type of primary key
    searchFields = '' ## Char, query for search in list mode


    def add_arguments(self, parser):
        parser.add_argument('app', type=str,help='Indicate the app')
        parser.add_argument('modelnameimport',  type=str,help='The name inside models app to create crud')

        parser.add_argument('-t','--templates', type=str, help='Folder where send files')
        parser.add_argument('-b','--basetemplate', type=str, help='Base template to use in list')

    def handle(self, *args, **kwargs):
        self.app = kwargs['app']
        self.modelname = kwargs['modelnameimport']
        list_extend_template = kwargs['basetemplate'] or 'baseBS.html'

        if self.app not in apps.app_configs:
            self.stdout.write(self.style.ERROR(f'{self.app} don´t exist'))
            exit(1)

        try:
            apps.get_model(self.app, self.modelname.lower())
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'{e}'))
            exit(2)

        modelfile = f'{self.app}/models.py'
        file = open(modelfile, 'r', encoding='utf-8')
        filer = file.read()
        file.close()

        if not f'class {self.modelname}' in filer:
            self.stdout.write(f'Model {self.modelname} not find in {self.app}/models.py, It can be {self.modelname.capitalize()}')
            exit(2)

        self.main()

    def main(self):

        try:
            model = apps.get_model(f'{self.app}.{self.modelname.lower()}')
        except Exception as e:
            return e
            self.stdout.write(self.style.ERROR(e))
            exit(1)

        for field in model._meta.get_fields():
            if 'reverse_related' in f'{type(field)}':
                continue
            self.baseFields.append(field)

        self.fieldsList = ','.join([f"'{field.name}'" for field in self.baseFields])
        self.pktype = model._meta.pk.get_internal_type()
        self.searchFields = ('|'.join(f"""Q({field.name}__icontains=search) """ for field in self.baseFields if field.get_internal_type() in ('CharField','IntegerField','DateField')))

        self.templates()
        self.forms()
        self.tables()
        self.views()
        self.urls()
        self.adminfile()

    def tables(self):

        try:
            tablesfiles = f'{self.app}/tables.py'
            file = open(tablesfiles, 'r', encoding='utf-8')
            filer = file.read()
            file.close()
        except:
            filer=''

        className = f'{self.modelname}Table'
        imports = ''

        if not f'class {className}' in filer:

            if not 'import django_tables2' in filer:
                imports += 'import django_tables2 as tables\r'

            if not 'import format_html' in filer:
                imports += 'from django.utils.html import format_html\r'

            if not 'from django_tables2.utils import A' in filer:
                imports += 'from django_tables2.utils import A\r'

            if not 'from django.utils.safestring import mark_safe' in filer:
                imports += 'from django.utils.safestring import mark_safe\r'

            if not 'from django.db.models import Q' in filer:
                imports += 'from django.db.models import Q\r'

            if not 'from django.shortcuts import HttpResponse' in filer:
                imports += 'from django.shortcuts import HttpResponse\r'

            if not 'from django.template import loader' in filer:
                imports += 'from django.template import loader\r'

            del filer  ##Liberamos memoria

            table = f'''
{imports}

from .models import {self.modelname}

class {className}(tables.Table):

    edit = tables.LinkColumn("{self.app}:{self.modelname}-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")],orderable=False)
    borrar = tables.LinkColumn("{self.app}:{self.modelname}-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")],orderable=False)
    
    def before_render(self, request):
        if request.user.has_perm('{self.app}.delete_{self.modelname.lower()}'):
            self.columns.show('borrar')
        else:
            self.columns.hide('borrar')
    
        if request.user.has_perm('{self.app}.change_{self.modelname.lower()}'):
            self.columns.show('edit')
        else:
            self.columns.hide('edit')
    
    
    class Meta:
        model = {self.modelname}
        template_name = "{self.tabletamplate}"
        orderable=True
        #exclude = excludeFields
'''
            file = open(tablesfiles, 'a', encoding='utf-8')

            self.stdout.write(self.style.NOTICE('Generating tables.py'))
            file.write(table)
            file.close()

    def views(self):
        tablesfiles = f'{self.app}/views.py'
        file = open(tablesfiles, 'r', encoding='utf-8')
        filer = file.read()
        file.close()

        if not f'class {self.modelname}List' in filer:
            imports = ''

            if not 'from django.views.generic import' in filer:
                imports += 'from django.views.generic import ListView,DeleteView,DetailView,CreateView,UpdateView\r'

            if not 'SingleTableView' in filer:
                imports += 'from django_tables2 import SingleTableView\r'

            if not 'reverse_lazy' in filer:
                imports += 'from django.urls import reverse_lazy\r'

            if not 'from django.views.generic import' in filer:
                imports += 'from django.views.generic import ListView,DeleteView,DetailView,CreateView,UpdateView\r'

            if not 'LoginRequiredMixin' in filer:
                imports += 'from django.contrib.auth.mixins import LoginRequiredMixin\r'

            if not 'PermissionRequiredMixin' in filer:
                imports += 'from django.contrib.auth.mixins import PermissionRequiredMixin\r'

            if not 'from dal' in filer:
                imports += 'from dal import autocomplete\r'

            if not 'from django.db.models import Q' in filer:
                imports += 'from django.db.models import Q\r'

            views = f'''
{imports}
from .forms import {self.modelname}Form
from .tables import {self.modelname}Table
from .models import {self.modelname}
####################

class {self.modelname}List(PermissionRequiredMixin,SingleTableView):
    permission_required = '{self.app}.view_{self.modelname}'
    model = {self.modelname}
    template_name = '{self.app}/{self.modelname.lower()}/{self.modelname}_list.html'
    table_class = {self.modelname}Table
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = {self.modelname}.objects.filter({self.searchFields})
        else:
            queryset = {self.modelname}.objects.all()
        return queryset


class {self.modelname}Create(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = '{self.app}.add_{self.modelname}'
    model = {self.modelname}
    form_class = {self.modelname}Form
    success_url = reverse_lazy('{self.app}:{self.modelname}-list')
    template_name = '{self.app}/{self.modelname}/{self.modelname}_form.html'

class {self.modelname}Update(PermissionRequiredMixin,UpdateView):
    permission_required = '{self.app}.change_{self.modelname}'
    model = {self.modelname}
    template_name = '{self.app}/{self.modelname}/{self.modelname}_form.html'
    form_class = {self.modelname}Form
    success_url = reverse_lazy('{self.app}:{self.modelname}-list')
    
class {self.modelname}View(PermissionRequiredMixin, UpdateView):
    permission_required = '{self.app}.change_{self.modelname}'
    model = {self.modelname}
    template_name = '{self.app}/{self.modelname}/{self.modelname}_form.html'
    form_class = {self.modelname}Form
    success_url = reverse_lazy('{self.app}:{self.modelname}-list')

    def get_form(self, form_class=None):
        form = super(self.__class__, self).get_form(form_class)
        for field, obj in form.base_fields.items():
            obj.disabled = True
        form.helper.inputs.pop(0)
        return form

class {self.modelname}Delete(PermissionRequiredMixin,DeleteView):
    permission_required = '{self.app}.delete_{self.modelname}'
    model = {self.modelname}
    template_name = '{self.app}/confirm_delete.html'
    success_url = reverse_lazy('{self.app}:{self.modelname}-list')
    
class {self.modelname}Autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return {self.modelname}.objects.none()
        qs = {self.modelname}.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
        
def {self.modelname}Post(request,qid):
    {self.modelname.lower()} = {self.modelname}.objects.filter(pk=qid)
    t = loader.get_template('proyecto/{self.modelname}/{self.modelname}_partial.html')
    c = {{}}
    c['{self.modelname.lower()}']= {self.modelname.lower()}

    if request.method == "POST":
        pass
        #v1 = request.POST.get('var1')
        #v2 = request.POST.get('var2')
        #v3 = request.POST.get('var3',100)
        #if v1:
        #    try:
        #        fse = Fase(proyecto_id=pid,fase=fs,orden=ord)
        #        fse.save()
        #        fases = Fase.objects.filter(proyecto_id=proyectoid)
        #        c = {{'context': fases}}
        #    except:
        #        pass

    return HttpResponse(t.render(c))
        '''

        self.stdout.write(self.style.NOTICE('Generating views.py'))

        file = open(f'{self.app}/views.py', 'a+', encoding='utf-8')
        file.write(views)
        file.close()

    def templates(self):

        templatedir = os.path.join(settings.TEMPLATES[0]['DIRS'][0], self.app, self.modelname)
        if not os.path.exists(templatedir):
            os.mkdir(templatedir)

        nomntemplist = f'{self.modelname}_list.html'

        templatelist = f'''
    
{{% extends "{self.list_extend_template}" %}}
{{% load i18n %}}
{{% load render_table from django_tables2 %}}
{{% block content %}}
    <h3>{self.modelname.capitalize()}</h3>
    <div class="row m-3">
        <form method="get">
            <div class="input-group mb-3">
                <input type="text" class="form-control" placeholder="{{% translate 'Search'%}}" aria-label="Search" aria-describedby="Search box" name="search">
                    <div class="input-group-append">
                        <button class="btn btn-outline-secondary" type="submit"><i class="bi bi-search"></i></button>
                    </div>
            </div>
        </form>
        <div class="col-1">
            <a class="btn btn-primary" href="{{% url '{self.app}:{self.modelname}-add' %}}" role="button">{{% translate 'Add' %}}</a>
        </div>
    </div>
    <div class="row">
        <div class="col-12">
            {{% render_table table %}}
        </div>
    </div>
{{% endblock %}}
                    '''

        self.stdout.write(self.style.NOTICE('Generating template list'))
        filetemplatelist = os.path.join(templatedir, nomntemplist)

        file = open(filetemplatelist, 'w+', encoding='utf-8')
        file.write(templatelist)
        file.close()

        ### PARTIAL TEMPLATE ###


        templateplartial = f'''
        <caption>{self.modelname.capitalize()}</caption>
<table class="table table-sm">
    <thead>
    <tr>
        <th scope="col">#</th>
        <th scope="col">{self.modelname.capitalize()}</th>
    </tr>
    </thead>
    <tbody>
    {{% for {self.modelname.lower()} in {self.modelname.lower()} %}}
        <tr>
            <td>{{ {self.modelname.lower()}.pk }}</td>
            <td>{{ {self.modelname.lower()} }}</td>
        </tr>
    {{% endfor %}}
    </tbody>
</table>

        '''
        nomntemppartial = f'{self.modelname}_partial.html'
        self.stdout.write(self.style.NOTICE('Generating template partial'))
        filetemplatelist = os.path.join(templatedir, nomntemppartial)

        file = open(filetemplatelist, 'w+', encoding='utf-8')
        file.write(templatelist)
        file.close()


        ### FORM  TEMPLATE###
        nomntempform = f'{self.modelname}_form.html'
        hasm2m = [field.get_internal_type() ==  'ManyToManyField' for field in self.baseFields].count(True) > 0

        templateform = f'''
    {{% extends "{self.forms_extend_template}" %}}
    {{% load crispy_forms_tags %}}
    {{% load i18n %}}
    '''
    ## TODO cambiar MANYTOMANY_STYLE a un import de css

        if hasm2m:
            templateform += f'''
    {{% block style%}}
        {MANYTOMANY_STYLE}
    {{% endblock %}}
            '''

        templateform += f'''
    {{% block content %}}
    {{% crispy form form.helper %}}
    {{% endblock %}}
        '''

        self.stdout.write(self.style.NOTICE('Generating template forms'))
        filetemplateform = os.path.join(templatedir, nomntempform)
        file = open(filetemplateform, 'a+', encoding='utf-8')
        file.write(templateform)
        file.close()

    def serializers(self):


        tablesfiles = f'{self.app}/serializers.py'
        try:
            file = open(tablesfiles, 'r', encoding='utf-8')
            filer = file.read()
            file.close()
        except:
            filer=''

        nombreclase = f'class {self.modelname}Serializer'

        if not nombreclase in filer:
            imports = ''

            if not 'from rest_framework import serializers' in filer:
                imports += 'from rest_framework import serializers'
            if not f'from {self.app}.models import {self.modelname}' in filer:
                imports += f'from {self.app}.models import {self.modelname}'

            if not self.fieldsList:
                campos = ''

            serializer = f'''
            {imports}
            
            class {nombreclase}(serializers.ModelSerializer):
                class Meta:
                    model = {self.modelname}
                    fields = [{'__all__' if self.fieldsList is None else self.fieldsList}]
            
            '''

            file = open(tablesfiles, 'a+', encoding='utf-8')
            file.write(serializer)
            file.close()

    def urls(self):
        # DO: Buscar la clave primaria, si esta es alfanumerica quitar el <int: > del path
        # TODO: Incluir en el url.py de la aplicacion

        urlfiles = f'{self.app}/urls.py'
        try:
            file = open(urlfiles, 'r', encoding='utf-8')
            filer = file.read()
            file.close()
        except:
            filer=''

        imports = ''
        if not 'from django.urls import path' in filer:
            imports = 'from django.urls import path'

        claveurl = '<pk>'
        if not f'{self.modelname}-list' in filer:
            if self.pktype in ('AutoField', 'IntField', 'BigAutoField'):
                claveurl = '<int:pk>'
            else:
                claveurl = '<pk>'

            ##from django.urls import path, include


            urlimport = f'''
from {self.app}.views import {self.modelname}List,{self.modelname}Create,{self.modelname}View,{self.modelname}Delete,{self.modelname}Update,{self.modelname}Autocomplete'''

        url = f'''
## {self.modelname}
urlpatterns += [
    path('{self.modelname.lower()}/list/', {self.modelname}List.as_view(), name='{self.modelname}-list'),
    path('{self.modelname.lower()}/add/', {self.modelname}Create.as_view(), name='{self.modelname}-add'),
    path('{self.modelname.lower()}/view/{claveurl}/', {self.modelname}View.as_view(), name='{self.modelname}-view'),
    path('{self.modelname.lower()}/modify/{claveurl}/', {self.modelname}Update.as_view(), name='{self.modelname}-update'),
    path('{self.modelname.lower()}/delete/{claveurl}/', {self.modelname}Delete.as_view(), name='{self.modelname}-delete'),
    path('{self.modelname.lower()}-autocomplete/',{self.modelname}Autocomplete.as_view(),name='{self.modelname}-autocomplete'),
]
    
        '''
        file = open(urlfiles, 'a+', encoding='utf-8')
        # self.stdout.write(self.style.NOTICE('Generating url.py .'))
        if imports:
            file.write(imports)
        file.write(urlimport)
        file.write(url)
        file.close()

    def forms(self):
        layout = f'''Div(HTML('<h3>{self.modelname}</h3><hr>'),css_class="mt-4"),'''
        campos = ''
        widgets = ''
        hasm2m2 = False
        style = ''

        # widgets = {
        #     'fechanacimiento': DateInput(),
        #     'fechaaniversario': DateInput()
        # }

        for field in self.baseFields:
            if field.primary_key == True:
                continue
            if field.editable == False:
                continue

            # if campo.related_model:
            #     layout += f'''Field('{campo.name}', css_class='mt-2 selectpicker exselect',data_live_search='true'),\r '''
            # else:

            layout += f''' Field('{field.name}',css_class='mt-2'),\r'''
            campos += f"'{field.name}',"

            if field.get_internal_type() == 'DateField':
                widgets += f"'{field.name}': DateInput(),\r"

            if field.get_internal_type() == 'DateTimeField':
                widgets += f"'{field.name}': DateInput(),\r"

            if field.get_internal_type() == 'TimeField':
                widgets += f"'{field.name}': TimeInput(),\r"

            if field.get_internal_type() ==  'ManyToManyField':
                widgets += f"'#{field.name}': FilteredSelectMultiple(verbose_name={self.modelname}._meta.verbose_name_plural, is_stacked=False),\r"
                widgets += f"'{field.name}': autocomplete.ModelSelect2Multiple(url='{field.related_model._meta.app_label}:{(field.related_model._meta.model_name).capitalize()}-autocomplete'),\r"
                hasm2m2 = True

            if field.get_internal_type() == 'ForeignKey':
                widgets += f"'{field.name}': autocomplete.ModelSelect2(url='{field.related_model._meta.app_label}:{(field.related_model._meta.model_name).capitalize()}-autocomplete'),\r"



        layout += '''HTML('<hr>'),'''

        ## Leemos el fichero forms.py
        formfiles = f'{self.app}/forms.py'
        try:
            file = open(formfiles, 'r', encoding='utf-8')
            filer = file.read()
            file.close()
        except:
            filer=''

        imports = ''
        if not f'class {self.modelname}Form(forms.ModelForm):' in filer:


            if not 'clases.form_classes' in filer:
                imports += 'from crud.clases.form_classes import DateInput, DateTimeInput, TimeInput\r'

            if not 'FilteredSelectMultiple' and hasm2m2 in filer:
                imports +='from django.contrib.admin.widgets import FilteredSelectMultiple\r'

            if not 'from django import forms' in filer:
                imports += 'from django import forms\r'

            if not 'from django.utils.translation import gettext_lazy as _'  in filer:
                imports += 'from django.utils.translation import gettext_lazy as _\r'

            if not 'from crispy_forms.helper import FormHelper'  in filer:
                imports += 'from crispy_forms.helper import FormHelper\r'

            if not 'from crispy_forms.layout'  in filer:
                imports += 'from crispy_forms.layout import Submit,Button,Layout,Field,HTML,Div\r'

            if not 'from dal' in filer:
                imports += 'from dal import autocomplete\r'

            if not 'gettext_lazy as _' in filer:
                imports += 'from django.utils.translation import gettext_lazy as _'

            del filer

        form = f'''
{imports}
from {self.app}.models import {self.modelname}\r

class {self.modelname}Form(forms.ModelForm):

    

    class Meta:
        model = {self.modelname}
        fields = [{campos}]

        widgets = {{
            {widgets}  
        }}

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-{self.modelname}'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        {layout}
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super({self.modelname}Form, self).__init__(*args, **kwargs)
                '''

        # self.stdout.write(self.style.NOTICE('Generating forms.py .'))

        file = open(f'{self.app}/forms.py', 'a+', encoding='utf-8')
        file.write(form)
        file.close()

    def adminfile(self,standalone=False):

        tablesfiles = f'{self.app}/admin.py'
        file = open(tablesfiles, 'r', encoding='utf-8')
        filer = file.read()
        file.close()

        nombreclase = f'{self.modelname}Admin'
        if not nombreclase in filer:


            if standalone:
                model = self.apps.get_model(f'{self.app}.{self.modelname.lower()}')
                campos = (','.join(f"""'{field.name}'""" for field in model._meta.get_fields() if
                           (not isinstance(field, django.db.models.fields.reverse_related.ManyToOneRel)) and (
                               not isinstance(field, django.db.models.fields.reverse_related.ManyToManyRel)) and (
                               not isinstance(field, django.db.models.fields.reverse_related.OneToOneRel))))
            if self.baseFields:
                campos=''
                for fields in self.baseFields:
                    if fields.primary_key == True:
                        continue
                    if fields.editable == False:
                        continue
                    campos += f"'{fields.name}',"


            imports = f'from {self.app}.models import {self.modelname}'

            admin = f'''
{imports}
        
@admin.register({self.modelname})
class {nombreclase}(admin.ModelAdmin):
    list_display = ({campos})
            '''
            self.stdout.write(self.style.NOTICE('Generating admin.py'))
            file = open(tablesfiles, 'a+', encoding='utf-8')
            file.write(admin)
            file.close()

