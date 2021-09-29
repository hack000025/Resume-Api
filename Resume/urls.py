"""PortFolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Resume.views import ProfileListCreateAPIView,EducationAPIView,ProfileDestroyAPIView, ExperienceAPIView , ProjectsAPIView , CertificationAPIView ,SkillsAPIView
# from Resume.views import ProfileCRUDCBV
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token , refresh_jwt_token ,verify_jwt_token

urlpatterns = [

    # path('api/profile/',ProfileCRUDCBV.as_view(),name = 'profile'),
    path('api/profile/',ProfileListCreateAPIView.as_view(),name = 'profile-listcreate'),
    path('api/profile/a_delete/<int:id>',ProfileDestroyAPIView.as_view(),name = 'profile'),
    path('api/profile/education/',EducationAPIView.as_view(),name = 'education'),
    path('api/profile/experince/',ExperienceAPIView.as_view(),name = 'experince'),
    path('api/profile/projects/',ProjectsAPIView.as_view(),name = 'project'),
    path('api/profile/certification',CertificationAPIView.as_view(),name = 'certification'),
    path('api/profile/skills',SkillsAPIView.as_view(),name = 'skills'),


]
