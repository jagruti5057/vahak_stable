from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator


#user Roles
class Role(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.id)

class Routes(models.Model):
    name=models.CharField(max_length=50, blank=True)

class HelpSupport(models.Model):
    qa_data=models.TextField(default=None)

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, is_staff=False, is_active=True, is_admin=False):
        if not phone:
            raise ValueError('users must have a phone number')
        if not password:
            raise ValueError('user must have a password')
        user_obj = self.model(
            phone=phone
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, phone, password=None):
        user = self.create_user(
            phone,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, phone, password=None):
        user = self.create_user(
            phone,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        return user 
    
class User(AbstractBaseUser):
    phone_number =  models.IntegerField(null=True,blank=True)
    email=models.EmailField(max_length=40,)
    otp = models.CharField(max_length = 9, blank = True, null= True)
    count = models.IntegerField(default = 0, help_text = 'Number of otp sent')
    validated = models.BooleanField(default=False, help_text="if it is true, that means user have validate otp correctly in second API")
    name = models.CharField(max_length = 20, blank = True, null = True)
    city=models.CharField(max_length=60,blank=True,null=True)
    role = models.ManyToManyField(Role,related_name='user_role',blank=True)
    referral_code=models.CharField(max_length=20,blank=True,null=True)
    company_start_date= models.PositiveSmallIntegerField(
        blank=True, null=True,help_text="Starting year of company"
        )
    company_bio=models.TextField()
    routes=models.ManyToManyField(Routes, blank=True, default=None,related_name='user_routes')
    profile_image=models.ImageField(upload_to='profile_images',default='downloads/default_profile_image.jpeg',blank=True, null=True)
    cover_image=models.ImageField(upload_to='cover_images',default='downloads/default-cover.png',blank=True)
    view_count = models.IntegerField(default=0)
    is_user_verified=models.BooleanField(
        max_length=20,default=False,help_text="Aadhar and gst verified user"
        )
    is_bank_verified=models.BooleanField(
        max_length=20,default=False,help_text="User Added his account details"
        )
    is_aadhaar_verified=models.BooleanField(
        max_length=20,default=False,help_text="User kyc,using adhaar"
        )
    is_gst_verified=models.BooleanField(
        max_length=20,default=False,help_text="User kyc,using gst"
        )
    is_bussiness_card=models.BooleanField(
        max_length=20,default=False,help_text="User created business card"
        )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, null=False)
    updated_date = models.DateTimeField(auto_now=True, null=False)
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    def __str__(self):
        return str(self.id)

    def get_full_name(self):
        if self.name:
            return self.name
        else:    
            return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active
   
class OfficeAddress(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)
    building_number=models.CharField(max_length=20)
    area=models.CharField(max_length=20)
    landmark=models.CharField(max_length=20,null=True,blank=True)
    city=models.CharField(max_length=20)
    pincode=models.CharField(max_length=20)
