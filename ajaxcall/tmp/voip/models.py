from django.db import models

from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User



class VOIP_QUOTE(models.Model):
  voip_name = models.CharField(max_length=255,blank=True, null=True,default="",)
  business_name = models.CharField 
  extension = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(1000)]) 
  locations = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(100)]) 
  did_existing_local_number = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50)]) 
  did_new_local_number = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50)]) 
  fax_numbers = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(20)]) 
  current_phone_provider = models.CharField 
  number_of_employees = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(2000)]) 
  tfs_existing_toll_free_numbers = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50)]) 
  tfs_new_toll_free_numbers = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50)]) 

  BUSINESS_TYPE_CHOICE = (('Technology','Technology'),('Education','Education'),('Hospitality','Hospitality'),('Corporate','Corporate'),('Healthcare','Healthcare'),('Automotive','Automotive'),('Manufacturing','Manufacturing'))
  business_type = models.CharField(max_length=255,choices=BUSINESS_TYPE_CHOICE,default='Technology',)


  def __str__(self):
      return self.voip_name


  class Meta:
      verbose_name = 'Voip QUOTE'