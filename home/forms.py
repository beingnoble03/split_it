import imp
from django import forms
from .models import *
from django.forms import fields
  
class ProfilePictureForm(forms.ModelForm):
  
    class Meta:
        model = ProfilePicture
        fields = '__all__'