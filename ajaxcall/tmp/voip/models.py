from django.db import models

from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.core.validators import MaxValueValidator, MinValueValidator


class VOIP_QUOTE(models.Model):
  voip_name = models.CharField(max_length=255,blank=True, null=True,default="",)
  number_of_phone_number =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50)]) 
  PROVIDER_CHOICE = (('roger','roger'),('videotron','videotron'))
  provider = models.CharField(max_length=255,choices=PROVIDER_CHOICE,default='roger',)


  def __str__(self):
      return self.voip_name


  class Meta:
      verbose_name = 'Voip QUOTE'