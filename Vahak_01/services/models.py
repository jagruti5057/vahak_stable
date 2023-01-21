from django.db import models
from account.models import User,Routes,Role
from datetime import datetime  
from django.utils.timezone import now

class Banner(models.Model):
    banner_image=models.ImageField(upload_to='banner_images',default='downloads/banners/load1.jpg',blank=True, null=True)
    
class Businesscard(models.Model):
    contact_person_name = models.CharField(max_length=30,null=False,blank=False)
    designation =models.CharField(max_length=30,null=False,blank=False)
    alternative_contact =models.CharField(max_length=30,null=True,blank=True)
    email =models.EmailField(null=True,blank=True)
    logo =models.ImageField(null=True,blank=True)
    bussiness_Address=models.TextField(null=False,blank=False)

class Vehicle(models.Model):
    vehicle_name =models.CharField(max_length=30,null=True,blank=True)
    vehicle_load_capacity=models.CharField(max_length=30,null=True,blank=True)
    vehicle_Type=models.CharField(max_length=30,null=True,blank=True)
    is_Tyres_defined=models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)

#changes in models
class Attachnewlorry(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)
    uservehicle_number=models.CharField(max_length=50,null=False,blank=False)
    current_location=models.CharField(max_length=35,null=False,blank=False)
    permit=models.ManyToManyField(Routes, related_name="permit",null=True, blank=True)
    vehicle_name =models.CharField(max_length=30,null=True,blank=True)
    vehicle_load_capacity=models.CharField(max_length=30,null=True,blank=True)
    vehicle_type=models.CharField(max_length=30,null=True,blank=True)
    vehical_tyres=models.CharField(max_length=20)
    is_all_permit=models.BooleanField(null=True,blank=True)
    is_lorry_status=models.CharField(max_length=20,default="Lorry Posted")
    enter_price=models.CharField(max_length=80,null=True,blank=True)
    is_active=models.BooleanField(null=True,blank=True,default=True)
    is_rc_verfied=models.BooleanField(null=True,blank=True,default=False)
    routes=models.ManyToManyField(Routes, blank=True, default=None,related_name='postload_routes')
    updated_date = models.DateTimeField(default=now, editable=False)
    expired_date = models.DateTimeField(blank=True, null=True)
    role = models.ManyToManyField(Role,related_name='role',blank=True)
    expired_hour=models.CharField(max_length=20,null=True,blank=True,default="")
    status_option = (
    ('active', 'active'),
    ('in_progress', 'in_progress'),
    ('in_transit', 'in_transit'),
    ('completed', 'completed'),
    ('deactive', 'deactive'),
    ('expired', 'expired'),
        )
    status = models.CharField(max_length=20, choices=status_option, default='active')


    def __str__(self):
        return self.status

    def update_status(self):
        if self.status == 'active':
            self.status = 'in_progress'
        elif self.status == 'in_progress':
            self.status = 'in_transit'
        elif self.status == 'in_transit':
            self.status = 'completed'
        elif self.status == 'completed':
            self.status = 'deactive'
        elif self.status == 'deactive':
            self.status = 'expired'
        self.save()

    def __str__(self):
        return '%s' % (self.vehicle_name)
    
class PostLoad(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)
    pickup_location=models.CharField(max_length=80)
    drop_location=models.CharField(max_length=80)
    material_name=models.CharField(max_length=70)
    quantity=models.CharField(max_length=70)
    vehicle_name =models.CharField(max_length=30,null=True,blank=True)
    vehicle_type=models.CharField(max_length=30,null=True,blank=True)
    excepted_price=models.CharField(max_length=80,null=True,blank=True)
    is_advance_pay=models.BooleanField(default=False)
    price=models.CharField(max_length=80,null=True,blank=True)
    advance_price=models.CharField(max_length=20,blank=True,null=True)
    to_pay=models.BooleanField(default=False)
    odc_consignment=models.CharField(max_length=20,null=True,blank=True)
    description=models.TextField(default=None)
    postload_date = models.DateTimeField(default=now, editable=False)
    expired_date = models.DateTimeField(default=now, editable=False)
    expired_hour=models.CharField(max_length=20,null=True,blank=True,default="")
    status_option = (
    ('active', 'active'),
    ('in_progress', 'in_progress'),
    ('in_transit', 'in_transit'),
    ('completed', 'completed'),
    ('deactive', 'deactive'),
    ('expired', 'expired'),
        )
    status = models.CharField(max_length=20, choices=status_option, default='active')
    def __str__(self):
        return self.status

    def update_status(self):
        if self.status == 'active':
            self.status = 'in_progress'
        elif self.status == 'in_progress':
            self.status = 'in_transit'
        elif self.status == 'in_transit':
            self.status = 'completed'
        elif self.status == 'completed':
            self.status = 'deactive'
        elif self.status == 'deactive':
            self.status = 'expired'
        self.save()
       
class Bid(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)
    PostLoad=models.ManyToManyField(PostLoad, related_name="postload",null=True, blank=True)
    Attachnewlorry=models.ManyToManyField(Attachnewlorry, related_name="attachlorry",null=True, blank=True)
    fixed_price=models.CharField(max_length=30,null=True,blank=True)
    comments=models.CharField(max_length=20,null=True,blank=True)
    


  
