from django.db import models
from django.utils.translation import gettext_lazy as _, get_language
from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from freepms.middleware import get_current_user
from pytz import all_timezones
from django.utils.html import mark_safe
from django.db.models.signals import post_save
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import Permission


class App(models.Model):
    name = models.CharField(max_length=15,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Model(models.Model):
    app = models.ForeignKey(App,on_delete=models.CASCADE)
    model = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.app}.{self.model}'

    @property
    def url(self):
        return f'{self.app.name}:{self.model}'

    class Meta:
        ordering = ('app','model')
        unique_together = ('app','model')

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=150, null=True,blank=True,editable=False)
    modify_by =  models.CharField(max_length=150, null=True,blank=True,editable=False)

    def save(self, *args, **kwargs):
        currentuser = get_current_user()
        if not self.pk:
            self.created_by = currentuser.username
        self.modify_by = currentuser.username

        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True

AddressTypeChoice = ((1,_('Personal Address')),(2,_('Fiscal Address')),(3,_('Shipping Address')))

class Address(models.Model):
    '''
    Abstract models for address
    '''
    country = models.ForeignKey('Country',on_delete=models.PROTECT,verbose_name=_('Country'))
    state = models.CharField(max_length=25,null=True,blank=True,verbose_name=_('State'))
    locality = models.CharField(max_length=25,null=True,blank=True,verbose_name=_('Locality'))
    postal_code =models.CharField(max_length=25,null=True,blank=True,verbose_name=_('Postal Code'))
    address = models.CharField(max_length=150,null=True,blank=True,verbose_name=_('Address'))

    class Meta:
        abstract = True

TIMEZONECHOICE = [(a,a) for a in all_timezones]

class Menu(models.Model):
    menu = models.CharField(max_length=20,verbose_name='Menu')
    model = models.ForeignKey(Model,null=True,blank=True,on_delete=models.PROTECT)
    url = models.CharField(max_length=100,null=True,blank=True)

    parent = models.ForeignKey('Menu', null=True, blank=True,limit_choices_to={'grouping': True}, on_delete=models.PROTECT, related_name='padre')
    order = models.PositiveSmallIntegerField(default=100)
    grouping = models.BooleanField(default=False,editable=False)

    def save(self,*args,**kwargs):
        if self.model:
            self.url = self.model.url+'-list'
            self.grouping = False
        else:
            self.grouping = True
            if not self.pk:
                self.order = 20

        super(Menu, self).save(*args,**kwargs)

    def __str__(self):
        return self.menu

    class Meta:
        ordering = ('order','menu')

#Ok
class Region(models.Model):
    '''
    Region Group of countries
    '''

    name = models.CharField(max_length=15,verbose_name=_('Name'))
    color = ColorField(default='#FF0000',verbose_name=_('Color'))
    order = models.IntegerField(default=100, verbose_name=_('Order'))

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')
        ordering = ('order', 'name')

    def __str__(self):
        return self.name
#Ok

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name=_('Code'))
    description = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Description'))
    numcode = models.CharField(max_length=3, unique=True, verbose_name=_('Numeric Code'))
    decimal = models.PositiveSmallIntegerField(default=2,verbose_name=_('Decimal positions'))


    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = _('Currency')
        verbose_name = _('Currencies')
        ordering = ('code',)
#Ok

class Country(models.Model):
    """
    Country model baased in ISO 3166-1
    """
    iso2 = models.CharField(max_length=2, unique=True)
    iso3 = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    flag = models.ImageField(upload_to='banderas', null=True, blank=True, verbose_name=_('Flag'))
    calling_code = models.CharField(max_length=10, null=True, blank=True,verbose_name=_('Calling Code'))
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True, blank=True,verbose_name=_('Region'))
    currencies = models.ManyToManyField(Currency,verbose_name=_('Currencies'))
    order = models.IntegerField(default=100,verbose_name=_('Order'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Countries')
        verbose_name = _('Country')
        ordering = ('order','iso2', 'iso3')
#Ok

class CompanyGroup(models.Model):
    '''
    Company Group
    '''
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    color = ColorField(default='#FF0000', verbose_name=_('Color'))
    order = models.IntegerField(default=100, verbose_name=_('Order'))
    logo = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name=_('Logo'))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()

        super(CompanyGroup, self).save(*args, **kwargs)

    class Meta:
        ordering =('order','name')
#Ok
class Brand(models.Model):
    '''
    Hotel´s brands
    '''
    name = models.CharField(max_length=25, verbose_name=_('Name'))
    group = models.ForeignKey(CompanyGroup,on_delete=models.PROTECT,verbose_name=_('Group'))
    color = ColorField(default='#FF0000', verbose_name=_('Color'))
    order = models.IntegerField(default=100, verbose_name=_('Order'))
    logo = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name=_('Logo'))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Brand, self).save(*args, **kwargs)

    class Meta:
        ordering = ('order', 'name')
#Ok
class Company(Address):
    '''
    Companies owner of hotels
    '''
    name = models.CharField(_('Name'),max_length=100)
    taxid = models.CharField(_('Tax ID'),max_length=15)
    phone = models.CharField(_('Phone'),max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=75, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    color = ColorField(default='#FFFFFF')
    of = models.BooleanField(default=False)
    hotels = models.ManyToManyField('Hotel')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Company, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
#Ok
class HotelComplex(Address):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
#Ok
class Hotel(Address):
    code = models.CharField(max_length=10 ,unique=True,verbose_name=_('Code'))
    name = models.CharField(max_length=50)
    color = ColorField(default='#FFFFFF')
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,verbose_name=_('Brand'))
    complex = models.ForeignKey(HotelComplex,on_delete=models.PROTECT,verbose_name=_('Complex'))
    basecurrency = models.ForeignKey(Currency,on_delete=models.PROTECT,verbose_name=_('Currency'))
    timezone = models.CharField(max_length=35, choices=TIMEZONECHOICE, default='UTC',verbose_name='Time Zone')

    active = models.BooleanField(default=False, verbose_name=_('Active'))
    closed = models.BooleanField(default=False, verbose_name=_('Closed'))

    web = models.URLField(blank=True,null=True,verbose_name=_('Web'))
    map = models.ImageField(upload_to='hotel/maps', verbose_name=_('Map'), null=True, blank=True)
    logog = models.ImageField(upload_to='hotel/logo', verbose_name=_('Big logo'), null=True, blank=True)
    logop = models.ImageField(upload_to='hotel/logo', verbose_name=_('Small logo'), null=True, blank=True)
    logoboton = models.ImageField(upload_to='hotel/logo', verbose_name=_('Button logo'), null=True, blank=True)
    background = models.ImageField(upload_to='hotel/images', verbose_name=_('BackGroud'), null=True, blank=True)

    def __str__(self):
        return self.code

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ManyToManyField(Company)
    hotels = models.ManyToManyField(Hotel)
    hoteldefault = models.ForeignKey(Hotel,on_delete=models.PROTECT,related_name='hoteldefault')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('Employee')

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = Employee.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

class CrmSegment(models.Model):
    code = models.CharField(max_length=10,unique=True,verbose_name=_('Code'))
    description = models.CharField(max_length=50, null=True, blank=True,verbose_name=_('Description'))

    def __str__(self):
        return self.code

#
# class OperationSegment(models.Model):
#     segmento = models.CharField(max_length=25, verbose_name=_('Segmento'))
#     segmento_en = models.CharField(max_length=25, verbose_name=_('Segmento'), null=True, blank=True)
#     abreviatura = models.CharField(max_length=5, verbose_name=_('Abreviatura'), null=True)
#     color = ColorField(null=True, blank=True, default='#ffffff', verbose_name=_('Color'))
#     repetitivo = models.BooleanField(default=False, verbose_name='¿Es Repetitivo?')
#     topten = models.BooleanField(default=False, verbose_name='¿Es TopTen?')
#     sinasignacion = models.BooleanField(default=False, verbose_name='¿Es Sin asignacion?')
#     cumpleañero = models.BooleanField(default=False, verbose_name='¿Es Cumpleañero?')
#     aniversario = models.BooleanField(default=False, verbose_name='¿Es Aniversario?')
#     focorojo = models.BooleanField(default=False, verbose_name='¿Es Foco Rojo?')
#
#     codloyalty = models.ForeignKey(NivelFidelizacion, blank=True, null=True, verbose_name=_('Codigo loyalty'), on_delete=models.CASCADE)
#     esalergia = models.BooleanField(default=False, verbose_name='¿Es alergia?')
#
#     def clean(self):
#
#         if self.repetitivo:
#             if SegmentoOperacion.objects.filter(repetitivo=True).count() > 1:
#                 raise ValidationError('Solo puede haber un tipo de incidencia de tipo Repetitivo')
#
#         if self.topten:
#             if SegmentoOperacion.objects.filter(topten=True).count() > 1:
#                 raise ValidationError('Solo puede haber un tipo de incidencia de tipo TopTen')
#
#         if self.sinasignacion:
#             if SegmentoOperacion.objects.filter(sinasignacion=True).count() > 1:
#                 raise ValidationError('Solo puede haber un tipo de incidencia de tipo Sin Asignacion')
#
#         if self.cumpleañero:
#             if SegmentoOperacion.objects.filter(cumpleañero=True).count() > 1:
#                 raise ValidationError('Solo puede haber un tipo de incidencia de tipo Cumpleañero')
#
#         if self.aniversario:
#             if SegmentoOperacion.objects.filter(aniversario=True).count() > 1:
#                 raise ValidationError('Solo puede haber un tipo de incidencia de tipo Aniversario')
#
#         if self.esalergia:
#             if SegmentoOperacion.objects.filter(esalergia=True).count() > 1:
#                 raise ValidationError('Solo puede haber un tipo de incidencia de tipo Alergia')
#
#     def __str__(self):
#
#         if get_language() == 'en':
#             return self.segmento_en or self.segmento
#         else:
#             return self.segmento
#
#     class Meta:
#         ordering = ('segmento',)
#         verbose_name_plural = 'Segmentos Operacion'
#         verbose_name = 'Segmento Operacion'
#
#

#Ok
#Ok
class ProductionGroup(models.Model):
    group = models.CharField(max_length=10, unique=True,verbose_name=_('Group'))
    description = models.CharField(max_length=50, null=True, blank=True,verbose_name=_('Description'))
    showincardex = models.BooleanField(default=False,verbose_name=_('Show in Cardex'))

    def __str__(self):
        return self.group

    class Meta:
        ordering = ('group',)
#Ok
class ProductionCenter(models.Model):
    center = models.CharField(max_length=10, unique=True,verbose_name=_('Center'))
    description = models.CharField(max_length=50, null=True, blank=True,verbose_name=_('Description'))
    group = models.ForeignKey(ProductionGroup, on_delete=models.PROTECT, null=True,verbose_name=_('Group'))
    crmSegment = models.ForeignKey(CrmSegment,  verbose_name=_('Segmento CRM'),on_delete=models.PROTECT,null=True,blank=True)
    tag = models.CharField(max_length=15, null=True, blank=True,verbose_name=_('Tag'))


    @property
    def showincardex(self):
        return self.grupo.showincardex

    def __str__(self):
        return self.center

    class Meta:
        ordering = ('group','center')
#Ok
class Tax(models.Model):
    name = models.CharField(max_length=15, verbose_name=_('Name'))
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name=_('Country'))
    tax = models.CharField(max_length=15,verbose_name=_('Tax'))
    percentage = models.DecimalField(max_digits=4,decimal_places=2,verbose_name=_('Percentage'),default=0.0)

    def clean(self):
        if self.percentage < 0:
            raise ValidationError(_('Negative values not permited'))

        if self.percentage >99.99:
            raise ValidationError(_('Value not permited'))

    def __str__(self):
        return self.tax

    class Meta:
        unique_together = ('tax','country')
        ordering = ('country','tax')

class TaxStructure(models.Model):
    description = models.CharField(max_length=20,verbose_name=_('Description'))
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name=_('Country'))
    dateto = models.DateField(null=True,blank=True,verbose_name=_('Aplication to date'))


    def __str__(self):
        return self.description

    class Meta:
        unique_together = ('description','country')
        ordering = ('country','description')

#Ok
class SourceGroup(models.Model):
    name = models.CharField(max_length=20,verbose_name=_('Name'),unique=True)

    def __str__(self):
        return self.name

#Ok
class Source(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('Name'))
    group = models.ForeignKey(SourceGroup,on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} - ({self.group})'

    class Meta():
        unique_together = ('name','group')

class SegmentGroup(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('Name'), unique=True)

    def __str__(self):
        return self.name

class Segment(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('Name'))
    group = models.ForeignKey(SegmentGroup,on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} - ({self.group})'

    class Meta():
        unique_together = ('name','group')

class MarketGroup(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('Name'), unique=True)

    def __str__(self):
        return self.name

class Market(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('Name'), unique=True)
    group = models.ForeignKey(MarketGroup, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} - ({self.group})'

    class Meta():
        unique_together = ('name','group')

SELLERTYPE = (('T',_('TTOO')),('A',_('Agency')))
SELLERCLIENTTYPE = (('C',_('Company')),('D',_('Direct')))
class Seller(Address):
    code=models.CharField(max_length=25,unique=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=1,choices=SELLERTYPE,default='T')
    clienttype = models.CharField(max_length=1, choices=SELLERCLIENTTYPE,default='C')
    agencies = models.ManyToManyField('Seller',limit_choices_to={'type':'A'})
    segment = models.ForeignKey(Segment,on_delete=models.PROTECT,verbose_name=_('Default Segment'),null=True,blank=True)
    source = models.ForeignKey(Source,on_delete=models.PROTECT,verbose_name=_('Default Source'),null=True,blank=True)
    market = models.ForeignKey(Market,on_delete=models.PROTECT,verbose_name=_('Default Market'),null=True,blank=True)

    def __str__(self):
        return f'{self.name} - ({self.type})'

    class Meta:
        verbose_name=_('Seller')

class Client(Address):
    code=models.CharField(max_length=25,unique=True)
    name = models.CharField(max_length=50)
    sellers = models.ManyToManyField(Seller)

#### MEALPLAN ###################
class MealPlanType(models.Model):
    name = models.CharField(max_length=25,unique=True)
    desert = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class MealPlan(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.PROTECT)
    mealplan = models.ForeignKey(MealPlanType,on_delete=models.PROTECT)

    def __str__(self):
        return self.mealplan

    class Meta:
        unique_together = ('hotel','mealplan')



#### ROOMS ###################

#ok
class RoomClasification(models.Model):
    clasification = models.CharField(max_length=15)
    image = models.ImageField(upload_to='roomclasi', null=True, blank=True)


    def __str__(self):
        return self.clasification

    def image_thumb(self):
        if self.imagen:
            return mark_safe(f'<img src="{self.image.url}" width=24 height=24 title="{self.clasification}"/>')
        else:
            return self.clasification
#ok
class RoomType(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.PROTECT, verbose_name=_('Hotel'))
    code = models.CharField(max_length=10, verbose_name=_('Code'))
    clasification = models.ForeignKey(RoomClasification, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, verbose_name=_('Nombre'), blank=True)
    total = models.IntegerField(default=0, verbose_name=_('Cantidad'))
    real = models.BooleanField(default=True, verbose_name=_('Real'))

    # points = models.DecimalField(default=1.0, max_digits=3, decimal_places=1, verbose_name=_('Cleaning Points'))
    # points_in = models.DecimalField(default=0.0, max_digits=3, decimal_places=1, verbose_name=_('Cleaning Points at CheckIn'))
    # points_out = models.DecimalField(default=0.0, max_digits=3, decimal_places=1, verbose_name=_('Cleaning Points at CheckOut'))
    #
    # base = models.BooleanField(default=False, verbose_name=_('Habitacion base'))
    # baseincrease = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, verbose_name=_('Incremento respecto base (porcentaje'))
    # baseincreaseamount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name=_('Incremento respecto base (importe)'))

    def __str__(self):
        return f'{self.code}'


    def save(self, *args, **kwargs):
        # if self.base:
        #     num = self.__class__.objects.filter(hotel=self.hotel, base=True).exists()
        #     if num:
        #         self.base = False
        #     else:
        #         self.baseincrease = 0
        #         self.baseincreaseamount = 0

        super(RoomType, self).save(*args, **kwargs)

    class Meta:

        index_together = ['hotel', 'code']




APLICATIONTAX_CHOICES = (('L',_('Last result')),('B','Base'))
class TaxStructureLine(models.Model):
    taxcab = models.ForeignKey(TaxStructure,on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(default=10)
    tax = models.ForeignKey(Tax,on_delete=models.PROTECT)
    aplication = models.CharField(max_length=1,choices=APLICATIONTAX_CHOICES,default='L')

    class Meta:
        unique_together = ('taxcab','order')
        ordering = ('order','taxcab')

class TaxByProductionCenter(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name=_('Country'))
    productioncenter = models.ForeignKey(ProductionCenter,on_delete=models.PROTECT, verbose_name=_('Production Center'))
    taxstructure = models.ForeignKey(TaxStructure,on_delete=models.PROTECT, verbose_name=_('Tax Structure'))

    class Meta:
        unique_together = ('country','productioncenter')
        ordering = ('country','productioncenter')


class Tip(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, verbose_name=_('Hotel'))
    tip = models.CharField(max_length=15,verbose_name=_('Tip'))
    percentage = models.BooleanField(default=0,verbose_name=_('Percentage?'))
    value = models.DecimalField(max_digits=4,decimal_places=2,verbose_name=_('Value'),default=0.0)
    #se calcula del total o de un centro

    class Meta:
        unique_together = ('hotel','tip')

class CityTax(models.Model):
    pass


class Prueba(models.Model):
    texto = models.CharField(max_length=10)
    fecha = models.DateField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,null=True,blank=True)
    habitacion = models.ForeignKey(RoomType,on_delete=models.CASCADE,null=True,blank=True)

