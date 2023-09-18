

from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView
from django.views.generic.list import ListView
from .models import paisent


# Create your views here.

class Registerpaisent(CreateView):
    template_name="register.html"
    model=paisent
    success_url="/consult/index"
    fields= "__all__"

class Listpaisent(ListView):
    context_object_name="paisents"
    model = paisent
    template_name = "list.html"

class Addmainpage(ListView):
    context_object_name="mains"
    model=paisent
    template_name = "index.html"

    
class Docmainpage(ListView):
    context_object_name="doctorlist"
    model=paisent
    template_name = "doclist.html"



class Deletepaisent(DeleteView):
    model = paisent
    template_name = "delete.html"
    success_url="/consult/list"
  

