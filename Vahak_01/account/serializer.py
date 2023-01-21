from rest_framework import serializers
from .models import User,Role,Routes,OfficeAddress,HelpSupport
from account.helpers import updateuserfields
        
class AddCompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('name', 'city','referral_code')
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields=['id','name']
        read_only_fields=('id',)   

    def save(self, **kwargs):
        """Include default for read_only `user` field"""
        kwargs["name"] = self.fields["name"].get_default()
        return super().save(**kwargs)

class QASerializer(serializers.ModelSerializer):
    class Meta:
        model=HelpSupport
        fields=['id','qa_data']
        
class GetUserRoleSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True, many=True)
    class Meta:
        model=User
        fields=['id','name','city','role',]
        read_only_fields=('id',)

class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Routes
        fields=['id','name']

class RoutesviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Routes
        fields=['name']
        
class AddCompanyBioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('company_start_date','company_bio')

class OfficeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=OfficeAddress
        fields=['user','building_number','area','landmark','city','pincode']

class EditUserProfileSerializer(serializers.ModelSerializer):
    routes = RoutesSerializer(read_only=True, many=True)
    services = RoleSerializer(source='role',read_only=True, many=True)
    
    def update(self, instance, validated_data):
        # Delete all records of genres.
        try:
            if 'routes' in self.initial_data: 
                route_data=self.initial_data['routes']
            else:
                route_data=''
            
            if 'services' in self.initial_data: 
                services=self.initial_data['services']
            else:
                services=''   
            #-----------------Routes-----------------------
            if route_data != '':
                updateuserfields(User,Routes,instance,route_data,'routes')
                
            #--------------------chnageUserRole-----------------
            if services != '':
                updateuserfields(User,Role,instance,services,'service')
            event_updated = super().update(instance, validated_data)
            return event_updated
        except Exception as e:
            raise serializers.ValidationError({'detail': e})
            
    class Meta:
        model = User
        fields = ('profile_image', 'cover_image', 'city', 'name','routes','services')