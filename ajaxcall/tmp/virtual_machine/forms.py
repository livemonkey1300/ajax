from django import forms
from django.forms import ModelForm
from .models import APPLICATIONS , FULLY_MANAGED , VIRTUAL_MACHINEAPP



class APPLICATIONSForm(forms.ModelForm):
  class Meta:
      model = APPLICATIONS
      fields = ('office2016standard','quickbooks2019','sage2019','sapbusinessone','cylanceaiendpointprotection','webrootsecurityendpoint','sense')

class FULLY_MANAGEDForm(forms.ModelForm):
  class Meta:
      model = FULLY_MANAGED
      fields = ('businesshoursmfest','monsunest')


class VIRTUAL_MACHINE_QUOTE_Form(models.Model):
  class Meta:
    model = VIRTUAL_MACHINEAPP
    fields = ( 'virtual_machine_name' , 'network_throughput''datacenter','operating_system','system_disk','data_disk','memory','vcpu','applications','fully_managed',)