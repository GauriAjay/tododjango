from django import forms
from django.forms import ModelForm
from .models import *
class AddListForm(ModelForm):
    class Meta:
        model=List
        fields=['item']