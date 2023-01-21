
from . import views
from rest_framework import routers
from django.urls import path, include
router = routers.DefaultRouter()
# router.register('vehicle',views.VehicalModelViewSet)


urlpatterns = [
    #----------------routers-------------------
    path('', include(router.urls)),
    path('banner/', views.BannerAPI.as_view()),
    path('Attachnewlorry/', views.AttachnewlorryAPI.as_view()),
    path('Attachnewlorry/<int:id>/', views.AttachlorryUpdateAPI.as_view()),
    path('post_load/', views.PostLoadAPIView.as_view()),
    path('post_load_filters/',views.FilterPostLoad.as_view()),
    path('attachlorryfilters/',views.FilterAttachlorry.as_view()),
    path('viewsprofile/',views.viwesprofileAPIView.as_view()),
    path('viewscoverimges/',views.viwesprofileAPIView.as_view()),
    path('loadlisting/',views.LoadlistingAPIView.as_view()),
    path('load_listing_filters/',views.Filterloadlisting.as_view()),
    path('lorry_listing_filters/',views.Filterlorrylisting.as_view()),
    path('lorrylisting/',views.LorryListingAPI.as_view()),
    path('loadbooknow/',views.LoadbookAPI.as_view()),
    path('mybidload/',views.MyBidAPI.as_view()),
    path('mybidlorry/',views.MyBidlorryAPI.as_view()),
    path('lorrybooknow/',views.LorrybookAPIView.as_view()),
    path('lorrymarket/',views.LorrymarketAPIView.as_view()),
    path('network_filters/',views.Filternetwork.as_view()),
]