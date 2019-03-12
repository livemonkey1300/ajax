from django.contrib import admin

# Register your models here.
from .models import EXCHANGE_QUOTE


class EXCHANGEAPPAdmin(admin.ModelAdmin):
    inlines = []


admin.site.register(EXCHANGE_QUOTE,EXCHANGEAPPAdmin)