from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from account.models import User,Routes,Role
from .serializer import PostModelSerializer,BannerSerializer,Businesscardserializer,MyBidSerializer,networkSerializer,lorrybooklistSerializer,lorrymarketSerializer,Attachnewlorryserializer,GetAttachnewlorryserializer,MyBidlorrySerializer,loadbookSerializer,viwesprofileSerializer,Lorrylistingserializer,viwescoverphotoSerializer,loadlistingSerializer
from .models import Businesscard,Attachnewlorry,PostLoad,Bid,Banner
from account.serializer import GetUserRoleSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from services.filters import PostLoadFilters,AtachlorryFilters,LoadFilters,LorryFilters
from rest_framework.pagination import PageNumberPagination

#-----------------APIView------------------------
class BannerAPI(APIView):
    def get(self,reuest,format=None):
        user = Banner.objects.all()
        serializer = BannerSerializer(user,many=True)
        return Response(serializer.data,status=200)

class BusinesscardAPI(APIView):
    def get(self,reuest,format=None):
        user = Businesscard.objects.all()
        serializer = Businesscardserializer(user,many=True)
        return Response(serializer.data,status=200)

    def post(self,request,format=None):
        serializer = Businesscardserializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BusinessCardUpdateAPI(APIView):     
    def put(self, request, id, format = None):
        user = Businesscard.objects.get(id=id)
        serializer = Businesscardserializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
        user = Businesscard.objects.get(id=id) 
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AttachnewlorryAPI(APIView):
    def get(self,reuest,format=None):
        user = Attachnewlorry.objects.all()
        serializer = GetAttachnewlorryserializer(user,many=True)
        return Response(serializer.data,status=200)

    def post(self,request,format=None):
        serializer = Attachnewlorryserializer(data=request.data)
        user=request.user
        user=User.objects.get(id=user.id)
        if serializer.is_valid():
           serializer.save(user=user)
           return Response(serializer.data)
        return Response(serializer.errors)

class AttachlorryUpdateAPI(APIView):    
    def put(self, request, id, format = None):
        user = Attachnewlorry.objects.get(id=id)
        serializer = Attachnewlorryserializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,id,format=None):
        user = Attachnewlorry.objects.get(id=id) 
        user.delete()
        return Response("Data deleted successfully ")

class PostLoadAPIView(APIView):
    def get(self,request,format=None):
        user = PostLoad.objects.all()
        serializer = PostModelSerializer(user,many=True)
        return Response(serializer.data,status=200)
    
    def post(self,request,format=None):
        serializer = PostModelSerializer(data=request.data)
        user=PostLoad.objects.get(id=request.user.id)
        if serializer.is_valid():
           serializer.save(user=user)
           return Response(serializer.data)
        return Response(serializer.errors)
    
class FilterAttachlorry(generics.ListAPIView):
    queryset = Attachnewlorry.objects.all()
    serializer_class = GetAttachnewlorryserializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AtachlorryFilters  
   
class FilterPostLoad(generics.ListAPIView):
    queryset = PostLoad.objects.all()
    serializer_class = PostModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostLoadFilters   

class viwesprofileAPIView(APIView):
    def get(self,request,format=None):
        user = User.objects.filter(id=request.user.id)
        serializer = viwesprofileSerializer(user,many=True)
        return Response(serializer.data,status=200)

    def put(self, request,  format = None):
        user = User.objects.get(id=request.user.id)
        serializer = viwescoverphotoSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class LoadlistingAPIView(APIView):
    def get(self,request,format=None):
        user = PostLoad.objects.filter(id=request.user.id)
        serializer = loadlistingSerializer(user,many=True)
        return Response(serializer.data,status=200)

    def put(self, request,  format = None):
        user = PostLoad.objects.get(id=request.user.id)
        serializer = loadlistingSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Filterloadlisting(generics.ListAPIView):
    queryset = PostLoad.objects.all()
    serializer_class = loadlistingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LoadFilters        
    
class Filterlorrylisting(generics.ListAPIView):
    queryset = Attachnewlorry.objects.all()
    serializer_class = Lorrylistingserializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LorryFilters  

class LorryListingAPI(APIView):
    def get(self,request,format=None):
        user = Attachnewlorry.objects.filter(user_id=request.user.id)
        serializer = Lorrylistingserializer(user,many=True)
        return Response(serializer.data,status=200)
   
class LoadbookAPI(APIView):
    def get(self,request,format=None):
        user = Bid.objects.filter(user_id=request.user.id)
        serializer = loadbookSerializer(user,many=True)
        return Response(serializer.data,status=200)

    def put(self, request,  format = None):
        user = Bid.objects.get(id=request.user.id)
        serializer = loadbookSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class MyBidAPI(APIView):
    def get(self,request,format=None):
        user = Bid.objects.filter(user_id=request.user.id)
        serializer = MyBidSerializer(user,many=True)
        return Response(serializer.data,status=200)

    def post(self,request,format=None):
        serializer = MyBidSerializer(data=request.data)
        user=request.user
        user=Attachnewlorry.objects.get(id=user.id)
        if serializer.is_valid():
           serializer.save(user=user)
           return Response(serializer.data)
        return Response(serializer.errors)
    
class MyBidlorryAPI(APIView):
    def get(self,request,format=None):
        user = Bid.objects.filter(user_id=request.user.id)
        serializer = MyBidlorrySerializer(user,many=True)
        return Response(serializer.data,status=200)

class LorrybookAPIView(APIView):
    def get(self,request,format=None):
        user = Bid.objects.filter(user_id=request.user.id)
        serializer = lorrybooklistSerializer(user,many=True)
        return Response(serializer.data,status=200)

class LorrymarketAPIView(APIView):
    def get(self,request,format=None):
        user = Attachnewlorry.objects.all()
        serializer = lorrymarketSerializer(user,many=True)
        return Response(serializer.data,status=200)
    
class NetworkAPIView(APIView):
    def get(self,request,format=None):
        user = Attachnewlorry.objects.all()
        serializer = networkSerializer(user,many=True)
        return Response(serializer.data,status=200)

    def post(self,request,format=None):
        serializer = networkSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Filternetwork(generics.ListAPIView):
    queryset = Attachnewlorry.objects.all()
    serializer_class = networkSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filter_backends=[SearchFilter]
    search_fields=['role__name','current_location','user__name']
