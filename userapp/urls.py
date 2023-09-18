from django.contrib import admin
from django.urls import include, path
from .views import PaisentRegisterView, UserLoginView

urlpatterns = [

    path('paisent_regi/',PaisentRegisterView.as_view(),name="paisent_regi"),
    
    path('login/',UserLoginView.as_view(),name="login"), 

  
]