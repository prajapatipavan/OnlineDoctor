
from django import views
from django.contrib import admin
from django.urls import include, path
from .views import Deletepaisent, Docmainpage, Listpaisent, Registerpaisent , Addmainpage

urlpatterns = [
    
     path('register/',Registerpaisent.as_view(),name="registerpaisent"),
    
     path('list/',Listpaisent.as_view(),name="listalldata"),

     path('index/',Addmainpage.as_view(),name="indexmain"),

      path('delete/<int:pk>',Deletepaisent.as_view(),name="deletepa"),

      path('doclist/',Docmainpage.as_view(),name="doclist"),
    
  
]
