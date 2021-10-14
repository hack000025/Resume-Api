
from django.shortcuts import render
from rest_framework.response import Response
from Resume.models import Profile , Education , Experience , Certification , Projects ,Skills
from Resume.serializer import ProfileSerializer , EducationSerializer , CertificationSerializer, ProjectSerializer , ExperienceSerializer,SkillsSerializers
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated ,AllowAny ,IsAdminUser
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from rest_framework.views import View
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView , DestroyAPIView ,UpdateAPIView
from rest_framework import viewsets

class ProfileListCreateAPIView (ListCreateAPIView ):
    # authentication_classes = [JSONWebTokenAuthentication ,]
    authentication_classes =[BasicAuthentication,]
   
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# class ProfileUpdateAPIView (UpdateAPIView ):
#     # authentication_classes = [JSONWebTokenAuthentication ,]
#     authentication_classes =[BasicAuthentication,]
#     lookup_field = 'id'
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

class ProfileDestroyAPIView(DestroyAPIView):
    def delete(self, request, id):

         authentication_classes =[BasicAuthentication,]
        idno = models.Profile.objects.filter(id=id)
        if len(idno)==0:
            return Response({'message':'Profile not found'}, status=400)
        idno.delete()
        return Response({'message':'Profile deleted successfully'},status=200)


class EducationAPIView(APIView):
     authentication_classes =[BasicAuthentication,]

    def get(self,request,*args,**kwarg):
        qs = Education.objects.all()
        serializer = EducationSerializer(qs,many = True)
        return Response(serializer.data,status=200)


class ExperienceAPIView(APIView):
     authentication_classes =[BasicAuthentication,]
    def get(self,request,*args,**kwarg):
        qs = Experience.objects.all()
        serializer = ExperienceSerializer(qs,many = True)
        return Response(serializer.data,status=200)



class ProjectsAPIView(APIView):
     authentication_classes =[BasicAuthentication,]
    def get(self,request,*args,**kwarg):
        qs = Projects.objects.all()
        serializer = ProjectSerializer(qs,many = True)
        return Response(serializer.data,status=200)



class CertificationAPIView(APIView):
     authentication_classes =[BasicAuthentication,]
    def get(self,request,*args,**kwarg):
        qs = Certification.objects.all()
        serializer = CertificationSerializer(qs,many = True)
        return Response(serializer.data,status=200)

class SkillsAPIView(APIView):
     authentication_classes =[BasicAuthentication,]
    def get(self,request,*args,**kwargs):
        qs = Skills.objects.all()
        serializer = SkillsSerializers(qs,many = True)
        return Response(serializer.data, status =200)
