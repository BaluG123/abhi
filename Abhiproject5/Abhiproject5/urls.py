"""Abhiproject5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from operator import ne
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from testapp.views import CablesCreateView, CablesDeleteView, CablesDetailView, CablesListView, CablesUpdateView, PaintDetailView,PaintListView,PaintCreateView,Home_view,signup_view,PaintUpdateView,PaintDeleteView,LogOut_View,PvcCreateView,PvcDeleteView,PvcDetailView,PvcUpdateView,PvcListView,SheetListView,SheetDetailView,SheetCreateView,SheetUpdateView,SheetDeleteView,SteelListView,SteelDetailView,SteelCreateView,SteelDeleteView,SteelUpdateView,TsheetListView,TsheetDetailView,TsheetCreateView,TsheetDeleteView,TsheetUpdateView,MotarListView,MotarDetailView,MotarCreateView,MotarUpdateView,MotarDeleteView,PvcfittingsListView,PvcfittingsDetailView,PvcfittingsCreateView,PvcfittingsDeleteView,PvcfittingsUpdateView,TankListView,TankDetailView,TankCreateView,TankDeleteView,TankUpdateView,OthersListView,OthersDetailView,OthersCreateView,OthersDeleteView,OthersUpdateView,NewListView,NewDetailView,NewCreateView,NewDeleteView,NewUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sbba/',Home_view,name="home"),
    path('paints/',PaintListView,name="paintlist"),
    path('p/<int:pk>',PaintDetailView.as_view(),name="paint_item_detail"),
    path('create/',PaintCreateView.as_view(),name="paint_create"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('signup/',signup_view,name="signup"),
    path('update/<int:pk>',PaintUpdateView.as_view(),name="pupdate"),
    path('delete/<int:pk>',PaintDeleteView.as_view(),name="delete"),
    path('logout/',LogOut_View,name="logout"),
    path('pvcs/',PvcListView,name="pvclist"),
    path('pvc/<int:pk>',PvcDetailView.as_view(),name="pvc_item_detail"),
    path('pvccreate/',PvcCreateView.as_view(),name="pvc_create"),
    path('pvcupdate/<int:pk>',PvcUpdateView.as_view(),name="pvc_update"),
    path('pvcdelete/<int:pk>',PvcDeleteView.as_view(),name="pvc_delete"),
    path('sheets/',SheetListView,name="sheetlist"),
    path('sheet/<int:pk>',SheetDetailView.as_view(),name="sheet_item_detail"),
    path('sheetcreate/',SheetCreateView.as_view(),name="sheet_create"),
    path('sheetupdate/<int:pk>',SheetUpdateView.as_view(),name="sheet_update"),
    path('sheetdelete/<int:pk>',SheetDeleteView.as_view(),name="sheet_delete"),
    path('steels/',SteelListView,name="steellist"),
    path('steelcreate/',SteelCreateView.as_view(),name="steel_item_detail"),
    path('steel/<int:pk>',SteelDetailView.as_view(),name="steel_create"),
    path('steelupdate/<int:pk>',SteelUpdateView.as_view(),name="steel_update"),
    path('steeldelete/<int:pk>',SteelDeleteView.as_view(),name="steel_delete"),
    path('tsheets/',TsheetListView,name="tsheetslist"),
    path('tsheet/<int:pk>',TsheetDetailView.as_view(),name="tsheets_item_detail"),
    path('tsheetcreate/',TsheetCreateView.as_view(),name="tsheet_create"),
    path('tsheetupdate/<int:pk>',TsheetUpdateView.as_view(),name="tsheet_update"),
    path('tsheetdelete/<int:pk>',TsheetDeleteView.as_view(),name="tsheet_delete"),
    path('motars/',MotarListView,name="motarlist"),
    path('motar/<int:pk>',MotarDetailView.as_view(),name="motar_item_detail"),
    path('motarcreate/',MotarCreateView.as_view(),name="motar_create"),
    path('motarupdate/<int:pk>',MotarUpdateView.as_view(),name="motar_update"),
    path('motardelete/<int:pk>',MotarDeleteView.as_view(),name="motar_delete"),
    path('cables/',CablesListView,name="cableslist"),
    path('cable/<int:pk>',CablesDetailView.as_view(),name="cable_item_detail"),
    path('cablecreate/',CablesCreateView.as_view(),name="cable_create"),
    path('cableupdate/<int:pk>',CablesUpdateView.as_view(),name="cable_update"),
    path('cabledelete/<int:pk>',CablesDeleteView.as_view(),name="cable_delete"),
    path('pvcfittings/',PvcfittingsListView,name="pvcfittingslist"),
    path('pvcf/<int:pk>',PvcfittingsDetailView.as_view(),name="pvcfittings_item_detail"),
    path('pvcfcreate/',PvcfittingsCreateView.as_view(),name="pvcfittings_create"),
    path('pvcfupdate/<int:pk>',PvcfittingsUpdateView.as_view(),name="pvcfittings_update"),
    path('pvcfdelete/<int:pk>',PvcfittingsDeleteView.as_view(),name="pvcfittings_delete"),
    path('tanks/',TankListView,name="tankslist"),
    path('tank/<int:pk>',TankDetailView.as_view(),name="tank_detail"),
    path('tankcreate/',TankCreateView.as_view(),name="tank_create"),
    path('tankupdate/<int:pk>',TankUpdateView.as_view(),name="tank_update"),
    path('tankdelete/<int:pk>',TankDeleteView.as_view(),name="tank_delete"),
    path('others/',OthersListView,name="otherslist"),
    path('other/<int:pk>',OthersDetailView.as_view(),name="other_detail"),
    path('othercreate/',OthersCreateView.as_view(),name="other_create"),
    path('otherupdate/<int:pk>',OthersUpdateView.as_view(),name="other_update"),
    path('otherdelete/<int:pk>',OthersDeleteView.as_view(),name="other_delete"),
    path('news/',NewListView,name="newlist"),
    path('new/<int:pk>',NewDetailView.as_view(),name="new_item_detail"),
    path('newcreate/',NewCreateView.as_view(),name="new_create"),
    path('newupdate/<int:pk>',NewUpdateView.as_view(),name="new_update"),
    path('newdelete/<int:pk>',NewDeleteView.as_view(),name="new_delete")
    


    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)