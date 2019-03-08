from django import forms
from django.forms import ModelForm
from .models import VOIPAPP




class VOIP_QUOTE_Form(models.Model):
  class Meta:
    model = VOIPAPP
    fields = ( 'voip_name' , 'number_of_phone_number')