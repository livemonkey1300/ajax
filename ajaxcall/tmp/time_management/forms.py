from django import forms
from django.forms import ModelForm
from .models import TIME_MANAGEMENT_QUOTE




class TIME_MANAGEMENT_QUOTE_Form(forms.ModelForm):
  class Meta:
    model = TIME_MANAGEMENT_QUOTE
    fields = ( 'time_management_name' , 'scheduled_date','time_scheduled','subject','description','creator',)