from django.db import models

from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User



class TIME_MANAGEMENT_QUOTE(models.Model):
  time_management_name = models.CharField(max_length=255,blank=True, null=True,default="",)
  scheduled_date = models.DateField 
  time_scheduled = models.TimeField 
  subject = models.CharField 
  description = models.CharField 
  creator = models.CharField 



  def __str__(self):
      return self.time_management_name


  class Meta:
      verbose_name = 'Time Management QUOTE'