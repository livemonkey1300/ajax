from django import forms
from django.forms import ModelForm
from .models import EXCHANGE_QUOTE




class EXCHANGE_QUOTE_Form(forms.ModelForm):
  class Meta:
    model = EXCHANGE_QUOTE
    fields = ( 'exchange_name' , 'business_name','mailbox','office_license','current_email_provider','number_of_employees','business_type','average_size_of_mailbox','migration_required',)