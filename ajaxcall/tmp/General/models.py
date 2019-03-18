from django.db import models

from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

from .json_import import BUSINESS_TYPE_CHOICE ,AVERAGE_SIZE_OF_MAILBOX_CHOICE ,MIGRATION_REQUIRED_CHOICE ,BUSINESS_TYPE_CHOICE ,DATACENTER_CHOICE ,OPERATING_SYSTEM_CHOICE ,SYSTEM_DISK_CHOICE ,DATA_DISK_CHOICE ,MEMORY_CHOICE ,VCPU_CHOICE , PRICE_TABLE

class TIME_MANAGEMENT(models.Model):
  time_management_name = models.CharField(max_length=255,default='')
  scheduled_date =  models.DateField(max_length=255,verbose_name='Scheduled date',null=True,blank=True)
  time_scheduled =  models.TimeField(max_length=255,verbose_name='Time Scheduled',null=True,blank=True)
  subject =  models.CharField(max_length=255,default='Subject',verbose_name='Subject',null=True,blank=True)
  description =  models.CharField(max_length=255,default='Description',verbose_name='Description',null=True,blank=True)
  creator =  models.CharField(max_length=255,default='creator',verbose_name='creator',null=True,blank=True)

  def __str__(self):
    return self.time_management_name

  def get_display(self):
    content = { 'data' : self }
    return mark_safe(render_to_string('General/MODEL_TPL/time_management.html' , content ))

  class Meta:
    verbose_name = 'Time Management'




class EXCHANGE(models.Model):
  exchange_name = models.CharField(max_length=255,default='')
  business_type = models.CharField(max_length=255,choices=BUSINESS_TYPE_CHOICE,default='Automotive',)
  business_name =  models.CharField(max_length=255,default='Business Name',verbose_name='Business Name',null=True,blank=True)
  mailbox =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(1000)],verbose_name='MailBox' )
  office_license =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(1000)],verbose_name='Office License' )
  current_email_provider =  models.CharField(max_length=255,default='Current Email Provider',verbose_name='Current Email Provider',null=True,blank=True)
  number_of_employees =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(2000)],verbose_name='Number of employees' )
  average_size_of_mailbox = models.CharField(max_length=255,choices=AVERAGE_SIZE_OF_MAILBOX_CHOICE,default='5 GB',)
  migration_required = models.CharField(max_length=255,choices=MIGRATION_REQUIRED_CHOICE,default='No',)

  def __str__(self):
    return self.exchange_name

  def get_display(self):
    content = { 'data' : self }
    return mark_safe(render_to_string('General/MODEL_TPL/exchange.html' , content ))

  class Meta:
    verbose_name = 'Exchange'




class VOIP(models.Model):
  voip_name = models.CharField(max_length=255,default='')
  business_type = models.CharField(max_length=255,choices=BUSINESS_TYPE_CHOICE,default='Automotive',)
  business_name =  models.CharField(max_length=255,default='Business Name',verbose_name='Business Name',null=True,blank=True)
  extension =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(1000)],verbose_name='Extension' )
  locations =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(100)],verbose_name='Locations' )
  did_existing_local_number =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50)],verbose_name='DiD Existing Local Number' )
  did_new_local_number =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50)],verbose_name='DiD New Local Number' )
  fax_numbers =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(20)],verbose_name='Fax Numbers' )
  current_phone_provider =  models.CharField(max_length=255,default='Current phone provider',verbose_name='Current phone provider',null=True,blank=True)
  number_of_employees =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(2000)],verbose_name='Number of employees' )
  tfs_existing_toll_free_numbers =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50)],verbose_name='TFs Existing Toll-Free Numbers' )
  tfs_new_toll_free_numbers =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50)],verbose_name='TFs New Toll-Free Numbers' )

  def __str__(self):
    return self.voip_name

  def get_display(self):
    content = { 'data' : self }
    return mark_safe(render_to_string('General/MODEL_TPL/voip.html' , content ))

  class Meta:
    verbose_name = 'VOIP'




class VIRTUAL_MACHINE(models.Model):
  virtual_machine_name = models.CharField(max_length=255,default='')
  datacenter = models.CharField(max_length=255,choices=DATACENTER_CHOICE,default='Brasilia, Brasil',)
  operating_system = models.CharField(max_length=255,choices=OPERATING_SYSTEM_CHOICE,default='Debian',)
  system_disk = models.CharField(max_length=255,choices=SYSTEM_DISK_CHOICE,default='SSD ENT Disk',)
  data_disk = models.CharField(max_length=255,choices=DATA_DISK_CHOICE,default='SSD ENT Disk',)
  network_throughput =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(1000)],verbose_name='Network Throughput' )
  memory = models.CharField(max_length=255,choices=MEMORY_CHOICE,default='2 GB',)
  vcpu = models.CharField(max_length=255,choices=VCPU_CHOICE,default='2 vCPU',)
  quickbooks = models.BooleanField(default=False,verbose_name='Quickbooks 2019')
  sage = models.BooleanField(default=False,verbose_name='Sage 2019')
  sapbusinessone = models.BooleanField(default=False,verbose_name='SAP Business One')
  webrootsecurityendpoint = models.BooleanField(default=False,verbose_name='Webroot Security Endpoint')
  cylanceaiendpointprotection = models.BooleanField(default=False,verbose_name='Cylance AI+ Endpoint Protection')
  officestandard = models.BooleanField(default=False,verbose_name='Office 2016 Standard')
  businesshoursmfest = models.BooleanField(default=False,verbose_name='Business Hours M-F EST')
  monsunest = models.BooleanField(default=False,verbose_name='7-24 Mon-Sun EST')

  def __str__(self):
    return self.virtual_machine_name

  def get_display(self):
    content = { 'data' : self }
    return mark_safe(render_to_string('General/MODEL_TPL/virtual_machine.html' , content ))

  class Meta:
    verbose_name = 'Virtual Machine'




