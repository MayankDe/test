from django import forms
from django.db import models
from django.db.models import fields
from .models import Image
class ImageForm(forms.ModelForm):
     class Meta:
         model=Image
         fields=("caption","image")