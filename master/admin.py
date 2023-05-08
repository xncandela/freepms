from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from master.models import Region,Employee
# Register your models here.


from master.models import CompanyGroup
        
@admin.register(CompanyGroup)
class CompanyGroupAdmin(admin.ModelAdmin):
    list_display = ('id','name','color','order')
        


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id','name','color','order',)
            
from master.models import Country
        
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id','iso2','iso3','name','flag','calling_code','region','order',)
    search_fields = ('iso2','iso3','name')
    list_filter = ('region',)
        
from master.models import Currency
        
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id','code','description','numcode','decimal',)
    search_fields = ('code','numcode')
    filter_horizontal = ('countries',)
        
from master.models import Brand
        
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name','group','color','order','logo')
        

from master.models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','country','state','locality','postal_code','address','name','taxid','phone','email','note','color')
        
from master.models import HotelComplex
        
@admin.register(HotelComplex)
class HotelComplexAdmin(admin.ModelAdmin):
    list_display = ('name','country','state','locality','postal_code','address',)



        
from master.models import Hotel
        
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('country','state','locality','postal_code','address','code','name','color','brand','company','complex','basecurrency','timezone','active','closed','web','map','logog','logop','logoboton','background',)
        

        

from master.models import ProductionGroup
        
@admin.register(ProductionGroup)
class ProductionGroupAdmin(admin.ModelAdmin):
    list_display = ('group','description','showincardex',)
            
from master.models import ProductionCenter
        
@admin.register(ProductionCenter)
class ProductionCenterAdmin(admin.ModelAdmin):
    list_display = ('center','description','group','crmSegment','tag',)
            
from master.models import Prueba
        
@admin.register(Prueba)
class PruebaAdmin(admin.ModelAdmin):
    list_display = ('texto','fecha',)


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
from master.models import RoomClasification
        
@admin.register(RoomClasification)
class RoomClasificationAdmin(admin.ModelAdmin):
    list_display = ('clasification','image',)
            
from master.models import RoomType
        
@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('hotel','code','clasification','name','total','real',)
            
from master.models import Tax
        
@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('country','tax','percentage',)
            
from master.models import SourceGroup
        
@admin.register(SourceGroup)
class SourceGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
            
from master.models import Source
        
@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name','group',)
            
from master.models import SegmentGroup
        
@admin.register(SegmentGroup)
class SegmentGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
            
from master.models import Segment
        
@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    list_display = ('name','group',)



from master.models import App
        
@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('name',)
            
from master.models import Menu
        
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu','model','url','parent',)
            