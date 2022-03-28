from atexit import register
from django.contrib import admin
from . models import Paint,Pvc,Sheet,Steel,Tsheets,Motar,PvcFittings,Tanks,Others,Cables,New

# Register your models here.
class PaintAdmin(admin.ModelAdmin):
    list_display = ['Item_Name','company','Price','Offered_Price','Offer','created','updated']
    search_fields = ('Item_Name','Description','Company')

class PvcAdmin(admin.ModelAdmin):
    list_display = ['Item_Name','company','length','Price','size','Offered_Price','Offer','created','updated']
    search_fields = ('Item_Name','Description','Company')    

class SheetAdmin(admin.ModelAdmin):
    list_display = ['Item_Name','company','length','width','thickness','colour','Price','Offered_Price','Offer','created','updated']
    search_fields = ('Item_Name','Description','Company')  

class SteelAdmin(admin.ModelAdmin):
    list_display = ['Item_Name','company','size','Price','Offered_Price','Offer','created','updated']
    search_fields = ('Item_Name','Description','Company')      

class TsheetsAdmin(admin.ModelAdmin):
    list_display = ['Item_Name','size','thickness','angle_size','Price','Offered_Price','Offer','created','updated']
    search_fields = ('Item_Name','Description','Company') 

class MotarAdmin(admin.ModelAdmin):
    list_display = ['Item_Name','company','hp','stage','feet','Price','Offered_Price','Offer','created','updated']
    search_fields = ('Item_Name','Description','Company')   

class CablesAdmin(admin.ModelAdmin):
    list_display = ['company','Item_Name','meter','thickness','Price','Offered_Price','Offer','created','updated']
    search_fields = ('Item_Name','Description','Company')   

class PvcfittingsAdmin(admin.ModelAdmin):
    list_display = ['Item_Name','size','ltrs','Price','Offered_Price','Offer','created','updated']
    search_fields = ('Item_Name','Description','Company')       

class TanksAdmin(admin.ModelAdmin):
    list_display = ['Item_Name','company','ltrs','Price','Offered_Price','Offer','created','updated']
    search_fields = ('Item_Name','Description','Company') 

class OthersAdmin(admin.ModelAdmin):
    list_display = ['Item_Name','Price','Offered_Price','Offer','created','updated']
    search_fields = ('Item_Name','Description','Company')   

class NewAdmin(admin.ModelAdmin):
    list_display = ['Item_Name','company','Price','Offered_Price','Offer','created','updated']
    search_fields = ('Item_Name','Description','Company')       

admin.site.register(Paint,PaintAdmin)
admin.site.register(Pvc,PvcAdmin)
admin.site.register(Sheet,SheetAdmin)
admin.site.register(Steel,SteelAdmin)
admin.site.register(Tsheets,TsheetsAdmin)
admin.site.register(Motar,MotarAdmin)
admin.site.register(PvcFittings,PvcfittingsAdmin)
admin.site.register(Tanks,TanksAdmin)
admin.site.register(Others,OthersAdmin)
admin.site.register(Cables,CablesAdmin)
admin.site.register(New,NewAdmin)