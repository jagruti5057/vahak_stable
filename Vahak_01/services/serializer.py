from rest_framework import serializers
from .models import Businesscard,Attachnewlorry,PostLoad,Bid,Banner
from account.serializer import RoutesSerializer,RoutesviewsSerializer,RoleSerializer,OfficeAddressSerializer
from account.models import Routes,User,Role,OfficeAddress
from account.helpers import updateuserfields
from datetime import datetime,timedelta
from datetime import date
import pandas as pd
import pytz

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields=['id','banner_image']
        
class Businesscardserializer(serializers.ModelSerializer):
    class Meta:
        model  = Businesscard
        fields = '__all__'

class Attachnewlorryserializer(serializers.ModelSerializer):
   
    class Meta:
        model=Attachnewlorry
        fields=['id','uservehicle_number', 'current_location', 'is_all_permit', 'is_active', 'is_rc_verfied', 'vehical_tyres', 'vehicle_type', 'vehicle_load_capacity', 'vehicle_name','permit']
        read_only_fields=('id','name')
        
class GetAttachnewlorryserializer(serializers.ModelSerializer):
    permit=RoutesSerializer(many=True,read_only=True)   
    username=serializers.SerializerMethodField()  
    profile_image =serializers.ImageField(source="user.profile_image")
    def get_username(self,user,*args):
            obj = User.objects.get(pk=user.id)
            print(obj.name)
            return obj.name
    class Meta:
        model=Attachnewlorry
        fields=['id','username','profile_image','uservehicle_number', 'current_location', 'is_all_permit', 'is_active', 'is_rc_verfied', 'user','vehical_tyres', 'vehicle_type', 'vehicle_load_capacity', 'vehicle_name','permit']
        read_only_fields=('id','name')

class PostModelSerializer(serializers.ModelSerializer):
    username=serializers.SerializerMethodField() 
    profile_image =serializers.ImageField(source="user.profile_image")

    def get_username(self,user,*args):
            obj = User.objects.get(pk=user.id)
            print(obj.name)
            return obj.name
    class Meta:
        model=PostLoad
        fields=['id','username','profile_image','pickup_location','drop_location','vehicle_name','vehicle_type','material_name','quantity','excepted_price','odc_consignment','description','user_id',]

class viwesprofileSerializer(serializers.ModelSerializer):
    routes = RoutesSerializer(read_only=True, many=True)
    officeaddress = serializers.SerializerMethodField()  
    services=serializers.SerializerMethodField()
    postload=serializers.SerializerMethodField()
    vehicle_name=serializers.SerializerMethodField()
    created_date=serializers.SerializerMethodField()

    def get_officeaddress(self,*args):
        get_user_id=args[0]
        officeaddress_data=OfficeAddress.objects.filter(user=get_user_id)
        li=[]
        for officeaddress in officeaddress_data:
            response={
                'building_number':officeaddress.building_number,
                'area':officeaddress.area,
                'landmark':officeaddress.landmark,
                'city':officeaddress.city,
                'pincode':officeaddress.pincode,    
            }
            li.append(response)
        return li
    def get_services(self,*args):
        get_user_id=args[0]
        service=[]
        user_obj=User.objects.get(id=str(get_user_id))
        roles=user_obj.role.all()
        for i in roles:
            role=Role.objects.get(id=i.id)
            service.append(role.name)
        return service  

    def get_postload(self,*args):
        get_user_id=args[0]
        postload_data=PostLoad.objects.filter(user=get_user_id).count()
        return postload_data

    def get_vehicle_name(self,*args):
        get_user_id=args[0]
        vehicle_data=Attachnewlorry.objects.filter(user=get_user_id)
        vehicle=[]
        for i in vehicle_data:
            vehicle.append(i.vehicle_name)
        return vehicle
    
    def get_created_date(self, obj):
        since=obj.created_date.strftime("%Y-%m-%d %H:%M:%S")
        sinceyear=int(since[0:4])
        sincemonth=int(since[5:7])
        today = date.today()
        today=str(today)
        curruentyear=int(today[0:4])
        curruentmonth=int(today[5:7])
        year=curruentyear-sinceyear
        if (year==0):
            months=curruentmonth-sincemonth 
            return months
        else:
            return year

    class Meta:
        model = User
        fields = ('profile_image', 'cover_image', 'city', 'name','routes','officeaddress','postload','services','vehicle_name','phone_number','created_date')

class viwescoverphotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','profile_image', 'cover_image')

class loadlistingSerializer(serializers.ModelSerializer):
    postload_date=serializers.SerializerMethodField()
    expired_date=serializers.SerializerMethodField()

    def get_postload_date(self, instance):
        global since2
        since=instance.postload_date.strftime("%Y-%m-%d %I:%M %p")
        s_date=instance.postload_date.strftime("%Y-%m-%d ")
        timezone= pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz=timezone ).strftime("%Y-%m-%d %I:%M %p")
        expired_time = ((pd.to_datetime(now))-(pd.to_datetime(since)))
        expired_time=str(expired_time)
        pl_time=since[11:16] #postload time using slicing
        total_daysfrom_pl=expired_time[0:2]
        if (int(total_daysfrom_pl) <= 2  ):  

            timeset=expired_time[7:12]
            timeset_f_min = timeset
            th_set=timeset_f_min[0:2]#time hour
            th_set=int(th_set)
            tm_set=timeset_f_min[4:7]
            tm_set=int(tm_set)
            t_set =((th_set*60)+tm_set)/60
            total_daysfrom_pl= int(total_daysfrom_pl)
            req_time= (((total_daysfrom_pl*24)+t_set))
            if (req_time < 48):
                rem_time = req_time
                e=PostLoad.objects.get(pk=instance.id)
                e.expired_hour=int(168-req_time)
                e.save()    
            if (req_time > 48) :
                change_status= PostLoad.objects.get(pk=instance.id)
                print (change_status)
                change_status.status = "Expired"
                change_status.expired_hour=0
                print (change_status)
                change_status.save()  
            since2=s_date
            return (since) 
        else:
            change_status= PostLoad.objects.get(pk=instance.id)
            print (change_status)
            change_status.status = "Expired"
            change_status.expired_hour = 0
            print (change_status)
            change_status.save()  
            since2=s_date
            return (since)


    def get_expired_date(self, obj):
        enddate = (pd.to_datetime(since2) + pd.DateOffset(days=2)).strftime("%Y-%m-%d ")
        return(enddate)

    class Meta:
        model = PostLoad
        fields = ('id','pickup_location', 'drop_location','quantity','vehicle_name','to_pay','excepted_price','postload_date','material_name','expired_date','status','expired_hour')

class Lorrylistingserializer(serializers.ModelSerializer):
    routes = RoutesviewsSerializer(read_only=True, many=True)
    updated_date=serializers.SerializerMethodField()
    
    def get_updated_date(self, instance):
        since=instance.updated_date.strftime("%Y-%m-%d %I:%M %p") 
        since_date=instance.updated_date.strftime("%Y-%m-%d ")#postload date
        timezone= pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz=timezone ).strftime("%Y-%m-%d %I:%M %p")
        expired_time = ((pd.to_datetime(now))-(pd.to_datetime(since)))
        expired_time=str(expired_time)
        pl_time=since[11:16] #postload time using slicing
        total_daysfrom_pl=expired_time[0:2]
        if (int(total_daysfrom_pl) <= 7  ):  

            timeset=expired_time[7:12]
            timeset_f_min = timeset
            th_set=timeset_f_min[0:2]#time hour
            th_set=int(th_set)
            tm_set=timeset_f_min[4:7]
            tm_set=int(tm_set)
            t_set =((th_set*60)+tm_set)/60
            total_daysfrom_pl= int(total_daysfrom_pl)
            req_time= (((total_daysfrom_pl*24)+t_set))
            if (req_time < 168):
                rem_time = req_time
                e=Attachnewlorry.objects.get(pk=instance.id)
                e.expired_hour=int(168-req_time)
                e.save()    
            if (req_time > 168) :
                change_status= Attachnewlorry.objects.get(pk=instance.id)
                print (change_status)
                change_status.status = "Expired"
                # change_status.expired_hour=00
                print (change_status)
                change_status.save()  
            enddate = (pd.to_datetime(since_date) + pd.DateOffset(days=7)).strftime("%Y-%m-%d ")
            return (since) 
        else:
            change_status= Attachnewlorry.objects.get(pk=instance.id)
            print (change_status)
            change_status.status = "Expired"
            change_status.expired_hour = 0
            print (change_status)
            change_status.save()  
            enddate = (pd.to_datetime(since_date) + pd.DateOffset(days=7)).strftime("%Y-%m-%d ")
            return (since)


    class Meta:
        model = Attachnewlorry
        fields=['id','uservehicle_number', 'current_location', 'vehicle_load_capacity','vehicle_name','routes','updated_date','status','expired_hour']
        
class postloadbidserializer(serializers.ModelSerializer): 
    class Meta:
        model = PostLoad
        fields = ('id','quantity','price', 'vehicle_name','pickup_location','drop_location')

class loadbookSerializer(serializers.ModelSerializer):
    PostLoad=postloadbidserializer(read_only=True, many=True)
    username=serializers.SerializerMethodField()
    
    def get_username(self,request,*args):
        obj = User.objects.get(pk= request.user.id)
        return obj.name
    class Meta:
        model=Bid
        fields=['id','fixed_price', 'comments','username','PostLoad']

class lorrybidSerializer(serializers.ModelSerializer):
    username=serializers.SerializerMethodField()
    profile_image =serializers.ImageField(source="user.profile_image")
  
    def get_username(self,user,*args):
        obj = User.objects.get(pk=user.id)
        return obj.name
    
    class Meta:
        model=Attachnewlorry
        fields=['id','username', 'vehicle_name','vehicle_load_capacity','vehicle_type','profile_image','enter_price']

class loadbidSerializer(serializers.ModelSerializer):
     class Meta:
        model=PostLoad
        fields=['id','pickup_location','drop_location']

class MyBidSerializer(serializers.ModelSerializer):
    Attachnewlorry=lorrybidSerializer(read_only=True, many=True)
    PostLoad=loadbidSerializer(read_only=True, many=True)
    class Meta:
        model=Bid
        fields=['id', 'fixed_price','PostLoad','Attachnewlorry']

class loadsentSerializer(serializers.ModelSerializer):
    username=serializers.SerializerMethodField()
    profile_image =serializers.ImageField(source="user.profile_image")
  
    def get_username(self,user,*args):
        obj = User.objects.get(pk=user.id)
        return obj.name
    
    class Meta:
        model=PostLoad
        fields=['id','username','quantity','material_name','price','pickup_location','drop_location','profile_image',]

class MyBidlorrySerializer(serializers.ModelSerializer):
    PostLoad=loadsentSerializer(read_only=True, many=True)
    class Meta:
        model=Bid
        fields=['id', 'fixed_price','PostLoad']   

class loadlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostLoad
        fields = ['id','pickup_location', 'drop_location','quantity','material_name','status']

class lorrylistSerializer(serializers.ModelSerializer):
    username=serializers.SerializerMethodField()
    profile_image =serializers.ImageField(source="user.profile_image")

    def get_username(self,request,*args):
        obj = User.objects.get(pk= request.user.id)
        return obj.name
    class Meta:
        model = Attachnewlorry
        fields = ['id','username','uservehicle_number','profile_image','current_location','vehicle_name','vehicle_load_capacity','enter_price','status']

class lorrybooklistSerializer(serializers.ModelSerializer):
    Attachnewlorry=lorrylistSerializer(read_only=True, many=True)
    PostLoad=loadlistSerializer(read_only=True, many=True)

    class Meta:
        model=Bid
        fields=['id', 'comments','PostLoad','Attachnewlorry']

class lorrymarketSerializer(serializers.ModelSerializer):
    username=serializers.SerializerMethodField()

    def get_username(self,request,*args):
        obj = User.objects.get(pk= request.user.id)
        return obj.name

    class Meta:
        model=Attachnewlorry
        fields=['id','vehicle_name', 'current_location','username','uservehicle_number','fixed_price','is_rc_verfied','routes']

class networkSerializer(serializers.ModelSerializer):
    username=serializers.SerializerMethodField()
    profile_image =serializers.ImageField(source="user.profile_image")
    role = RoleSerializer(read_only=True, many=True)

    def get_username(self,request,*args):
        obj = User.objects.get(pk= request.user.id)
        return obj.name

    class Meta:
        model = Attachnewlorry
        fields = ['id','username','current_location','profile_image','role']