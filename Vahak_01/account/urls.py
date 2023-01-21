from django.urls import path, include
from .views import RegisterUser, ValidateOTP,OfficeAddressAPIView,Add_Company_Detail,AllocateUserRole,EditUserProfileApiView,AddCompanyBioAPIView,HelpsupportAPI
from rest_framework import routers
from .views import UserRoleModelViewSet,RoutesModelViewSet

router = routers.DefaultRouter()
#-----backend-user-api
router.register('add_user_role', UserRoleModelViewSet)
router.register('routes',RoutesModelViewSet)

urlpatterns = [
    path('help/', HelpsupportAPI.as_view()),
    path('register_user/', RegisterUser.as_view()),
    path('validate_otp/', ValidateOTP.as_view()),
    path('add_company_detail/', Add_Company_Detail.as_view()),
    path('assign_user_role/', AllocateUserRole.as_view()),
    path('edit_profile/<int:id>/',EditUserProfileApiView.as_view()),
    path('add_company_bio/<int:id>/',AddCompanyBioAPIView.as_view()),
    path('add_office_address/',OfficeAddressAPIView.as_view()),
    path('', include(router.urls)),
]
