from pickle import FALSE

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User


class PaisentCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields =["username","email","contact","password1","password2"]

    @transaction.atomic
    def save(self,commit=True):
        user = super().save(commit=FALSE)
        user.is_paisent=True
        if commit:
             user.save()
        return user    