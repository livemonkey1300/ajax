from django import forms
from django.forms import ModelForm
from .models import  EXCHANGE ,  VOIP ,  VIRTUAL_MACHINE  


class EXCHANGE_Form(forms.ModelForm):
  class Meta:
    model = EXCHANGE
    fields = ( 'exchange_name' , 'business_name','mailbox','office_license','current_email_provider','number_of_employees','business_type','average_size_of_mailbox','migration_required',)


class VOIP_Form(forms.ModelForm):
  class Meta:
    model = VOIP
    fields = ( 'voip_name' , 'business_name','extension','locations','did_existing_local_number','did_new_local_number','fax_numbers','current_phone_provider','number_of_employees','tfs_existing_toll-free_numbers','tfs_new_toll-free_numbers','business_type',)


class VIRTUAL_MACHINE_Form(forms.ModelForm):
  class Meta:
    model = VIRTUAL_MACHINE
    fields = ( 'virtual_machine_name' , 'network_throughput','datacenter','operating_system','system_disk','data_disk','memory','vcpu','office2016standard','quickbooks2019','sage2019','sapbusinessone','cylanceaiendpointprotection','webrootsecurityendpoint''businesshoursmfest','monsunest')


