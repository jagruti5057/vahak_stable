import django_filters
from django_filters import FilterSet, AllValuesFilter
# from django_filters import DateTimeFilter, NumberFilter
from rest_framework import generics 
from django_filters.rest_framework import DjangoFilterBackend
from .models import Businesscard,Attachnewlorry,PostLoad,Role,User

class PostLoadFilters(django_filters.FilterSet):
    min_quantity = django_filters.NumberFilter(field_name='quantity', lookup_expr='gte')
    max_quantity = django_filters.NumberFilter(field_name='quantity', lookup_expr='lte')   
    vehicle_name = AllValuesFilter(field_name='vehicle_name')
    is_aadhaar_verified = AllValuesFilter(field_name='user__is_aadhaar_verified')
    is_gst_verified = AllValuesFilter(field_name='user__is_gst_verified')
    class Meta:
        model = PostLoad
        fields = (
            'vehicle_name',
            'min_quantity',
            'max_quantity',
            'is_aadhaar_verified',
            'is_gst_verified'
            )
        
class AtachlorryFilters(django_filters.FilterSet):
    min_capacity = django_filters.NumberFilter(field_name='vehicle_load_capacity', lookup_expr='gte')
    max_capacity = django_filters.NumberFilter(field_name='vehicle_load_capacity', lookup_expr='lte')   
    vehicle_name = AllValuesFilter(field_name='vehicle_name')
    is_aadhaar_verified = AllValuesFilter(field_name='user__is_aadhaar_verified')
    is_gst_verified = AllValuesFilter(field_name='user__is_gst_verified')
    class Meta:
        model = Attachnewlorry
        fields = (
            'vehicle_name',
            'min_capacity',
            'max_capacity',
            'is_aadhaar_verified',
            'is_gst_verified'
            )      
        
class LoadFilters(django_filters.FilterSet):
    is_in_active = django_filters.AllValuesFilter(field_name='is_in_active')
    is_in_progress = django_filters.AllValuesFilter(field_name='is_in_progress')
    is_expired = django_filters.AllValuesFilter(field_name='is_expired')
    is_completed = django_filters.AllValuesFilter(field_name='is_completed')
    is_in_transit = django_filters.AllValuesFilter(field_name='is_in_transit')

    class Meta:
        model = PostLoad
        fields = (
            'is_in_active',
            'is_in_progress',
            'is_expired',
            'is_completed',
            'is_in_transit',
            )

class LorryFilters(django_filters.FilterSet):
    Truck= django_filters.CharFilter(field_name='vehicle_name')
    Lvc= django_filters.CharFilter(field_name='vehicle_name')
    Container= django_filters.CharFilter(field_name='vehicle_name')
    Hyva= django_filters.CharFilter(field_name='vehicle_name')
    Trailer= django_filters.CharFilter(field_name='vehicle_name')
    Tanker= django_filters.CharFilter(field_name='vehicle_name')
    
    class Meta:
        model = Attachnewlorry
        fields = (
            'Truck',
            'Lvc',
            'Container',
            'Hyva',
            'Trailer',
            'Tanker',
         )
 