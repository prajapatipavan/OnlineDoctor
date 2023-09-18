from msilib.schema import ListView
from django.shortcuts import render


from.models import User
from .forms  import PaisentCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

# Create your views here.

class PaisentRegisterView(CreateView):
    model =User
    template_name='paisent_regi.html'
    form_class=PaisentCreationForm
    success_url='/'

class UserLoginView (LoginView):
    template_name ='login.html'
    success_url ='/'


    