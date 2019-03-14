from django.contrib import admin

# Register your models here.
from .models import  EXCHANGE ,  VOIP ,  VIRTUAL_MACHINE  



admin.site.register(EXCHANGE)
admin.site.register(VOIP)
admin.site.register(VIRTUAL_MACHINE)
