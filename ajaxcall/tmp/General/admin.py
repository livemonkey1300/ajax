from django.contrib import admin

# Register your models here.
from .models import  VOIP ,  VIRTUAL_MACHINE  



admin.site.register(VOIP)
admin.site.register(VIRTUAL_MACHINE)
