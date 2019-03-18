from django.contrib import admin

# Register your models here.
from .models import TIME_MANAGEMENT_QUOTE


class TIME_MANAGEMENTAPPAdmin(admin.ModelAdmin):
    inlines = []


admin.site.register(TIME_MANAGEMENT_QUOTE,TIME_MANAGEMENTAPPAdmin)