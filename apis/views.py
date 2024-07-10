from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import *
from .serializers import *


#To give service list
class ServiceAPIView(APIView):
    def get(self, request , format = None):
        queryset = Service.objects.all()
        serializer = ServiceSerializer(queryset, many = True, context={'request': request})
        return Response(serializer.data , status= status.HTTP_200_OK)
    def post(self, request , format = None):
        serializer = ServiceSerializer(data= request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Service created successfully"}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
#To give a serivce's details
class ServcieDetailView(APIView):

    def get(self, request, id):
        try:
            service =  Service.objects.get(pk= id)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status= status.HTTP_404_NOT_FOUND)
        
        serializer = ServiceSerializer(service, context={'request': request})
        return Response(serializer.data, status= status.HTTP_200_OK)
    

class CaseStudyListAPIView(APIView):

    def get(self, request , format = None):
        queryset = CaseStudy.objects.all()
        serializer = CaseStudySerializer(queryset, many = True, context={'request': request})
        return Response(serializer.data , status= status.HTTP_200_OK)
    def post(self, request , format = None):
        serializer = CaseStudySerializer(data= request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Case study created successfully"}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

class CaseStudyDetailAPIView(APIView):
    def get(self, request, id):
        try:
            case_study = CaseStudy.objects.get(pk = id)
        except CaseStudy.DoesNotExist:
            return Response({"error": "Case Study not found"}, status= status.HTTP_404_NOT_FOUND)
        
        serializer = CaseStudySerializer(case_study, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)