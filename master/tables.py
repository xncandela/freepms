import django_tables2 as tables
from django.utils.translation import gettext_lazy as _
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from .models import Country
from .models import Currency
from .models import Region
from django.utils.html import format_html

excludeFields = ('created_at', 'updated_at','created_by','modify_by')

class ImageColumn(tables.Column):
    def render(self, value):
        return format_html('<img src="/media/{url}" height="16px", width="auto">',  url=value)


class RegionTable(tables.Table):
    edit = tables.LinkColumn("master:country-update", text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:country-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])

    class Meta:
        model = Region
        template_name = "django_tables2/bootstrap4.html"
        orderable = True
        #exclude = excludeFields

class countryTable(tables.Table):
    edit = tables.LinkColumn("master:country-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:country-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])

    flag = ImageColumn('flag')
    class Meta:
        model = Country
        template_name = "django_tables2/bootstrap4.html"
        orderable = True
        #exclude = excludeFields




class CurrencyTable(tables.Table):

    edit = tables.LinkColumn("master:Currency-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:Currency-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])

    
    class Meta:
        model = Currency
        template_name = "django_tables2/bootstrap4.html"
        orderable = True
        #exclude = excludeFields





from .models import CompanyGroup

class CompanyGroupTable(tables.Table):

    edit = tables.LinkColumn("master:CompanyGroup-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:CompanyGroup-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])

    
    class Meta:
        model = CompanyGroup
        template_name = "django_tables2/bootstrap4.html"
        orderable = True
        #exclude = excludeFields



from .models import Brand

class BrandTable(tables.Table):

    edit = tables.LinkColumn("master:Brand-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:Brand-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])

    
    class Meta:
        model = Brand
        template_name = "django_tables2/bootstrap4.html"
        orderable = True
        #exclude = excludeFields



from .models import Company

class CompanyTable(tables.Table):

    edit = tables.LinkColumn("master:Company-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:Company-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])
    fields = ['name','taxid','phone','email','country','state','locality','postal_code','address','note','color',]

    
    class Meta:
        model = Company
        template_name = "django_tables2/bootstrap4.html"
        orderable = True
        #exclude = excludeFields



from .models import HotelComplex

class HotelComplexTable(tables.Table):

    edit = tables.LinkColumn("master:HotelComplex-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:HotelComplex-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])

    
    class Meta:
        model = HotelComplex
        template_name = "django_tables2/bootstrap4.html"
        orderable = True
        #exclude = excludeFields



from .models import Hotel

class HotelTable(tables.Table):

    edit = tables.LinkColumn("master:Hotel-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:Hotel-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])

    
    class Meta:
        model = Hotel
        template_name = "django_tables2/bootstrap4.html"
        fields = ['code', 'name', 'brand', 'company', 'complex', 'active', 'closed', 'country']
        orderable = True
        #exclude = excludeFields

    

    


from .models import ProductionGroup

class ProductionGroupTable(tables.Table):

    edit = tables.LinkColumn("master:ProductionGroup-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:ProductionGroup-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])

    
    class Meta:
        model = ProductionGroup
        template_name = "django_tables2/bootstrap4.html"
        #exclude = excludeFields
        orderable = True
    


from .models import ProductionCenter

class ProductionCenterTable(tables.Table):

    edit = tables.LinkColumn("master:ProductionCenter-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:ProductionCenter-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])

    
    class Meta:
        model = ProductionCenter
        template_name = "django_tables2/bootstrap4.html"
        #exclude = excludeFields
        orderable = True
    


from .models import Prueba

class PruebaTable(tables.Table):

    edit = tables.LinkColumn("master:Prueba-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:Prueba-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])
    
    
    class Meta:
        model = Prueba
        template_name = "django_tables2/bootstrap4.html"
        orderable=True
        ##exclude = excludeFields

    


from .models import RoomClasification

class RoomClasificationTable(tables.Table):

    edit = tables.LinkColumn("master:RoomClasification-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:RoomClasification-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])
    
    
    class Meta:
        model = RoomClasification
        template_name = "django_tables2/bootstrap4.html"
        orderable=True
        ##exclude = excludeFields

    


from .models import RoomType

class RoomTypeTable(tables.Table):

    edit = tables.LinkColumn("master:RoomType-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:RoomType-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])
    
    
    class Meta:
        model = RoomType
        template_name = "django_tables2/bootstrap4.html"
        orderable=True
        ##exclude = excludeFields

    


from .models import Tax

class TaxTable(tables.Table):

    edit = tables.LinkColumn("master:Tax-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:Tax-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])
    
    
    class Meta:
        model = Tax
        template_name = "django_tables2/bootstrap4.html"
        orderable=True
        #exclude = excludeFields

    


from .models import SourceGroup

class SourceGroupTable(tables.Table):

    edit = tables.LinkColumn("master:SourceGroup-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:SourceGroup-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])
    
    
    class Meta:
        model = SourceGroup
        template_name = "django_tables2/bootstrap4.html"
        orderable=True
        #exclude = excludeFields

    


from .models import Source

class SourceTable(tables.Table):

    edit = tables.LinkColumn("master:Source-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:Source-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])
    
    
    class Meta:
        model = Source
        template_name = "django_tables2/bootstrap4.html"
        orderable=True
        #exclude = excludeFields

    


from .models import SegmentGroup

class SegmentGroupTable(tables.Table):

    edit = tables.LinkColumn("master:SegmentGroup-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:SegmentGroup-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])
    
    
    class Meta:
        model = SegmentGroup
        template_name = "django_tables2/bootstrap4.html"
        orderable=True
        #exclude = excludeFields

    


from .models import Segment

class SegmentTable(tables.Table):

    edit = tables.LinkColumn("master:Segment-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:Segment-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])
    
    
    class Meta:
        model = Segment
        template_name = "django_tables2/bootstrap4.html"
        orderable=True
        #exclude = excludeFields

    


from .models import App

class AppTable(tables.Table):

    edit = tables.LinkColumn("master:App-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:App-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])
    
    
    class Meta:
        model = App
        template_name = "django_tables2/bootstrap4.html"
        orderable=True
        ##exclude = excludeFields

    


from .models import Model

class ModelTable(tables.Table):

    edit = tables.LinkColumn("master:Model-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:Model-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])
    
    
    class Meta:
        model = Model
        template_name = "django_tables2/bootstrap4.html"
        orderable=True
        ##exclude = excludeFields

    


from .models import Menu

class MenuTable(tables.Table):

    edit = tables.LinkColumn("master:Menu-update",text=mark_safe('<i class="bi bi-pencil"></i>'), args=[A("pk")])
    borrar = tables.LinkColumn("master:Menu-delete", text=mark_safe('<i class="bi bi-trash"></i>'), args=[A("pk")])
    
    
    class Meta:
        model = Menu
        template_name = "django_tables2/bootstrap4.html"
        orderable=True
        ##exclude = excludeFields
