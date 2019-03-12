from django import forms
from django.forms import ModelForm
from .models import VOIP_QUOTE




class VOIP_QUOTE_Form(forms.ModelForm):
  class Meta:
    model = VOIP_QUOTE
    fields = ( 'voip_name' , 'business_name','extension','locations','did_existing_local_number','did_new_local_number','fax_numbers','current_phone_provider','number_of_employees','tfs_existing_toll-free_numbers','tfs_new_toll-free_numbers','business_type',)