from django.db import models

from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class EXCHANGE(models.Model):
  user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
  exchange_name = models.CharField(max_length=255,blank=True, null=True,default="",)
  business_name = models.CharField(max_length=255,default='')
  mailbox = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(1000)])
  office_license = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(1000)])
  current_email_provider = models.CharField(max_length=255,default='')
  number_of_employees = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(2000)])
  BUSINESS_TYPE_CHOICE = (('Technology','Technology'),('Education','Education'),('Hospitality','Hospitality'),('Corporate','Corporate'),('Healthcare','Healthcare'),('Automotive','Automotive'),('Manufacturing','Manufacturing'))
  business_type = models.CharField(max_length=255,choices=BUSINESS_TYPE_CHOICE,default='Technology',)
  AVERAGE_SIZE_OF_MAILBOX_CHOICE = (('5 GB','5 GB'),('10 GB','10 GB'),('25 GB','25 GB'),('50 GB','50 GB'),('75 GB','75 GB'))
  average_size_of_mailbox = models.CharField(max_length=255,choices=AVERAGE_SIZE_OF_MAILBOX_CHOICE,default='5 GB',)
  MIGRATION_REQUIRED_CHOICE = (('Yes','Yes'),('No','No'))
  migration_required = models.CharField(max_length=255,choices=MIGRATION_REQUIRED_CHOICE,default='Yes',)


  def __str__(self):
      return self.exchange_name

  def get_display(self):
    content = { 'data' : self }
    return mark_safe(render_to_string('General/exchange.html' , content ))

  class Meta:
      verbose_name = 'Exchange'


class VOIP(models.Model):
  user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
  voip_name = models.CharField(max_length=255,blank=True, null=True,default="",)
  business_name = models.CharField(max_length=255,default='')
  extension = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(1000)])
  locations = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(100)])
  did_existing_local_number = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50)])
  did_new_local_number = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50)])
  fax_numbers = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(20)])
  current_phone_provider = models.CharField(max_length=255,default='')
  number_of_employees = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(2000)])
  tfs_existing_toll_free_numbers = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50)])
  tfs_new_toll_free_numbers = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50)])
  BUSINESS_TYPE_CHOICE = (('Technology','Technology'),('Education','Education'),('Hospitality','Hospitality'),('Corporate','Corporate'),('Healthcare','Healthcare'),('Automotive','Automotive'),('Manufacturing','Manufacturing'))
  business_type = models.CharField(max_length=255,choices=BUSINESS_TYPE_CHOICE,default='Technology',)


  def __str__(self):
      return self.voip_name

  def get_display(self):
    content = { 'data' : self }
    return mark_safe(render_to_string('General/voip.html' , content ))

  class Meta:
      verbose_name = 'Voip'


class VIRTUAL_MACHINE(models.Model):
  user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
  virtual_machine_name = models.CharField(max_length=255,blank=True, null=True,default="",)
  network_throughput = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(1000)])
  DATACENTER_CHOICE = (('Canada/Eastern','Canada/Eastern'),('Vancouver, BC','Vancouver, BC'),('Los Angeles, CA','Los Angeles, CA'),('Brasilia, Brasil','Brasilia, Brasil'),('Ottawa, ON','Ottawa, ON'),('Miami, FL','Miami, FL'),('Paris, France','Paris, France'),('Mexico City, MX','Mexico City, MX'))
  datacenter = models.CharField(max_length=255,choices=DATACENTER_CHOICE,default='Canada/Eastern',)
  OPERATING_SYSTEM_CHOICE = (('CentOS','CentOS'),('Windows Server','Windows Server'),('Ubuntu','Ubuntu'),('Debian','Debian'),('SUSE Linux','SUSE Linux'),('OpenSUSE','OpenSUSE'))
  operating_system = models.CharField(max_length=255,choices=OPERATING_SYSTEM_CHOICE,default='CentOS',)
  SYSTEM_DISK_CHOICE = (('HDD SAS Disk','HDD SAS Disk'),('SSD ENT Disk','SSD ENT Disk'))
  system_disk = models.CharField(max_length=255,choices=SYSTEM_DISK_CHOICE,default='HDD SAS Disk',)
  DATA_DISK_CHOICE = (('HDD SAS Disk','HDD SAS Disk'),('SSD ENT Disk','SSD ENT Disk'))
  data_disk = models.CharField(max_length=255,choices=DATA_DISK_CHOICE,default='HDD SAS Disk',)
  MEMORY_CHOICE = (('2 GB','2 GB'),('4 GB','4 GB'),('6 GB','6 GB'),('8 GB','8 GB'),('10 GB','10 GB'),('12 GB','12 GB'),('14 GB','14 GB'),('16 GB','16 GB'),('18 GB','18 GB'),('20 GB','20 GB'),('22 GB','22 GB'),('24 GB','24 GB'),('26 GB','26 GB'),('28 GB','28 GB'),('30 GB','30 GB'),('32 GB','32 GB'))
  memory = models.CharField(max_length=255,choices=MEMORY_CHOICE,default='2 GB',)
  VCPU_CHOICE = (('4 vCPU','4 vCPU'),('2 vCPU','2 vCPU'),('6 vCPU','6 vCPU'))
  vcpu = models.CharField(max_length=255,choices=VCPU_CHOICE,default='4 vCPU',)
  office2016standard  = models.BooleanField(default=False,verbose_name='Office 2016 Standard')
  quickbooks2019  = models.BooleanField(default=False,verbose_name='Quickbooks 2019')
  sage2019  = models.BooleanField(default=False,verbose_name='Sage 2019')
  sapbusinessone  = models.BooleanField(default=False,verbose_name='SAP Business One')
  cylanceaiendpointprotection  = models.BooleanField(default=False,verbose_name='Cylance AI+ Endpoint Protection')
  webrootsecurityendpoint  = models.BooleanField(default=False,verbose_name='Webroot Security Endpoint')
  businesshoursmfest  = models.BooleanField(default=False,verbose_name='Business Hours M-F EST')
  monsunest  = models.BooleanField(default=False,verbose_name='7-24 Mon-Sun EST')


  def __str__(self):
      return self.virtual_machine_name

  def get_display(self):
    content = { 'data' : self }
    return mark_safe(render_to_string('General/virtual_machine.html' , content ))

  class Meta:
      verbose_name = 'Virtual_machine'
