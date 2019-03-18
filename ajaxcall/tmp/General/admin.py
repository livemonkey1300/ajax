from django.contrib import admin

# Register your models here.
from .models import TIME_MANAGEMENT ,EXCHANGE ,VOIP ,VIRTUAL_MACHINE 




admin.site.register(TIME_MANAGEMENT)
admin.site.register(EXCHANGE)
admin.site.register(VOIP)
admin.site.register(VIRTUAL_MACHINE)
