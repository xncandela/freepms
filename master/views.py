


##################
from django.views.generic import ListView,DeleteView,DetailView,CreateView,UpdateView
from django.shortcuts import render, reverse,redirect
from dal import autocomplete

from django_tables2 import SingleTableView
from django.urls import reverse_lazy

from .functions import load_apps

from .forms import RegionForm
from .tables import RegionTable
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.db.models import Q

from .forms import countryForm
from .tables import countryTable
from .models import Country
from .models import Region
from .forms import CurrencyForm
from .tables import CurrencyTable
from .models import Currency





####################

class RegionList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_Region'
    model = Region
    template_name = 'master/crud/Region_list.html'
    table_class = RegionTable
    table_pagination = False

    def get_queryset(self):

        search = self.request.GET.get('search',None)
        if search:
            queryset = Region.objects.filter( Q(name__icontains=search))
        else:
            queryset = Region.objects.all()
        return queryset


class RegionCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_Region'
    model = Region
    form_class = RegionForm
    success_url = reverse_lazy('master:Region-list')
    template_name = 'master/crud/Region_form.html'

class RegionUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_Region'
    model = Region
    template_name = 'master/crud/Region_form.html'
    form_class = RegionForm
    success_url = reverse_lazy('master:Region-list')

class RegionDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_Region'
    model = Region
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:Region-list')


class RegionAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Region.objects.none()
        qs = Region.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

####################

class CountryList(PermissionRequiredMixin, SingleTableView):
    permission_required = 'master.view_country'
    model = Country
    template_name = 'master/crud/country_list.html'
    table_class = countryTable
    table_pagination = False

    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
            queryset = Country.objects.filter(Q(id__icontains=search) | Q(iso2__icontains=search) | Q(iso3__icontains=search) | Q(name__icontains=search) | Q(calling_code__icontains=search)|Q(order__icontains=search))

        else:
            queryset = Country.objects.all()
        return queryset

    # def get_context_data(self, **kwargs):
    #     print('Context:',self,**kwargs)

class CountryCreate(PermissionRequiredMixin, CreateView):  # LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_country'
    model = Country
    form_class = countryForm
    success_url = reverse_lazy('master:Country-list')
    template_name = 'master/crud/country_form.html'

class CountryUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'master.change_country'
    model = Country
    template_name = 'master/crud/country_form.html'
    form_class = countryForm
    success_url = reverse_lazy('master:Country-list')

class CountryDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'master.delete_country'
    model = Country
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:Country-list')

class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Country.objects.none()
        qs = Country.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


####################

class CurrencyList(PermissionRequiredMixin, SingleTableView):
    permission_required = 'master.view_Currency'
    model = Currency
    template_name = 'master/crud/Currency_list.html'
    table_class = CurrencyTable
    table_pagination = False

    def get_queryset(self):
        search = self.request.GET.get('search', None)
        if search:
            queryset = Currency.objects.filter(
                Q(id__icontains=search) | Q(code__icontains=search) | Q(description__icontains=search) | Q(numcode__icontains=search) | Q(decimal__icontains=search))
        else:
            queryset = Currency.objects.all()
        return queryset


class CurrencyCreate(PermissionRequiredMixin, CreateView):  # LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_Currency'
    model = Currency
    form_class = CurrencyForm
    success_url = reverse_lazy('master:Currency-list')
    template_name = 'master/crud/Currency_form.html'


class CurrencyUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'master.change_Currency'
    model = Currency
    template_name = 'master/crud/Currency_form.html'
    form_class = CurrencyForm
    success_url = reverse_lazy('master:Currency-list')


class CurrencyDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'master.delete_Currency'
    model = Currency
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:Currency-list')

class CurrencyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Currency.objects.none()
        qs = Currency.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs




from .forms import CompanyGroupForm
from .tables import CompanyGroupTable
from .models import CompanyGroup
####################

class CompanyGroupList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_CompanyGroup'
    model = CompanyGroup
    template_name = 'master/crud/CompanyGroup_list.html'
    table_class = CompanyGroupTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = CompanyGroup.objects.filter(Q(id__icontains=search) |Q(created_at__icontains=search) |Q(updated_at__icontains=search) |Q(name__icontains=search) |Q(color__icontains=search) |Q(order__icontains=search) )
        else:
            queryset = CompanyGroup.objects.all()
        return queryset


class CompanyGroupCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_CompanyGroup'
    model = CompanyGroup
    form_class = CompanyGroupForm
    success_url = reverse_lazy('master:CompanyGroup-list')
    template_name = 'master/crud/CompanyGroup_form.html'

class CompanyGroupUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_CompanyGroup'
    model = CompanyGroup
    template_name = 'master/crud/CompanyGroup_form.html'
    form_class = CompanyGroupForm
    success_url = reverse_lazy('master:CompanyGroup-list')

class CompanyGroupDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_CompanyGroup'
    model = CompanyGroup
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:CompanyGroup-list')

class CompanyGroupAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return CompanyGroup.objects.none()
        qs = CompanyGroup.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


from .forms import BrandForm
from .tables import BrandTable
from .models import Brand
####################

class BrandList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_Brand'
    model = Brand
    template_name = 'master/crud/Brand_list.html'
    table_class = BrandTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = Brand.objects.filter(Q(id__icontains=search) |Q(created_at__icontains=search) |Q(updated_at__icontains=search) |Q(created_by__icontains=search) |Q(modify_by__icontains=search) |Q(name__icontains=search) |Q(color__icontains=search) |Q(order__icontains=search) )
        else:
            queryset = Brand.objects.all()
        return queryset


class BrandCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_Brand'
    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy('master:Brand-list')
    template_name = 'master/crud/Brand_form.html'

class BrandUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_Brand'
    model = Brand
    template_name = 'master/crud/Brand_form.html'
    form_class = BrandForm
    success_url = reverse_lazy('master:Brand-list')

class BrandDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_Brand'
    model = Brand
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:Brand-list')

class BrandAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Brand.objects.none()
        qs = Brand.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


from .forms import CompanyForm
from .tables import CompanyTable
from .models import Company
####################

class CompanyList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_Company'
    model = Company
    template_name = 'master/crud/Company_list.html'
    table_class = CompanyTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = Company.objects.filter(Q(id__icontains=search) |Q(state__icontains=search) |Q(locality__icontains=search) |Q(postal_code__icontains=search) |Q(address__icontains=search) |Q(name__icontains=search) |Q(taxid__icontains=search) |Q(phone__icontains=search) |Q(email__icontains=search) |Q(color__icontains=search) )
        else:
            queryset = Company.objects.all()
        return queryset


class CompanyCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_Company'
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('master:Company-list')
    template_name = 'master/crud/Company_form.html'

class CompanyUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_Company'
    model = Company
    template_name = 'master/crud/Company_form.html'
    form_class = CompanyForm
    success_url = reverse_lazy('master:Company-list')

class CompanyDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_Company'
    model = Company
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:Company-list')

    
class CompanyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Company.objects.none()
        qs = Company.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

from .forms import HotelComplexForm
from .tables import HotelComplexTable
from .models import HotelComplex
####################

class HotelComplexList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_HotelComplex'
    model = HotelComplex
    template_name = 'master/crud/HotelComplex_list.html'
    table_class = HotelComplexTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = HotelComplex.objects.filter(Q(id__icontains=search) |Q(created_at__icontains=search) |Q(updated_at__icontains=search) |Q(created_by__icontains=search) |Q(modify_by__icontains=search) |Q(state__icontains=search) |Q(locality__icontains=search) |Q(postal_code__icontains=search) |Q(address__icontains=search) |Q(name__icontains=search) )
        else:
            queryset = HotelComplex.objects.all()
        return queryset


class HotelComplexCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_HotelComplex'
    model = HotelComplex
    form_class = HotelComplexForm
    success_url = reverse_lazy('master:HotelComplex-list')
    template_name = 'master/crud/HotelComplex_form.html'

class HotelComplexUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_HotelComplex'
    model = HotelComplex
    template_name = 'master/crud/HotelComplex_form.html'
    form_class = HotelComplexForm
    success_url = reverse_lazy('master:HotelComplex-list')

class HotelComplexDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_HotelComplex'
    model = HotelComplex
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:HotelComplex-list')

    
class HotelComplexAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return HotelComplex.objects.none()
        qs = HotelComplex.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

from .forms import HotelForm
from .tables import HotelTable
from .models import Hotel
####################

class HotelList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_Hotel'
    model = Hotel
    template_name = 'master/crud/Hotel_list.html'
    table_class = HotelTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = Hotel.objects.filter(Q(id__icontains=search) |Q(created_at__icontains=search) |Q(updated_at__icontains=search) |Q(created_by__icontains=search) |Q(modify_by__icontains=search) |Q(state__icontains=search) |Q(locality__icontains=search) |Q(postal_code__icontains=search) |Q(address__icontains=search) |Q(code__icontains=search) |Q(name__icontains=search) |Q(color__icontains=search) |Q(timezone__icontains=search) |Q(web__icontains=search) )
        else:
            queryset = Hotel.objects.all()
        return queryset


class HotelCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_Hotel'
    model = Hotel
    form_class = HotelForm
    success_url = reverse_lazy('master:Hotel-list')
    template_name = 'master/crud/Hotel_form.html'

class HotelUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_Hotel'
    model = Hotel
    template_name = 'master/crud/Hotel_form.html'
    form_class = HotelForm
    success_url = reverse_lazy('master:Hotel-list')

class HotelDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_Hotel'
    model = Hotel
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:Hotel-list')


class HotelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Hotel.objects.none()
        qs = Hotel.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


from .forms import ProductionGroupForm
from .tables import ProductionGroupTable
from .models import ProductionGroup
####################

class ProductionGroupList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_ProductionGroup'
    model = ProductionGroup
    template_name = 'master/productiongroup/ProductionGroup_list.html'
    table_class = ProductionGroupTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = ProductionGroup.objects.filter(Q(created_by__icontains=search) |Q(modify_by__icontains=search) |Q(group__icontains=search) |Q(description__icontains=search) )
        else:
            queryset = ProductionGroup.objects.all()
        return queryset


class ProductionGroupCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_ProductionGroup'
    model = ProductionGroup
    form_class = ProductionGroupForm
    success_url = reverse_lazy('master:ProductionGroup-list')
    template_name = 'master/ProductionGroup/ProductionGroup_form.html'

class ProductionGroupUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_ProductionGroup'
    model = ProductionGroup
    template_name = 'master/ProductionGroup/ProductionGroup_form.html'
    form_class = ProductionGroupForm
    success_url = reverse_lazy('master:ProductionGroup-list')

class ProductionGroupDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_ProductionGroup'
    model = ProductionGroup
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:ProductionGroup-list')


class ProductionGroupAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return ProductionGroup.objects.none()
        qs = ProductionGroup.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs



from .forms import ProductionCenterForm
from .tables import ProductionCenterTable
from .models import ProductionCenter
####################

class ProductionCenterList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_ProductionCenter'
    model = ProductionCenter
    template_name = 'master/productioncenter/ProductionCenter_list.html'
    table_class = ProductionCenterTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = ProductionCenter.objects.filter(Q(created_by__icontains=search) |Q(modify_by__icontains=search) |Q(center__icontains=search) |Q(description__icontains=search) |Q(tag__icontains=search) )
        else:
            queryset = ProductionCenter.objects.all()
        return queryset


class ProductionCenterCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_ProductionCenter'
    model = ProductionCenter
    form_class = ProductionCenterForm
    success_url = reverse_lazy('master:ProductionCenter-list')
    template_name = 'master/ProductionCenter/ProductionCenter_form.html'

class ProductionCenterUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_ProductionCenter'
    model = ProductionCenter
    template_name = 'master/ProductionCenter/ProductionCenter_form.html'
    form_class = ProductionCenterForm
    success_url = reverse_lazy('master:ProductionCenter-list')

class ProductionCenterDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_ProductionCenter'
    model = ProductionCenter
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:ProductionCenter-list')

class ProductionCenterAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return ProductionCenter.objects.none()
        qs = ProductionCenter.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


from .forms import PruebaForm
from .tables import PruebaTable
from .models import Prueba
####################

class PruebaList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_Prueba'
    model = Prueba
    template_name = 'master/prueba/Prueba_list.html'
    table_class = PruebaTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = Prueba.objects.filter(Q(texto__icontains=search) |Q(fecha__icontains=search) )
        else:
            queryset = Prueba.objects.all()
        return queryset


class PruebaCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_Prueba'
    model = Prueba
    form_class = PruebaForm
    success_url = reverse_lazy('master:Prueba-list')
    template_name = 'master/Prueba/Prueba_form.html'

class PruebaUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_Prueba'
    model = Prueba
    template_name = 'master/Prueba/Prueba_form.html'
    form_class = PruebaForm
    success_url = reverse_lazy('master:Prueba-list')

class PruebaDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_Prueba'
    model = Prueba
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:Prueba-list')


class PruebaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Prueba.objects.none()
        qs = Prueba.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs



from .forms import RoomClasificationForm
from .tables import RoomClasificationTable
from .models import RoomClasification
####################

class RoomClasificationList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_RoomClasification'
    model = RoomClasification
    template_name = 'master/roomclasification/RoomClasification_list.html'
    table_class = RoomClasificationTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = RoomClasification.objects.filter(Q(clasification__icontains=search) )
        else:
            queryset = RoomClasification.objects.all()
        return queryset


class RoomClasificationCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_RoomClasification'
    model = RoomClasification
    form_class = RoomClasificationForm
    success_url = reverse_lazy('master:RoomClasification-list')
    template_name = 'master/RoomClasification/RoomClasification_form.html'

class RoomClasificationUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_RoomClasification'
    model = RoomClasification
    template_name = 'master/RoomClasification/RoomClasification_form.html'
    form_class = RoomClasificationForm
    success_url = reverse_lazy('master:RoomClasification-list')

class RoomClasificationDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_RoomClasification'
    model = RoomClasification
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:RoomClasification-list')


class RoomClasificationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return RoomClasification.objects.none()
        qs = RoomClasification.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs




from .forms import RoomTypeForm
from .tables import RoomTypeTable
from .models import RoomType
####################

class RoomTypeList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_RoomType'
    model = RoomType
    template_name = 'master/roomtype/RoomType_list.html'
    table_class = RoomTypeTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = RoomType.objects.filter(Q(code__icontains=search) |Q(name__icontains=search) |Q(total__icontains=search) )
        else:
            queryset = RoomType.objects.all()
        return queryset


class RoomTypeCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_RoomType'
    model = RoomType
    form_class = RoomTypeForm
    success_url = reverse_lazy('master:RoomType-list')
    template_name = 'master/RoomType/RoomType_form.html'

class RoomTypeUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_RoomType'
    model = RoomType
    template_name = 'master/RoomType/RoomType_form.html'
    form_class = RoomTypeForm
    success_url = reverse_lazy('master:RoomType-list')

class RoomTypeDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_RoomType'
    model = RoomType
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:RoomType-list')

class RoomTypeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return RoomType.objects.none()
        qs = RoomType.objects.all()

        clasification = self.forwarded.get('clasification', None)
        hotel = self.forwarded.get('hotel', None)

        if clasification:
            qs = qs.filter(continent=clasification)

        if hotel:
            qs = qs.filter(continent=hotel)


        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

from .forms import TaxForm
from .tables import TaxTable
from .models import Tax
####################

class TaxList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_Tax'
    model = Tax
    template_name = 'master/tax/Tax_list.html'
    table_class = TaxTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = Tax.objects.filter(Q(created_by__icontains=search) |Q(modify_by__icontains=search) |Q(tax__icontains=search) )
        else:
            queryset = Tax.objects.all()
        return queryset

class TaxCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_Tax'
    model = Tax
    form_class = TaxForm
    success_url = reverse_lazy('master:Tax-list')
    template_name = 'master/Tax/Tax_form.html'

class TaxUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_Tax'
    model = Tax
    template_name = 'master/Tax/Tax_form.html'
    form_class = TaxForm
    success_url = reverse_lazy('master:Tax-list')

class TaxDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_Tax'
    model = Tax
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:Tax-list')
    
class TaxAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Tax.objects.none()
        qs = Tax.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

        

from .forms import SourceGroupForm
from .tables import SourceGroupTable
from .models import SourceGroup
####################

class SourceGroupList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_SourceGroup'
    model = SourceGroup
    template_name = 'master/sourcegroup/SourceGroup_list.html'
    table_class = SourceGroupTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = SourceGroup.objects.filter(Q(created_by__icontains=search) |Q(modify_by__icontains=search) |Q(name__icontains=search) )
        else:
            queryset = SourceGroup.objects.all()
        return queryset


class SourceGroupCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_SourceGroup'
    model = SourceGroup
    form_class = SourceGroupForm
    success_url = reverse_lazy('master:SourceGroup-list')
    template_name = 'master/SourceGroup/SourceGroup_form.html'

class SourceGroupUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_SourceGroup'
    model = SourceGroup
    template_name = 'master/SourceGroup/SourceGroup_form.html'
    form_class = SourceGroupForm
    success_url = reverse_lazy('master:SourceGroup-list')

class SourceGroupDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_SourceGroup'
    model = SourceGroup
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:SourceGroup-list')
    
class SourceGroupAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return SourceGroup.objects.none()
        qs = SourceGroup.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

        

from .forms import SourceForm
from .tables import SourceTable
from .models import Source
####################

class SourceList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_Source'
    model = Source
    template_name = 'master/source/Source_list.html'
    table_class = SourceTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = Source.objects.filter(Q(created_by__icontains=search) |Q(modify_by__icontains=search) |Q(name__icontains=search) )
        else:
            queryset = Source.objects.all()
        return queryset


class SourceCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_Source'
    model = Source
    form_class = SourceForm
    success_url = reverse_lazy('master:Source-list')
    template_name = 'master/Source/Source_form.html'

class SourceUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_Source'
    model = Source
    template_name = 'master/Source/Source_form.html'
    form_class = SourceForm
    success_url = reverse_lazy('master:Source-list')

class SourceDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_Source'
    model = Source
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:Source-list')
    
class SourceAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Source.objects.none()
        qs = Source.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

        

from .forms import SegmentGroupForm
from .tables import SegmentGroupTable
from .models import SegmentGroup
####################

class SegmentGroupList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_SegmentGroup'
    model = SegmentGroup
    template_name = 'master/segmentgroup/SegmentGroup_list.html'
    table_class = SegmentGroupTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = SegmentGroup.objects.filter(Q(created_by__icontains=search) |Q(modify_by__icontains=search) |Q(name__icontains=search) )
        else:
            queryset = SegmentGroup.objects.all()
        return queryset


class SegmentGroupCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_SegmentGroup'
    model = SegmentGroup
    form_class = SegmentGroupForm
    success_url = reverse_lazy('master:SegmentGroup-list')
    template_name = 'master/SegmentGroup/SegmentGroup_form.html'

class SegmentGroupUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_SegmentGroup'
    model = SegmentGroup
    template_name = 'master/SegmentGroup/SegmentGroup_form.html'
    form_class = SegmentGroupForm
    success_url = reverse_lazy('master:SegmentGroup-list')

class SegmentGroupDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_SegmentGroup'
    model = SegmentGroup
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:SegmentGroup-list')
    
class SegmentGroupAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return SegmentGroup.objects.none()
        qs = SegmentGroup.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

        

from .forms import SegmentForm
from .tables import SegmentTable
from .models import Segment
####################

class SegmentList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_Segment'
    model = Segment
    template_name = 'master/segment/Segment_list.html'
    table_class = SegmentTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = Segment.objects.filter(Q(created_by__icontains=search) |Q(modify_by__icontains=search) |Q(name__icontains=search) )
        else:
            queryset = Segment.objects.all()
        return queryset


class SegmentCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_Segment'
    model = Segment
    form_class = SegmentForm
    success_url = reverse_lazy('master:Segment-list')
    template_name = 'master/Segment/Segment_form.html'

class SegmentUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_Segment'
    model = Segment
    template_name = 'master/Segment/Segment_form.html'
    form_class = SegmentForm
    success_url = reverse_lazy('master:Segment-list')

class SegmentDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_Segment'
    model = Segment
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:Segment-list')
    
class SegmentAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Segment.objects.none()
        qs = Segment.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

        

from .forms import AppForm
from .tables import AppTable
from .models import App
####################


def appImport(request):
   load_apps()
   return redirect(reverse('admin:master_app_changelist'))

class AppList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_App'
    model = App
    template_name = 'master/app/App_list.html'
    table_class = AppTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = App.objects.filter(Q(name__icontains=search) )
        else:
            queryset = App.objects.all()
        return queryset


class AppCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_App'
    model = App
    form_class = AppForm
    success_url = reverse_lazy('master:App-list')
    template_name = 'master/App/App_form.html'

class AppUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_App'
    model = App
    template_name = 'master/App/App_form.html'
    form_class = AppForm
    success_url = reverse_lazy('master:App-list')

class AppDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_App'
    model = App
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:App-list')
    
class AppAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return App.objects.none()
        qs = App.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

        

from .forms import ModelForm
from .tables import ModelTable
from .models import Model
####################

class ModelList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_Model'
    model = Model
    template_name = 'master/model/Model_list.html'
    table_class = ModelTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = Model.objects.filter(Q(model__icontains=search) )
        else:
            queryset = Model.objects.all()
        return queryset


class ModelCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_Model'
    model = Model
    form_class = ModelForm
    success_url = reverse_lazy('master:Model-list')
    template_name = 'master/Model/Model_form.html'

class ModelUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_Model'
    model = Model
    template_name = 'master/Model/Model_form.html'
    form_class = ModelForm
    success_url = reverse_lazy('master:Model-list')

class ModelDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_Model'
    model = Model
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:Model-list')
    
class ModelAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Model.objects.none()
        qs = Model.objects.all()
        if self.q:
            qs = qs.filter(model__istartswith=self.q)

        return qs

        

from .forms import MenuForm
from .tables import MenuTable
from .models import Menu
####################

class MenuList(PermissionRequiredMixin,SingleTableView):
    permission_required = 'master.view_Menu'
    model = Menu
    template_name = 'master/menu/Menu_list.html'
    table_class = MenuTable
    table_pagination = False
    
    def get_queryset(self):
        search = self.request.GET.get('search',None)
        if search:
           queryset = Menu.objects.filter(Q(menu__icontains=search) |Q(url__icontains=search) )
        else:
            queryset = Menu.objects.all()
        return queryset


class MenuCreate(PermissionRequiredMixin,CreateView): #LoginRequiredMixin (para pedir el usuario)
    permission_required = 'master.add_Menu'
    model = Menu
    form_class = MenuForm
    success_url = reverse_lazy('master:Menu-list')
    template_name = 'master/Menu/Menu_form.html'

class MenuUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = 'master.change_Menu'
    model = Menu
    template_name = 'master/Menu/Menu_form.html'
    form_class = MenuForm
    success_url = reverse_lazy('master:Menu-list')

class MenuDelete(PermissionRequiredMixin,DeleteView):
    permission_required = 'master.delete_Menu'
    model = Menu
    template_name = 'master/confirm_delete.html'
    success_url = reverse_lazy('master:Menu-list')
    
class MenuAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Menu.objects.none()
        qs = Menu.objects.all()
        if self.q:
            qs = qs.filter(menu__istartswith=self.q)

        return qs

        