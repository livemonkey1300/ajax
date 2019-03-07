from django.db import models

from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.core.validators import MaxValueValidator, MinValueValidator


class VOIPAPP(models.Model):
  voip_name = models.CharField(max_length=255,blank=True, null=True,default="",)
  network_throughput =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(1000)]) 


  def __str__(self):
      return self.voip_name

  class Meta:
      verbose_name = 'Voip'