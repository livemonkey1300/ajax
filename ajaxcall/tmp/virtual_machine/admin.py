from django.contrib import admin

# Register your models here.
from .models import APPLICATIONS , FULLY_MANAGED , VIRTUAL_MACHINE_QUOTE

class APPLICATIONS_Inline(admin.TabularInline):
  model = APPLICATIONS
  extra = 0
class FULLY_MANAGED_Inline(admin.TabularInline):
  model = FULLY_MANAGED
  extra = 0

class VIRTUAL_MACHINEAPPAdmin(admin.ModelAdmin):
    inlines = [APPLICATIONS_Inline,FULLY_MANAGED_Inline]


admin.site.register(APPLICATIONS)
admin.site.register(FULLY_MANAGED)
admin.site.register(VIRTUAL_MACHINE_QUOTE,VIRTUAL_MACHINEAPPAdmin)