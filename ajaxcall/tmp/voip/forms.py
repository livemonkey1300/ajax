from django import forms
from django.forms import ModelForm
from .models import VOIP_QUOTE




class VOIP_QUOTE_Form(models.Model):
  class Meta:
    model = VOIP_QUOTE
    fields = ( 'voip_name' , 'number_of_phone_number','provider',)