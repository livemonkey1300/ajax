from django.contrib import admin

# Register your models here.
from .models import APPLICATIONS , FULLY_MANAGED , VIRTUAL_MACHINEAPP

class APPLICATIONS_Inline(admin.TabularInline):
  model = APPLICATIONS

class FULLY_MANAGED_Inline(admin.TabularInline):
  model = FULLY_MANAGED

class VIRTUAL_MACHINEAPPAdmin(admin.ModelAdmin):
    list_display = ('applications','fully_managed')
    inlines = [APPLICATIONS_Inline,FULLY_MANAGED_Inline]


admin.site.register(APPLICATIONS)
admin.site.register(FULLY_MANAGED)
admin.site.register(VIRTUAL_MACHINEAPP)
