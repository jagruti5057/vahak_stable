from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,Role,Routes,OfficeAddress,HelpSupport
from .serializer import AddCompanyDetailSerializer,QASerializer,RoleSerializer,RoutesSerializer,OfficeAddressSerializer,EditUserProfileSerializer,GetUserRoleSerializer,AddCompanyBioSerializer
from account.helpers import get_tokens_for_user,send_otp_via_email
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

#-------------ModelViewSet-----------------------
class UserRoleModelViewSet(ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

class RoutesModelViewSet(ModelViewSet):
    serializer_class=RoutesSerializer
    queryset=Routes.objects.all()

#-----------------APIView------------------------
class HelpsupportAPI(APIView):
    def get(self,reuest,format=None):
        user = HelpSupport.objects.all()
        serializer = QASerializer(user,many=True)
        return Response(serializer.data,status=200)

    def post(self,request,format=None):
        serializer = QASerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class RegisterUser(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email:
            email = str(email)
            user = User.objects.filter(email=email)
            key = send_otp_via_email(email)
            if key:
                old = User.objects.filter(email=email)
                if old.exists():
                    old = old.first()
                    count = old.count
                    if count > 10:
                        return Response({'status' : False, 'detail' : 'Maximum otp limits reached. Kindly support our customer care or try with different number'})   
                    old.count = count+1
                    old.save()
                    response={
                            'user_id':old.id,
                            'status': True,
                            'otp':key,
                            'details':'OTP send successfully',
                        }
                    print("count increase", count)
                    return Response(response,status=status.HTTP_200_OK)
                else:
                    data=User(email=email,otp=key)
                    data.save()
                    response={
                            'user_id':data.id,
                            'otp':key,
                            'details':'OTP send successfully',
                            'status': True
                        }
                    return Response(response,status=status.HTTP_201_CREATED)           
            else:
                return Response({'status': False, 'detail' : "OTP sending error. Please try after some time."})
        else:
            return Response({'status': False, 'detail': 'Email is not given in post request'})
                    
class ValidateOTP(APIView):
    def post(self, request, *args, **kwargs):
        try:
            email = request.data .get('email', False)
            otp_send = request.data.get('otp', False)
            if email and otp_send:
                old = User.objects.filter(email=email)
                if old.exists():
                    old = old.first()
                    otp = old.otp
                    print(otp_send,otp)
                    if str(otp_send) == str(otp):
                        old.validated = True
                        old.save()
                        token = get_tokens_for_user(old)

                        return Response({'token':token,'status': True, 'detail' : "OTP matched."})
                    else:
                        return Response({'status': False, 'detail': 'OTP incoorect'})            
                else:
                    return Response({'status': False, 'detail' : "First proceed via sending otp request"})    
            else:
                return Response({'status': False, 'detail' : "Please provide both email and otp for validation"})
        except Exception as e:
            print("Something went wrong")
            
class Add_Company_Detail(APIView):
    """
    List all Company_Detail, or create a new Company_Detail.
    """
    def get(self, request, format=None):
        try:
            snippets = User.objects.all()
            serializer = AddCompanyDetailSerializer(snippets, many=True)
            response={
                'data':serializer.data,
                'status':True
            }
            return Response(response)
        
        except Exception :
            return Response("Something went wrong",status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request, format=None):
        try:
            old = User.objects.get(id = request.user.id)
            company_name=request.data.get('name','')
            city=request.data.get('city','')
            referral_code=request.data.get('referral_code')
            if old:
                old.city=city
                old.company_name=company_name
                old.referral_code=referral_code
                old.save()
                response={
                        'details':'data added successfully',
                        'status': True
                            }
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                return Response("Please Login again",status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response("Something went Wrong",status=status.HTTP_400_BAD_REQUEST)    

class AddCompanyBioAPIView(APIView):
    """
    Add Company Bio At User Profile
    """
    def put(self,request,id,format=None):
        user=User.objects.get(id=id)
        serializer = AddCompanyBioSerializer(user,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class OfficeAddressAPIView(APIView):
    def get(self,reuest,format=None):
        user = OfficeAddress.objects.all()
        serializer = OfficeAddressSerializer(user,many=True)
        return Response(serializer.data,status=200)

    def post(self,request,format=None):
        serializer = OfficeAddressSerializer(data=request.data)
        user=request.user
        user=User.objects.get(id=user.id)
        if serializer.is_valid():
           serializer.save(user=user)
           return Response(serializer.data)
        return Response(serializer.errors)
  
class AllocateUserRole(APIView):
    """
    Assigning user role, One user can have multiple role.
    """
    def get(self,request):
        try:
            user=request.user
            print
            snippets=User.objects.filter(id=user.id)
            serializer=GetUserRoleSerializer(snippets, many=True)
            response={
                'data':serializer.data,
                'status':True
            }
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception:
            response={
                'data':"Something went Wrong",
                'status':False
            }
            return Response(response)
    def post(self,request):
        try:
            roles=request.data.get("role")
            user=request.user
            for role in roles:
                role_obj=Role.objects.filter(id=role).first()
                if role_obj:
                    user.role.add(role_obj.id)
                else:
                    response={
                    'details':"Please Add valid role",
                    'status': False
                        }
                    return Response(response)
            response={
                'details':'data added successfully',
                'status': True
                    }
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception :
            return Response("Something went wrong")
  
class EditUserProfileApiView(APIView):
    """
    List UserProfile Detail, or Update UserProfile Detail...
    """
    # parser_classes = [MultiPartParser, FormParser]
    def get(self,request,format=None,*args, **kwargs,):
        user_id=kwargs['id']
        user = User.objects.filter(id=user_id)
        serializer = EditUserProfileSerializer(user,many=True)
        response={
                    'data':serializer.data,
                    'status':True
            }
        return Response(response,status=200)

    def put(self, request, id, format = None):        
        user = User.objects.get(id=id)
        serializer = EditUserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response={
                'data':serializer.data,
                'status':True
            }
            return Response(response,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
        
        
        
            