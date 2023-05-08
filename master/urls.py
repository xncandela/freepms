"""freepms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

urlpatterns = []
from master.views import RegionList,RegionCreate,RegionDelete,RegionUpdate, RegionAutocomplete## region
urlpatterns += [
    path('region/', RegionList.as_view(), name='Region-list'),
    path('region/add/', RegionCreate.as_view(), name='Region-add'),
    path('region/<pk>/', RegionUpdate.as_view(), name='Region-update'),
    path('region/<pk>/delete/', RegionDelete.as_view(), name='Region-delete'),
    path('region-autocomplete/',RegionAutocomplete.as_view(),name='Region-autocomplete'),
]

from master.views import CountryList,CountryCreate,CountryDelete,CountryUpdate,CountryAutocomplete ## country
urlpatterns += [
    path('country/', CountryList.as_view(), name='Country-list'),
    path('country/add/', CountryCreate.as_view(), name='Country-add'),
    path('country/<pk>/', CountryUpdate.as_view(), name='Country-update'),
    path('country/<pk>/delete/', CountryDelete.as_view(), name='Country-delete'),
    path('country-autocomplete/',CountryAutocomplete.as_view(),name='Country-autocomplete'),
]

from master.views import CurrencyList,CurrencyCreate,CurrencyDelete,CurrencyUpdate## Currency
urlpatterns += [
    path('currency/', CurrencyList.as_view(), name='Currency-list'),
    path('currency/add/', CurrencyCreate.as_view(), name='Currency-add'),
    path('currency/<pk>/', CurrencyUpdate.as_view(), name='Currency-update'),
    path('currency/<pk>/delete/', CurrencyDelete.as_view(), name='Currency-delete'),
]

from master.views import CompanyGroupList,CompanyGroupCreate,CompanyGroupDelete,CompanyGroupUpdate

## CompanyGroup
urlpatterns += [
    path('companygroup/', CompanyGroupList.as_view(), name='CompanyGroup-list'),
    path('companygroup/add/', CompanyGroupCreate.as_view(), name='CompanyGroup-add'),
    path('companygroup/<pk>/', CompanyGroupUpdate.as_view(), name='CompanyGroup-update'),
    path('companygroup/<pk>/delete/', CompanyGroupDelete.as_view(), name='CompanyGroup-delete'),
]

from master.views import BrandList,BrandCreate,BrandDelete,BrandUpdate

        ## Brand
urlpatterns += [
    path('brand/', BrandList.as_view(), name='Brand-list'),
    path('brand/add/', BrandCreate.as_view(), name='Brand-add'),
    path('brand/<pk>/', BrandUpdate.as_view(), name='Brand-update'),
    path('brand/<pk>/delete/', BrandDelete.as_view(), name='Brand-delete'),
]

from master.views import CompanyList,CompanyCreate,CompanyDelete,CompanyUpdate

## Company
urlpatterns += [
    path('company/', CompanyList.as_view(), name='Company-list'),
    path('company/add/', CompanyCreate.as_view(), name='Company-add'),
    path('company/<int:pk>/', CompanyUpdate.as_view(), name='Company-update'),
    path('company/<int:pk>/delete/', CompanyDelete.as_view(), name='Company-delete'),
]


from master.views import HotelComplexList,HotelComplexCreate,HotelComplexDelete,HotelComplexUpdate
## HotelComplex
urlpatterns += [
    path('hotelcomplex/', HotelComplexList.as_view(), name='HotelComplex-list'),
    path('hotelcomplex/add/', HotelComplexCreate.as_view(), name='HotelComplex-add'),
    path('hotelcomplex/<int:pk>/', HotelComplexUpdate.as_view(), name='HotelComplex-update'),
    path('hotelcomplex/<int:pk>/delete/', HotelComplexDelete.as_view(), name='HotelComplex-delete'),
]

from master.views import HotelList,HotelCreate,HotelDelete,HotelUpdate
## Hotel
urlpatterns += [
    path('hotel/', HotelList.as_view(), name='Hotel-list'),
    path('hotel/add/', HotelCreate.as_view(), name='Hotel-add'),
    path('hotel/<int:pk>/', HotelUpdate.as_view(), name='Hotel-update'),
    path('hotel/<int:pk>/delete/', HotelDelete.as_view(), name='Hotel-delete'),
]


from master.views import ProductionGroupList,ProductionGroupCreate,ProductionGroupDelete,ProductionGroupUpdate
## ProductionGroup
urlpatterns += [
    path('productiongroup/', ProductionGroupList.as_view(), name='ProductionGroup-list'),
    path('productiongroup/add/', ProductionGroupCreate.as_view(), name='ProductionGroup-add'),
    path('productiongroup/<int:pk>/', ProductionGroupUpdate.as_view(), name='ProductionGroup-update'),
    path('productiongroup/<int:pk>/delete/', ProductionGroupDelete.as_view(), name='ProductionGroup-delete'),
]
    
        
from master.views import ProductionCenterList,ProductionCenterCreate,ProductionCenterDelete,ProductionCenterUpdate
## ProductionCenter
urlpatterns += [
    path('productioncenter/', ProductionCenterList.as_view(), name='ProductionCenter-list'),
    path('productioncenter/add/', ProductionCenterCreate.as_view(), name='ProductionCenter-add'),
    path('productioncenter/<int:pk>/', ProductionCenterUpdate.as_view(), name='ProductionCenter-update'),
    path('productioncenter/<int:pk>/delete/', ProductionCenterDelete.as_view(), name='ProductionCenter-delete'),
]
    
        
from master.views import PruebaList,PruebaCreate,PruebaDelete,PruebaUpdate
## Prueba
urlpatterns += [
    path('prueba/', PruebaList.as_view(), name='Prueba-list'),
    path('prueba/add/', PruebaCreate.as_view(), name='Prueba-add'),
    path('prueba/<int:pk>/', PruebaUpdate.as_view(), name='Prueba-update'),
    path('prueba/<int:pk>/delete/', PruebaDelete.as_view(), name='Prueba-delete'),
]
    
        
from master.views import RoomClasificationList,RoomClasificationCreate,RoomClasificationDelete,RoomClasificationUpdate
## RoomClasification
urlpatterns += [
    path('roomclasification/', RoomClasificationList.as_view(), name='RoomClasification-list'),
    path('roomclasification/add/', RoomClasificationCreate.as_view(), name='RoomClasification-add'),
    path('roomclasification/<int:pk>/', RoomClasificationUpdate.as_view(), name='RoomClasification-update'),
    path('roomclasification/<int:pk>/delete/', RoomClasificationDelete.as_view(), name='RoomClasification-delete'),
]
    
        
from master.views import RoomTypeList,RoomTypeCreate,RoomTypeDelete,RoomTypeUpdate
## RoomType
urlpatterns += [
    path('roomtype/', RoomTypeList.as_view(), name='RoomType-list'),
    path('roomtype/add/', RoomTypeCreate.as_view(), name='RoomType-add'),
    path('roomtype/<int:pk>/', RoomTypeUpdate.as_view(), name='RoomType-update'),
    path('roomtype/<int:pk>/delete/', RoomTypeDelete.as_view(), name='RoomType-delete'),
]
    
        
from master.views import TaxList,TaxCreate,TaxDelete,TaxUpdate,TaxAutocomplete
## Tax
urlpatterns += [
    path('tax/', TaxList.as_view(), name='Tax-list'),
    path('tax/add/', TaxCreate.as_view(), name='Tax-add'),
    path('tax/<int:pk>/', TaxUpdate.as_view(), name='Tax-update'),
    path('tax/<int:pk>/delete/', TaxDelete.as_view(), name='Tax-delete'),
    path('tax-autocomplete/',TaxAutocomplete.as_view(),name='tax-autocomplete'),
]
    
        
from master.views import SourceGroupList,SourceGroupCreate,SourceGroupDelete,SourceGroupUpdate,SourceGroupAutocomplete
## SourceGroup
urlpatterns += [
    path('sourcegroup/', SourceGroupList.as_view(), name='SourceGroup-list'),
    path('sourcegroup/add/', SourceGroupCreate.as_view(), name='SourceGroup-add'),
    path('sourcegroup/<int:pk>/', SourceGroupUpdate.as_view(), name='SourceGroup-update'),
    path('sourcegroup/<int:pk>/delete/', SourceGroupDelete.as_view(), name='SourceGroup-delete'),
    path('sourcegroup-autocomplete/',SourceGroupAutocomplete.as_view(),name='sourcegroup-autocomplete'),
]
    
        
from master.views import SourceList,SourceCreate,SourceDelete,SourceUpdate,SourceAutocomplete
## Source
urlpatterns += [
    path('source/', SourceList.as_view(), name='Source-list'),
    path('source/add/', SourceCreate.as_view(), name='Source-add'),
    path('source/<int:pk>/', SourceUpdate.as_view(), name='Source-update'),
    path('source/<int:pk>/delete/', SourceDelete.as_view(), name='Source-delete'),
    path('source-autocomplete/',SourceAutocomplete.as_view(),name='source-autocomplete'),
]
    
        
from master.views import SegmentGroupList,SegmentGroupCreate,SegmentGroupDelete,SegmentGroupUpdate,SegmentGroupAutocomplete
## SegmentGroup
urlpatterns += [
    path('segmentgroup/', SegmentGroupList.as_view(), name='SegmentGroup-list'),
    path('segmentgroup/add/', SegmentGroupCreate.as_view(), name='SegmentGroup-add'),
    path('segmentgroup/<int:pk>/', SegmentGroupUpdate.as_view(), name='SegmentGroup-update'),
    path('segmentgroup/<int:pk>/delete/', SegmentGroupDelete.as_view(), name='SegmentGroup-delete'),
    path('segmentgroup-autocomplete/',SegmentGroupAutocomplete.as_view(),name='segmentgroup-autocomplete'),
]
    
        
from master.views import SegmentList,SegmentCreate,SegmentDelete,SegmentUpdate,SegmentAutocomplete
## Segment
urlpatterns += [
    path('segment/', SegmentList.as_view(), name='Segment-list'),
    path('segment/add/', SegmentCreate.as_view(), name='Segment-add'),
    path('segment/<int:pk>/', SegmentUpdate.as_view(), name='Segment-update'),
    path('segment/<int:pk>/delete/', SegmentDelete.as_view(), name='Segment-delete'),
    path('segment-autocomplete/',SegmentAutocomplete.as_view(),name='segment-autocomplete'),
]
    
        
from master.views import AppList,AppCreate,AppDelete,AppUpdate,AppAutocomplete,appImport
## App
urlpatterns += [
    path('app/', AppList.as_view(), name='App-list'),
    path('app/add/', AppCreate.as_view(), name='App-add'),
    path('app/<int:pk>/', AppUpdate.as_view(), name='App-update'),
    path('app/<int:pk>/delete/', AppDelete.as_view(), name='App-delete'),
    path('app-autocomplete/',AppAutocomplete.as_view(),name='app-autocomplete'),
    path('app-import/',appImport,name='app-import')
]
    
        
from master.views import ModelList,ModelCreate,ModelDelete,ModelUpdate,ModelAutocomplete
## Model
urlpatterns += [
    path('model/', ModelList.as_view(), name='Model-list'),
    path('model/add/', ModelCreate.as_view(), name='Model-add'),
    path('model/<int:pk>/', ModelUpdate.as_view(), name='Model-update'),
    path('model/<int:pk>/delete/', ModelDelete.as_view(), name='Model-delete'),
    path('model-autocomplete/',ModelAutocomplete.as_view(),name='model-autocomplete'),
]
    
        
from master.views import MenuList,MenuCreate,MenuDelete,MenuUpdate,MenuAutocomplete
## Menu
urlpatterns += [
    path('menu/', MenuList.as_view(), name='Menu-list'),
    path('menu/add/', MenuCreate.as_view(), name='Menu-add'),
    path('menu/<int:pk>/', MenuUpdate.as_view(), name='Menu-update'),
    path('menu/<int:pk>/delete/', MenuDelete.as_view(), name='Menu-delete'),
    path('menu-autocomplete/',MenuAutocomplete.as_view(),name='menu-autocomplete'),
]
    
        