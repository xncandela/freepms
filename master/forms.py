
from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Button,Layout,Field,HTML,Div,Row,Column

from crud.clases.form_classes import DateInput, DateTimeInput, TimeInput
# from crud.widgets.select2 import Select2Widget

from django.contrib.admin.widgets import FilteredSelectMultiple
from dal import autocomplete


# widgets = {
#     'fechanacimiento': DateInput(),
#     'fechaaniversario': DateInput()
# }
from .models import Country
from .models import Region
from .models import Currency
from .models import CompanyGroup
from .models import Brand
from .models import Company
from master.models import HotelComplex
from master.models import Hotel
from master.models import ProductionGroup
from master.models import RoomType
from master.models import RoomClasification
from master.models import Prueba
from master.models import ProductionCenter


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['name','color','order']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-region'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
         Div(HTML('''<h3>Region</h3><hr>'''),css_class="mt-4"),
         'country',
         'name',
         'color',
         'order',
          HTML('<hr>'),

        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(RegionForm, self).__init__(*args, **kwargs)

class countryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = ['id','iso2','iso3','name','flag','calling_code','region','order']
        widgets = {
            'region': autocomplete.ModelSelect2(url='master:Region-autocomplete')
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-country'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>country</h3><hr>'),css_class="mt-4"),
            Field('currency'),
            Field('iso2',css_class='mt-2'),
            Field('iso3',css_class='mt-2'),
            Field('name',css_class='mt-2'),
            Field('flag',css_class='mt-2'),
            Field('calling_code',css_class='mt-2'),
            Field('region', css_class='mt-2',data_live_search='true'),
            Field('order',css_class='mt-2'),
            HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(countryForm, self).__init__(*args, **kwargs)

class CurrencyForm(forms.ModelForm):

    class Meta:
        widgets = {
            # 'countries': FilteredSelectMultiple(verbose_name=Currency._meta.verbose_name_plural, is_stacked=False)
            'countries': autocomplete.ModelSelect2Multiple(url='master:Country-autocomplete')
        }
        model = Currency
        fields = ['code','description','numcode','decimal','countries']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-Currency'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>Currency</h3><hr>'),css_class="mt-4"),
             Field('hotel',css_class='mt-2'),
             Field('code',css_class='mt-2'),
             Field('description',css_class='mt-2'),
             Field('numcode',css_class='mt-2'),
             Field('decimal',css_class='mt-2'),
             Field('countries',css_class='mt-2'),
            HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(CurrencyForm, self).__init__(*args, **kwargs)

class CompanyGroupForm(forms.ModelForm):
    class Meta:
        model = CompanyGroup
        fields = ['name','color','order']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-CompanyGroup'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>CompanyGroup</h3><hr>'),css_class="mt-4"), Field('brand',css_class='mt-2'),
 Field('id',css_class='mt-2'),
 Field('name',css_class='mt-2'),
 Field('color',css_class='mt-2'),
 Field('order',css_class='mt-2'),
HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(CompanyGroupForm, self).__init__(*args, **kwargs)

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name','group','color','order','logo']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-Brand'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>Brand</h3><hr>'),css_class="mt-4"), Field('hotel',css_class='mt-2'),
  Field('name',css_class='mt-2'),
Field('group', css_class='mt-2'),
  Field('color',css_class='mt-2'),
 Field('order',css_class='mt-2'),
 Field('logo',css_class='mt-2'),
HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(BrandForm, self).__init__(*args, **kwargs)

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name','taxid','phone','email','country','state','locality','postal_code','address','note','color',]

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-Company'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>Company</h3><hr>'),css_class="mt-4"), Field('country',css_class='mt-2'),

        Field('name',css_class='mt-2'),
        Field('taxid',css_class='mt-2'),
        Field('phone',css_class='mt-2'),
            Field('state', css_class='mt-2'),
            Field('locality', css_class='mt-2'),
            Field('postal_code', css_class='mt-2'),
            Field('address', css_class='mt-2'),
        Field('email',css_class='mt-2'),
        Field('note',css_class='mt-2'),
        Field('color',css_class='mt-2'),
        HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(CompanyForm, self).__init__(*args, **kwargs)

class HotelComplexForm(forms.ModelForm):
    class Meta:
        model = HotelComplex
        fields = ['name','country','state','locality','postal_code','address',]

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-HotelComplex'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>HotelComplex</h3><hr>'),css_class="mt-4"),
        Field('name', css_class='mt-2'),
        Field('country',css_class='mt-2'),
        Field('state',css_class='mt-2'),
        Field('locality',css_class='mt-2'),
        Field('postal_code',css_class='mt-2'),
        Field('address',css_class='mt-2'),

HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(HotelComplexForm, self).__init__(*args, **kwargs)

class HotelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        fields = ['code','name','color','brand','company','complex','basecurrency','timezone','active','closed','country','state','locality','postal_code','address','web','map','logog','logop','logoboton','background',]

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-Hotel'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
                Div(HTML('<h3>Hotel</h3><hr>'),css_class="mt-4"),
                Row(Column(Field('code'),css_class='col-3'), Column(Field('name'),css_class='col-9')),
                Row(
                    Column(Field('brand'),css_class='col-3 mt-2'),
                    Column(Field('company'),css_class='col-3 mt-2'),
                    Column(Field('color'), css_class='col-3 mt-2'),
                    Column(Field('complex'), css_class='col-3 mt-2'),

                ),
                Div(
                    Row(
                    Field('basecurrency',css_class='mt-2 col-6 '),
                    Field('timezone',css_class='mt-2 col-6'),
                    )
                ),
                Div(
                    Row(
                    Field('active',css_class='mt-2 col-2'),
                    Field('closed',css_class='mt-2 col-2')),
                ),
                Div(
                    Row(
                        Field('country', css_class='mt-2 col-3'),
                        Field('state', css_class='mt-2 col-4'),
                        Field('locality', css_class='mt-2 col-5'),
                    )
                ),
                Div(
                    Row(
                        Field('postal_code', css_class='mt-2 col-4'),
                        Field('address', css_class='mt-2 col-8'),
                    ),
                ),
            Div(

                Row(
                    Field('web', css_class='mt-2 col-6'),
                    Field('map', css_class='mt-2 col-4'),
                ),
                Row(
                    Field('logog', css_class='mt-2 col-4'),
                    Field('logop', css_class='mt-2 col-4'),

                ),
                Row(
                    Field('logoboton', css_class='mt-2 col-4'),
                    Field('background', css_class='mt-2 col-4'),
                )


            ),
                HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(HotelForm, self).__init__(*args, **kwargs)

class ProductionGroupForm(forms.ModelForm):

    class Meta:
        model = ProductionGroup
        fields = ['group','description','showincardex',]

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-ProductionGroup'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>ProductionGroup</h3><hr>'),css_class="mt-4"), Field('group',css_class='mt-2'),
 Field('description',css_class='mt-2'),
 Field('showincardex',css_class='mt-2'),
HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(ProductionGroupForm, self).__init__(*args, **kwargs)

class ProductionCenterForm(forms.ModelForm):

    class Meta:
        model = ProductionCenter
        fields = ['center','description','group','crmSegment','tag',]

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-ProductionCenter'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>ProductionCenter</h3><hr>'),css_class="mt-4"), Field('center',css_class='mt-2'),
         Field('description',css_class='mt-2'),
         Field('group',css_class='mt-2'),
         Field('crmSegment',css_class='mt-2'),
         Field('tag',css_class='mt-2'),
HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(ProductionCenterForm, self).__init__(*args, **kwargs)

class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = ['texto','fecha','hotel','habitacion']
        widgets = {
            'fecha': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-Prueba'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(HTML('<h3>Prueba</h3><hr>'),css_class="mt-4"), Field('texto',css_class='mt-2'),
            Field('fecha',css_class='mt-2'),
            Field('hotel', css_class='mt-2'),
            Field('habitacion', css_class='mt-2'),
            HTML('<hr>'),
            )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))

        super(PruebaForm, self).__init__(*args, **kwargs)

        if self.instance:
            self.fields['habitacion'].queryset = RoomType.objects.filter(hotel=self.instance)

class RoomClasificationForm(forms.ModelForm):

    

    class Meta:
        model = RoomClasification
        fields = ['clasification','image',]

        widgets = {
              
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-RoomClasification'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>RoomClasification</h3><hr>'),css_class="mt-4"), Field('clasification',css_class='mt-2'),
 Field('image',css_class='mt-2'),
HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(RoomClasificationForm, self).__init__(*args, **kwargs)

class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ['hotel','code','clasification','name','total','real',]


    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-RoomType'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>RoomType</h3><hr>'),css_class="mt-4"), Field('hotel',css_class='mt-2'),
 Field('code',css_class='mt-2'),
 Field('clasification',css_class='mt-2'),
 Field('name',css_class='mt-2'),
 Field('total',css_class='mt-2'),
 Field('real',css_class='mt-2'),
HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(RoomTypeForm, self).__init__(*args, **kwargs)
                

from master.models import Tax


class TaxForm(forms.ModelForm):

    class Meta:
        model = Tax
        fields = ['name','country','tax','percentage',]

        widgets = {
            'country': autocomplete.ModelSelect2(url='master:country-autocomplete'),
  
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-Tax'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>Tax</h3><hr>'),css_class="mt-4"),
            Field('name', css_class='mt-2'),
            Field('country',css_class='mt-2'),
            Field('tax',css_class='mt-2'),
            Field('percentage',css_class='mt-2'),
        HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(TaxForm, self).__init__(*args, **kwargs)
                

from master.models import SourceGroup


class SourceGroupForm(forms.ModelForm):

    

    class Meta:
        model = SourceGroup
        fields = ['name',]

        widgets = {
              
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-SourceGroup'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>SourceGroup</h3><hr>'),css_class="mt-4"), Field('name',css_class='mt-2'),
HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(SourceGroupForm, self).__init__(*args, **kwargs)
                

from master.models import Source


class SourceForm(forms.ModelForm):


    class Meta:
        model = Source
        fields = ['name','group',]

        widgets = {
            'group': autocomplete.ModelSelect2(url='master:sourcegroup-autocomplete'),
  
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-Source'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>Source</h3><hr>'),css_class="mt-4"), Field('name',css_class='mt-2'),
 Field('group',css_class='mt-2'),
HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(SourceForm, self).__init__(*args, **kwargs)
                

from master.models import SegmentGroup


class SegmentGroupForm(forms.ModelForm):

    

    class Meta:
        model = SegmentGroup
        fields = ['name',]


    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-SegmentGroup'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>SegmentGroup</h3><hr>'),css_class="mt-4"), Field('name',css_class='mt-2'),
HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(SegmentGroupForm, self).__init__(*args, **kwargs)
                

from master.models import Segment


class SegmentForm(forms.ModelForm):

    

    class Meta:
        model = Segment
        fields = ['name','group',]

        widgets = {
            'group': autocomplete.ModelSelect2(url='master:segmentgroup-autocomplete'),
         }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-Segment'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>Segment</h3><hr>'),css_class="mt-4"), Field('name',css_class='mt-2'),
         Field('group',css_class='mt-2'),
        HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(SegmentForm, self).__init__(*args, **kwargs)
                

from master.models import App


class AppForm(forms.ModelForm):

    

    class Meta:
        model = App
        fields = ['name',]

        widgets = {
              
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-App'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>App</h3><hr>'),css_class="mt-4"), Field('name',css_class='mt-2'),
HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(AppForm, self).__init__(*args, **kwargs)
                

from master.models import Model


class ModelForm(forms.ModelForm):

    

    class Meta:
        model = Model
        fields = ['app','model',]

        widgets = {
            'app': autocomplete.ModelSelect2(url='master:app-autocomplete'),
  
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-Model'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>Model</h3><hr>'),css_class="mt-4"), Field('app',css_class='mt-2'),
 Field('model',css_class='mt-2'),
HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(ModelForm, self).__init__(*args, **kwargs)
                

from master.models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['menu','model','url','parent','order']

        widgets = {
            'model': autocomplete.ModelSelect2(url='master:model-autocomplete'),
'parent': autocomplete.ModelSelect2(url='master:menu-autocomplete'),
  
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-Menu'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
        Div(HTML('<h3>Menu</h3><hr>'),css_class="mt-4"),
            Field('menu',css_class='mt-2'),
            Field('model',css_class='mt-2'),
            Field('url',css_class='mt-2'),
            Field('parent',css_class='mt-2'),
            Field('order', css_class='mt-2'),
        HTML('<hr>'),
        )
        self.helper.add_input(Submit('submit', _('Save')))
        self.helper.add_input(Button('back', _('Back'),
                                 css_class='btn-success',
                                 onClick="javascript:history.go(-1);"))
        super(MenuForm, self).__init__(*args, **kwargs)
                