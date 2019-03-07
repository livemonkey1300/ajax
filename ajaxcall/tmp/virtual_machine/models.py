from django.db import models

from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.core.validators import MaxValueValidator, MinValueValidator


class DATACENTER(models.Model):
  DATACENTER_CHOICE = (('canada/eastern','Canada/Eastern'),('vancouver,bc','Vancouver, BC'),('losangeles,ca','Los Angeles, CA'),('brasilia,brasil','Brasilia, Brasil'),('ottawa,on','Ottawa, ON'),('miami,fl','Miami, FL'),('paris,france','Paris, France'),('mexicocity,mx','Mexico City, MX'))
  datacenter = models.CharField(max_length=255,choices=DATACENTER_CHOICE,default='canada/eastern',)

  def __str__(self):
      return self.datacenter

  
class OPERATING_SYSTEM(models.Model):
  OPERATING_SYSTEM_CHOICE = (('centos','CentOS'),('windowsserver','Windows Server'),('ubuntu','Ubuntu'),('debian','Debian'),('suselinux','SUSE Linux'),('opensuse','OpenSUSE'))
  operating_system = models.CharField(max_length=255,choices=OPERATING_SYSTEM_CHOICE,default='centos',)

  def __str__(self):
      return self.operating_system

  
class SYSTEM_DISK(models.Model):
  SYSTEM_DISK_CHOICE = (('hddsasdisk','HDD SAS Disk'),('ssdentdisk','SSD ENT Disk'))
  system_disk = models.CharField(max_length=255,choices=SYSTEM_DISK_CHOICE,default='hddsasdisk',)

  def __str__(self):
      return self.system_disk

  
class DATA_DISK(models.Model):
  DATA_DISK_CHOICE = (('hddsasdisk','HDD SAS Disk'),('ssdentdisk','SSD ENT Disk'))
  data_disk = models.CharField(max_length=255,choices=DATA_DISK_CHOICE,default='hddsasdisk',)

  def __str__(self):
      return self.data_disk

  
class MEMORY(models.Model):
  MEMORY_CHOICE = (('gb','2 GB'),('gb','4 GB'),('gb','6 GB'))
  memory = models.CharField(max_length=255,choices=MEMORY_CHOICE,default='gb',)

  def __str__(self):
      return self.memory

  
class VCPU(models.Model):
  VCPU_CHOICE = (('gb','2 GB'),('gb','90 GB'))
  vcpu = models.CharField(max_length=255,choices=VCPU_CHOICE,default='gb',)

  def __str__(self):
      return self.vcpu

  
class APPLICATIONS(models.Model):
  office2016standard  = models.BooleanField(default=False,verbose_name='Office 2016 Standard')
  quickbooks2019  = models.BooleanField(default=False,verbose_name='Quickbooks 2019')
  sage2019  = models.BooleanField(default=False,verbose_name='Sage 2019')
  sapbusinessone  = models.BooleanField(default=False,verbose_name='SAP Business One')
  cylanceaiendpointprotection  = models.BooleanField(default=False,verbose_name='Cylance AI+ Endpoint Protection')
  webrootsecurityendpoint  = models.BooleanField(default=False,verbose_name='Webroot Security Endpoint')

  def __str__(self):
    return '( Office 2016 Standard : %s )( Quickbooks 2019 : %s )( Sage 2019 : %s )( SAP Business One : %s )( Cylance AI+ Endpoint Protection : %s )( Webroot Security Endpoint : %s )' % ( self.office2016standard,self.quickbooks2019,self.sage2019,self.sapbusinessone,self.cylanceaiendpointprotection,self.webrootsecurityendpoint )

class FULLY_MANAGED(models.Model):
  businesshoursmfest  = models.BooleanField(default=False,verbose_name='Business Hours M-F EST')
  monsunest  = models.BooleanField(default=False,verbose_name='7-24 Mon-Sun EST')

  def __str__(self):
    return '( Business Hours M-F EST : %s )( 7-24 Mon-Sun EST : %s )' % ( self.businesshoursmfest,self.monsunest )


class VIRTUAL_MACHINEAPP(models.Model):
  network_throughput =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(1000)]) 
  datacenter = models.OneToOneField(DATACENTER,on_delete=models.CASCADE)
  operating_system = models.OneToOneField(OPERATING_SYSTEM,on_delete=models.CASCADE)
  system_disk = models.OneToOneField(SYSTEM_DISK,on_delete=models.CASCADE)
  data_disk = models.OneToOneField(DATA_DISK,on_delete=models.CASCADE)
  memory = models.OneToOneField(MEMORY,on_delete=models.CASCADE)
  vcpu = models.OneToOneField(VCPU,on_delete=models.CASCADE)
  applications = models.OneToOneField(APPLICATIONS,on_delete=models.CASCADE)
  fully_managed = models.OneToOneField(FULLY_MANAGED,on_delete=models.CASCADE)
