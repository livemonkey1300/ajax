from django.db import models

from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.core.validators import MaxValueValidator, MinValueValidator

class APPLICATIONS(models.Model):
  office2016standard  = models.BooleanField(default=False,verbose_name='Office 2016 Standard')
  quickbooks2019  = models.BooleanField(default=False,verbose_name='Quickbooks 2019')
  sage2019  = models.BooleanField(default=False,verbose_name='Sage 2019')
  sapbusinessone  = models.BooleanField(default=False,verbose_name='SAP Business One')
  cylanceaiendpointprotection  = models.BooleanField(default=False,verbose_name='Cylance AI+ Endpoint Protection')
  webrootsecurityendpoint  = models.BooleanField(default=False,verbose_name='Webroot Security Endpoint')
  sense  = models.BooleanField(default=False,verbose_name='sense')

  def __str__(self):
    return '( Office 2016 Standard : %s )( Quickbooks 2019 : %s )( Sage 2019 : %s )( SAP Business One : %s )( Cylance AI+ Endpoint Protection : %s )( Webroot Security Endpoint : %s )( sense : %s )' % ( self.office2016standard,self.quickbooks2019,self.sage2019,self.sapbusinessone,self.cylanceaiendpointprotection,self.webrootsecurityendpoint,self.sense )

  class Meta:
      verbose_name = 'Applications'

class FULLY_MANAGED(models.Model):
  businesshoursmfest  = models.BooleanField(default=False,verbose_name='Business Hours M-F EST')
  monsunest  = models.BooleanField(default=False,verbose_name='7-24 Mon-Sun EST')

  def __str__(self):
    return '( Business Hours M-F EST : %s )( 7-24 Mon-Sun EST : %s )' % ( self.businesshoursmfest,self.monsunest )

  class Meta:
      verbose_name = 'Fully Managed'


class VIRTUAL_MACHINE_QUOTE(models.Model):
  virtual_machine_name = models.CharField(max_length=255,blank=True, null=True,default="",)
  network_throughput =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(1000)])
  DATACENTER_CHOICE = (('Canada/Eastern','Canada/Eastern'),('Vancouver, BC','Vancouver, BC'),('Los Angeles, CA','Los Angeles, CA'),('Brasilia, Brasil','Brasilia, Brasil'),('Ottawa, ON','Ottawa, ON'),('Miami, FL','Miami, FL'),('Paris, France','Paris, France'),('Mexico City, MX','Mexico City, MX'),('Miami 3','Miami 3'))
  datacenter = models.CharField(max_length=255,choices=DATACENTER_CHOICE,default='Canada/Eastern',)
  OPERATING_SYSTEM_CHOICE = (('CentOS','CentOS'),('Windows Server','Windows Server'),('Ubuntu','Ubuntu'),('Debian','Debian'),('SUSE Linux','SUSE Linux'),('OpenSUSE','OpenSUSE'),('sense','sense'))
  operating_system = models.CharField(max_length=255,choices=OPERATING_SYSTEM_CHOICE,default='CentOS',)
  SYSTEM_DISK_CHOICE = (('HDD SAS Disk','HDD SAS Disk'),('SSD ENT Disk','SSD ENT Disk'))
  system_disk = models.CharField(max_length=255,choices=SYSTEM_DISK_CHOICE,default='HDD SAS Disk',)
  DATA_DISK_CHOICE = (('HDD SAS Disk','HDD SAS Disk'),('SSD ENT Disk','SSD ENT Disk'))
  data_disk = models.CharField(max_length=255,choices=DATA_DISK_CHOICE,default='HDD SAS Disk',)
  MEMORY_CHOICE = (('2 GB','2 GB'),('4 GB','4 GB'),('6 GB','6 GB'))
  memory = models.CharField(max_length=255,choices=MEMORY_CHOICE,default='2 GB',)
  VCPU_CHOICE = (('2 GB','2 GB'),('90 GB','90 GB'))
  vcpu = models.CharField(max_length=255,choices=VCPU_CHOICE,default='2 GB',)
  applications = models.ForeignKey(APPLICATIONS,null=True,on_delete=models.SET_NULL)
  fully_managed = models.ForeignKey(FULLY_MANAGED,null=True,on_delete=models.SET_NULL)


  def __str__(self):
      return self.virtual_machine_name


  class Meta:
      verbose_name = 'Virtual Machine QUOTE'
