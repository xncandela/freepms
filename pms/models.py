from django.db import models
from django.utils.translation import gettext_lazy as _
from freepms.middleware import get_current_user
from pytz import all_timezones
from django.utils.html import mark_safe

from master.models import BaseModel,Hotel,MealPlan,RoomType
# Create your models here.







STATECHOICES = (('B',_('Booking')),('C','Cancelled'),('I','In House'),('O','Check-out'),('N','No Show'))

class Booking(BaseModel):
    hotel = models.ForeignKey(Hotel,on_delete=models.PROTECT,verbose_name=_('Hotel'))
    state = models.CharField(max_length=1, choices=STATECHOICES,default='B')
    datein = models.DateField(verbose_name=_('Check In Date'))
    dateout = models.DateField(verbose_name=_('Check Out Date'))

    number = models.CharField(max_length=25)
    voucher = models.CharField(max_length=25, null=True, blank=True)

    useroomtype = models.ForeignKey(RoomType, on_delete=models.PROTECT,verbose_name=_('Used Room Type'))
    billingroomtype = models.ForeignKey(RoomType,on_delete=models.PROTECT,verbose_name=_('Billing Room Type'))
    usemealplan = models.ForeignKey(MealPlan, on_delete=models.PROTECT, verbose_name=_('Used Meal Plan'))
    billingmealplan = models.ForeignKey(MealPlan, on_delete=models.PROTECT,verbose_name=_('Billing Meal Plan'))

    def save(self, *args, **kwargs):

        #TODO: Create number funticon

        super(Booking, self).save()



