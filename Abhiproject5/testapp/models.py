from django.db import models
from django.urls import reverse

# Create your models here.
class Paint(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('post','Post'))
    COMPANY_CHOICES = (('asianPaints','asianpaints'),('indigo paints','INDIGO Paints'),('agsar paints','Agsar Paints'),('mrf Paints','MRF Paints'),('berger paints','Berger Paints'),('birla paints','Birla Paints'))
    Item_Name=models.CharField(max_length=1000)
    Item_Image=models.FileField(null=True,blank=True,upload_to='paints/')
    company=models.CharField(max_length=15,choices=COMPANY_CHOICES)
    volume=models.CharField(max_length=150)
    Price=models.IntegerField()
    Offered_Price=models.IntegerField()
    Offer=models.IntegerField()
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    Description=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='post')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.Item_Name

    def get_absolute_url(self):
        return reverse('paintlist')

class Pvc(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('post','Post'))
    COMPANY_CHOICES = (('supreme','Supreme'),('a1 plast','A1 PLAST'),('spectra','Spectra'),('mahesh','Mahesh'),('others','Others'))
    Item_Name=models.CharField(max_length=1000)
    Item_Image=models.FileField(null=True,blank=True,upload_to='pvcs/')
    company=models.CharField(max_length=15,choices=COMPANY_CHOICES)
    length=models.CharField(max_length=150)
    size=models.CharField(max_length=150)
    Price=models.IntegerField()
    Offered_Price=models.IntegerField()
    Offer=models.IntegerField()
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    Description=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='post')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.Item_Name

    def get_absolute_url(self):
        return reverse('pvclist')     

class Sheet(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('post','Post'))
    SHEET_CHOICES=(('asper','Asper'),('gc','GC'),('colourcoated','Colour Coated'),('fibre','Fibre'))
    COMPANY_CHOICES=(('ramco','Ramco'),('jsw','JSW'),('uttam','Uttam'),('amns','AMNS'),('jindal','Jindal'),('kamdenu','Kamdenu'),('charminar','Charminar')) 
    COLOUR_CHOICES=(('gray','Gray'),('silver','Silver'),('skyblue','SkyBlue'),('brickred','Brick red'),('green','Green'),('yellow','Yellow'),('red','Red'),('transparent','TransParent'))
    sheet=models.CharField(max_length=20,choices=SHEET_CHOICES)
    Item_Name=models.CharField(max_length=1000)
    Item_Image=models.FileField(null=True,blank=True,upload_to='sheets/')
    company=models.CharField(max_length=15,choices=COMPANY_CHOICES)
    colour=models.CharField(max_length=15,choices=COLOUR_CHOICES)
    length=models.CharField(max_length=150)
    width=models.CharField(max_length=150)
    thickness=models.CharField(max_length=150)
    Price=models.IntegerField()
    Offered_Price=models.IntegerField()
    Offer=models.IntegerField()
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    Description=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='post')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.Item_Name

    def get_absolute_url(self):
        return reverse('sheetlist')        

class Steel(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('post','Post'))
    STEEL_CHOICES = (('tmt','TMT'),('tube','Tube'),('plain sheet','Plain Sheet'))
    COMPANY_CHOICES = (('sk','SK'),('tata','TATA'),('indus','Indus'),('kamdenu','Kamdenu'),('a1gold','A1 Gold'),('jindal','Jindal'),('jsw','JSW'))
    steel=models.CharField(max_length=15,choices=STEEL_CHOICES)
    Item_Name=models.CharField(max_length=1000)
    Item_Image=models.FileField(null=True,blank=True,upload_to='sheets/')
    company=models.CharField(max_length=15,choices=COMPANY_CHOICES)
    size=models.CharField(max_length=150)
    Price=models.IntegerField()
    Offered_Price=models.IntegerField()
    Offer=models.IntegerField()
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    Description=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='post')

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.Item_Name

    def get_absolute_url(self):
        return reverse('steellist')
        
class Tsheets(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('post','Post'))
    STEEL_CHOICES = (('flat','FLAT'),('angle','ANGLE'),('channel','CHANNEL'))
    steel=models.CharField(max_length=10,choices=STEEL_CHOICES)
    Item_Name=models.CharField(max_length=1000)
    Item_Image=models.FileField(null=True,blank=True,upload_to='tsheets/')
    size=models.CharField(max_length=100)
    thickness=models.CharField(max_length=100)
    angle_size=models.CharField(max_length=100)
    Price=models.IntegerField()
    Offered_Price=models.IntegerField()
    Offer=models.IntegerField()
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    Description=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='post')

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.Item_Name

    def get_absolute_url(self):
        return reverse('tsheetslist')     

class Motar(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('post','Post'))
    COMPANY_CHOICES = (('kirloskar','Kirloskar'),('slv','SLV'),('ashirvad','Ashirvad'),('vguard','V-Guard'),('sharpplus','Sharp Plus'),('mascot','Mascot'))
    CHOICE=(('inwater','In Water'),('outsidewater','OutSide Water'))
    company=models.CharField(max_length=16,choices=COMPANY_CHOICES)
    choose=models.CharField(max_length=15,choices=CHOICE)
    Item_Name=models.CharField(max_length=1000)
    Item_Image=models.FileField(null=True,blank=True,upload_to='motars/')
    hp=models.CharField(max_length=150)
    stage=models.CharField(max_length=150)
    feet=models.CharField(max_length=150)
    Price=models.IntegerField()
    Offered_Price=models.IntegerField()
    Offer=models.IntegerField()
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    Description=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='post')

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.Item_Name

    def get_absolute_url(self):
        return reverse('motarlist')     

class Cables(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('post','Post'))
    COMPANY_CHOICES = (('finolex','Finolex'),('sudhakar','Sudhakar'),('meco','Meco'),('lt','LT'),('lk','LK'),('mascot','Mascot'))
    company=models.CharField(max_length=16,choices=COMPANY_CHOICES)
    Item_Name=models.CharField(max_length=1000)
    Item_Image=models.FileField(null=True,blank=True,upload_to='cables/')
    meter=models.CharField(max_length=150)
    thickness=models.CharField(max_length=150)
    Price=models.IntegerField()
    Offered_Price=models.IntegerField()
    Offer=models.IntegerField()
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    Description=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='post')

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.Item_Name

    def get_absolute_url(self):
        return reverse('cableslist')      

class PvcFittings(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('post','Post'))
    Item_Name=models.CharField(max_length=1000)
    Item_Image=models.FileField(null=True,blank=True,upload_to='pvcfittings/')
    size=models.CharField(max_length=150)
    ltrs=models.CharField(max_length=10)
    Price=models.IntegerField()
    Offered_Price=models.IntegerField()
    Offer=models.IntegerField()
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    Description=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='post')

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.Item_Name

    def get_absolute_url(self):
        return reverse('pvcfittingslist') 

class Tanks(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('post','Post'))
    COMPANY_CHOICES = (('supreme','Supreme'),('ashirvad','Ashirvad'),('hitank','Hitank'),('ganga','Ganga'),('premium plus','Premium Plus'),('kaveri','Kaveri'),('prestige','Prestige'),('vastuganga','Vastuganga'))
    TYPE_CHOICES = (('roto mold','Roto Mold'),('blow mold','Blow Mold'))
    company=models.CharField(max_length=15,choices=COMPANY_CHOICES)
    type=models.CharField(max_length=15,choices=TYPE_CHOICES)
    Item_Name=models.CharField(max_length=1000)
    Item_Image=models.FileField(null=True,blank=True,upload_to='tanks/')
    ltrs=models.CharField(max_length=100)
    colour=models.CharField(max_length=20)
    Price=models.IntegerField()
    Offered_Price=models.IntegerField()
    Offer=models.IntegerField()
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    Description=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='post')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.Item_Name

    def get_absolute_url(self):
        return reverse('tankslist')               

class Others(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('post','Post'))
    Item_Name=models.CharField(max_length=1000)
    Item_Image=models.FileField(null=True,blank=True,upload_to='others/')
    Price=models.IntegerField()
    Offered_Price=models.IntegerField()
    Offer=models.IntegerField()
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    Description=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='post')

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.Item_Name

    def get_absolute_url(self):
        return reverse('otherslist')         

class New(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('post','Post'))
    CHOICES=(('paint','Paint'),('pvc','Pvc'),('steel','Steel'),('sheet','Sheet'),('flat','Flat'),('angle','Angle'),('motar','Motar'),('cables','Cables'),('pvcfittings','Pvcfittings'),('tanks','Tanks'),('others','Others'),('channel','Channel')) 
    Item_type=models.CharField(max_length=20,choices=CHOICES)
    Item_Name=models.CharField(max_length=2000)
    Item_Image=models.FileField(null=True,blank=True,upload_to='new/')
    company=models.CharField(max_length=100,null=True,blank=True)
    Price=models.IntegerField()
    Offered_Price=models.IntegerField()
    Offer=models.IntegerField()
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    Description=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='post')

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.Item_Name

    def get_absolute_url(self):
        return reverse('newlist')









    















    




