from pyexpat import model
from attr import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView,DetailView,UpdateView,CreateView
from . models import Paint,Pvc,Sheet,Steel,Tsheets,Motar,PvcFittings,Tanks,Others,Cables,New
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q
from . import forms 
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
def PaintListView(request):
    if "q" in request.GET:
        q=request.GET['q']
        paint_list=Paint.objects.filter(Q(Item_Name__icontains=q)|Q(Description__icontains=q))
    else:
        paint_list=Paint.objects.all()
    paginator=Paginator(paint_list,8)
    page_number=request.GET.get('page')
    try:
        paint_list=paginator.page(page_number)
    except PageNotAnInteger:
        paint_list=paginator.page(1)
    except EmptyPage:
        paint_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/paint_list.html',{'paint_list':paint_list})
    
class PaintDetailView(DetailView):
    model=Paint

class PaintCreateView(CreateView):
    model=Paint
    fields=['Item_Name','Item_Image','company','volume','Price','Offered_Price','Offer','Description','status']

class PaintUpdateView(UpdateView):
    model=Paint
    fields=['Item_Name','Item_Image','company','volume','Price','Offered_Price','Offer','Description','status']

class PaintDeleteView(DeleteView):
    model=Paint
    success_url=reverse_lazy('paintlist')     

def Home_view(request):
    return render(request,'testapp/home.html')   

def signup_view(request):
    form=forms.SignUpForm()
    if request.method=='POST':
        form=forms.SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form}) 

def LogOut_View(request):
    return render(request,'testapp/logout.html')   

def PvcListView(request):
    if "q" in request.GET:
        q=request.GET['q']
        pvc_list=Pvc.objects.filter(Q(Item_Name__icontains=q)|Q(Description__icontains=q))
    else:
        pvc_list=Pvc.objects.all()
    paginator=Paginator(pvc_list,8)
    page_number=request.GET.get('page')
    try:
        pvc_list=paginator.page(page_number)
    except PageNotAnInteger:
        pvc_list=paginator.page(1)
    except EmptyPage:
        pvc_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/pvc_list.html',{'pvc_list':pvc_list})
    
class PvcDetailView(DetailView):
    model=Pvc

class PvcCreateView(CreateView):
    model=Pvc
    fields=['Item_Name','Item_Image','company','length','size','Price','Offered_Price','Offer','Description','status']

class PvcUpdateView(UpdateView):
    model=Pvc
    fields=['Item_Name','Item_Image','company','length','size','Price','Offered_Price','Offer','Description','status']

class PvcDeleteView(DeleteView):
    model=Pvc
    success_url=reverse_lazy('pvclist')          

def SheetListView(request):
    if "q" in request.GET:
        q=request.GET['q']
        sheet_list=Sheet.objects.filter(Q(Item_Name__icontains=q)|Q(Description__icontains=q))
    else:
        sheet_list=Sheet.objects.all()
    paginator=Paginator(sheet_list,8)
    page_number=request.GET.get('page')
    try:
        sheet_list=paginator.page(page_number)
    except PageNotAnInteger:
        sheet_list=paginator.page(1)
    except EmptyPage:
        sheet_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/sheet_list.html',{'sheet_list':sheet_list})
    
class SheetDetailView(DetailView):
    model=Sheet

class SheetCreateView(CreateView):
    model=Sheet
    fields=['sheet','Item_Name','Item_Image','company','colour','length','width','thickness','Price','Offered_Price','Offer','Description','status']

class SheetUpdateView(UpdateView):
    model=Sheet
    fields=['sheet','Item_Name','Item_Image','company','colour','length','width','thickness','Price','Offered_Price','Offer','Description','status']

class SheetDeleteView(DeleteView):
    model=Sheet
    success_url=reverse_lazy('sheetlist')  

def SteelListView(request):
    if "q" in request.GET:
        q=request.GET['q']
        steel_list=Steel.objects.filter(Q(Item_Name__icontains=q)|Q(Description__icontains=q))
    else:
        steel_list=Steel.objects.all()
    paginator=Paginator(steel_list,8)
    page_number=request.GET.get('page')
    try:
        steel_list=paginator.page(page_number)
    except PageNotAnInteger:
        steel_list=paginator.page(1)
    except EmptyPage:
        steel_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/steel_list.html',{'steel_list':steel_list})
    
class SteelDetailView(DetailView):
    model=Steel

class SteelCreateView(CreateView):
    model=Steel
    fields=['steel','Item_Name','Item_Image','company','size','Price','Offered_Price','Offer','Description','status']

class SteelUpdateView(UpdateView):
    model=Steel
    fields=['steel','Item_Name','Item_Image','company','size','Price','Offered_Price','Offer','Description','status']

class SteelDeleteView(DeleteView):
    model=Steel
    success_url=reverse_lazy('steellist')  

def TsheetListView(request):
    if "q" in request.GET:
        q=request.GET['q']
        tsheets_list=Tsheets.objects.filter(Q(Item_Name__icontains=q)|Q(Description__icontains=q))
    else:
        tsheets_list=Tsheets.objects.all()
    paginator=Paginator(tsheets_list,8)
    page_number=request.GET.get('page')
    try:
        tsheets_list=paginator.page(page_number)
    except PageNotAnInteger:
        tsheets_list=paginator.page(1)
    except EmptyPage:
        tsheets_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/tsheets_list.html',{'tsheets_list':tsheets_list})
    
class TsheetDetailView(DetailView):
    model=Tsheets

class TsheetCreateView(CreateView):
    model=Tsheets
    fields=['steel','Item_Name','Item_Image','size','thickness','angle_size','Price','Offered_Price','Offer','Description','status']

class TsheetUpdateView(UpdateView):
    model=Tsheets
    fields=['steel','Item_Name','Item_Image','size','thickness','angle_size','Price','Offered_Price','Offer','Description','status']

class TsheetDeleteView(DeleteView):
    model=Tsheets
    success_url=reverse_lazy('tsheetslist') 

def MotarListView(request):
    if "q" in request.GET:
        q=request.GET['q']
        motar_list=Motar.objects.filter(Q(Item_Name__icontains=q)|Q(Description__icontains=q))
    else:
        motar_list=Motar.objects.all()
    paginator=Paginator(motar_list,8)
    page_number=request.GET.get('page')
    try:
        motar_list=paginator.page(page_number)
    except PageNotAnInteger:
        motar_list=paginator.page(1)
    except EmptyPage:
        motar_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/motar_list.html',{'motar_list':motar_list})
    
class MotarDetailView(DetailView):
    model=Motar

class MotarCreateView(CreateView):
    model=Motar
    fields=['company','choose','Item_Name','Item_Image','hp','stage','Price','Offered_Price','Offer','Description','status']

class MotarUpdateView(UpdateView):
    model=Motar
    fields=['company','choose','Item_Name','Item_Image','hp','stage','Price','Offered_Price','Offer','Description','status']

class MotarDeleteView(DeleteView):
    model=Motar
    success_url=reverse_lazy('motarlist')    

def CablesListView(request):
    if "q" in request.GET:
        q=request.GET['q']
        cables_list=Cables.objects.filter(Q(Item_Name__icontains=q)|Q(Description__icontains=q))
    else:
        cables_list=Cables.objects.all()
    paginator=Paginator(cables_list,8)
    page_number=request.GET.get('page')
    try:
        cables_list=paginator.page(page_number)
    except PageNotAnInteger:
        cables_list=paginator.page(1)
    except EmptyPage:
        cables_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/cables_list.html',{'cables_list':cables_list})
    
class CablesDetailView(DetailView):
    model=Cables

class CablesCreateView(CreateView):
    model=Cables
    fields=['company','Item_Name','Item_Image','meter','thickness','Price','Offered_Price','Offer','Description','status']

class CablesUpdateView(UpdateView):
    model=Cables
    fields=['company','Item_Name','Item_Image','meter','thickness','Price','Offered_Price','Offer','Description','status']

class CablesDeleteView(DeleteView):
    model=Cables
    success_url=reverse_lazy('cableslist')    

def PvcfittingsListView(request):
    if "q" in request.GET:
        q=request.GET['q']
        pvcfittings_list=PvcFittings.objects.filter(Q(Item_Name__icontains=q)|Q(Description__icontains=q))
    else:
        pvcfittings_list=PvcFittings.objects.all()
    paginator=Paginator(pvcfittings_list,8)
    page_number=request.GET.get('page')
    try:
        pvcfittings_list=paginator.page(page_number)
    except PageNotAnInteger:
        pvcfittings_list=paginator.page(1)
    except EmptyPage:
        pvcfittings_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/pvcfittings_list.html',{'pvcfittings_list':pvcfittings_list})
    
class PvcfittingsDetailView(DetailView):
    model=PvcFittings

class PvcfittingsCreateView(CreateView):
    model=PvcFittings
    fields=['Item_Name','Item_Image','size','Price','Offered_Price','Offer','Description','status']

class PvcfittingsUpdateView(UpdateView):
    model=PvcFittings
    fields=['Item_Name','Item_Image','size','Price','Offered_Price','Offer','Description','status']

class PvcfittingsDeleteView(DeleteView):
    model=PvcFittings
    success_url=reverse_lazy('pvcfittingslist')   

def TankListView(request):
    if "q" in request.GET:
        q=request.GET['q']
        tanks_list=Tanks.objects.filter(Q(Item_Name__icontains=q)|Q(Description__icontains=q))
    else:
        tanks_list=Tanks.objects.all()
    paginator=Paginator(tanks_list,8)
    page_number=request.GET.get('page')
    try:
        tanks_list=paginator.page(page_number)
    except PageNotAnInteger:
        tanks_list=paginator.page(1)
    except EmptyPage:
        tanks_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/tanks_list.html',{'tanks_list':tanks_list})
    
class TankDetailView(DetailView):
    model=Tanks

class TankCreateView(CreateView):
    model=Tanks
    fields=['Item_Name','company','type','Item_Image','ltrs','colour','Price','Offered_Price','Offer','Description','status']

class TankUpdateView(UpdateView):
    model=Tanks
    fields=['Item_Name','company','type','Item_Image','ltrs','colour','Price','Offered_Price','Offer','Description','status']

class TankDeleteView(DeleteView):
    model=Tanks
    success_url=reverse_lazy('tankslist') 

def OthersListView(request):
    if "q" in request.GET:
        q=request.GET['q']
        others_list=Others.objects.filter(Q(Item_Name__icontains=q)|Q(Description__icontains=q))
    else:
        others_list=Others.objects.all()
    paginator=Paginator(others_list,8)
    page_number=request.GET.get('page')
    try:
        others_list=paginator.page(page_number)
    except PageNotAnInteger:
        others_list=paginator.page(1)
    except EmptyPage:
        others_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/others_list.html',{'others_list':others_list})
    
class OthersDetailView(DetailView):
    model=Others

class OthersCreateView(CreateView):
    model=Others
    fields=['Item_Name','Item_Image','Price','Offered_Price','Offer','Description','status']

class OthersUpdateView(UpdateView):
    model=Others
    fields=['Item_Name','Item_Image','Price','Offered_Price','Offer','Description','status']

class OthersDeleteView(DeleteView):
    model=Others
    success_url=reverse_lazy('otherslist')     

def NewListView(request):
    if "q" in request.GET:
        q=request.GET['q']
        new_list=New.objects.filter(Q(Item_Name__icontains=q)|Q(Description__icontains=q))
    else:
        new_list=New.objects.all()
    paginator=Paginator(new_list,8)
    page_number=request.GET.get('page')
    try:
        new_list=paginator.page(page_number)
    except PageNotAnInteger:
        new_list=paginator.page(1)
    except EmptyPage:
        new_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/new_list.html',{'new_list':new_list})
    
class NewDetailView(DetailView):
    model=New

class NewCreateView(CreateView):
    model=New
    fields=['Item_Name','company','Item_Image','Price','Offered_Price','Offer','Description','status']

class NewUpdateView(UpdateView):
    model=New
    fields=['Item_Name','company','Item_Image','Price','Offered_Price','Offer','Description','status']

class NewDeleteView(DeleteView):
    model=New
    success_url=reverse_lazy('newlist')     
