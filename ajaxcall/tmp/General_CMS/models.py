from cms.models.pluginmodel import CMSPlugin
from django.db import models

from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class TIME_MANAGEMENT(CMSPlugin):
  time_management_name = models.CharField(max_length=255,blank=True, null=True,default="",)
  scheduled_date = models.DateField() 
  time_scheduled = models.TimeField() 
  subject = models.CharField(max_length=255,default='') 
  description = models.CharField(max_length=255,default='') 
  creator = models.CharField(max_length=255,default='') 


  def __str__(self):
      return self.time_management_name

  def get_display(self):
    content = { 'data' : self }
    return mark_safe(render_to_string('General_CMS/time_management.html' , content ))

  class Meta:
      verbose_name = 'Time_management'

