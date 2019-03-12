from django.db import models

from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.core.validators import MaxValueValidator, MinValueValidator



class EXCHANGE_QUOTE(models.Model):
  exchange_name = models.CharField(max_length=255,blank=True, null=True,default="",)
  business_name = models.CharField(max_length=255,default='') 
  mailbox = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(1000)]) 
  office_license = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(1000)]) 
  current_email_provider = models.CharField(max_length=255,default='') 
  number_of_employees = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(2000)]) 

  BUSINESS_TYPE_CHOICE = (('Technology','Technology'),('Education','Education'),('Hospitality','Hospitality'),('Corporate','Corporate'),('Healthcare','Healthcare'),('Automotive','Automotive'),('Manufacturing','Manufacturing'))
  business_type = models.CharField(max_length=255,choices=BUSINESS_TYPE_CHOICE,default='Technology',)
  AVERAGE_SIZE_OF_MAILBOX_CHOICE = (('5 GB','5 GB'),('10 GB','10 GB'),('25 GB','25 GB'),('50 GB','50 GB'))
  average_size_of_mailbox = models.CharField(max_length=255,choices=AVERAGE_SIZE_OF_MAILBOX_CHOICE,default='5 GB',)
  MIGRATION_REQUIRED_CHOICE = (('Yes','Yes'),('No','No'))
  migration_required = models.CharField(max_length=255,choices=MIGRATION_REQUIRED_CHOICE,default='Yes',)


  def __str__(self):
      return self.exchange_name


  class Meta:
      verbose_name = 'Exchange QUOTE'