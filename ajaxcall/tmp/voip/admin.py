from django.contrib import admin

# Register your models here.
from .models import VOIP_QUOTE


class VOIPAPPAdmin(admin.ModelAdmin):
    inlines = []


admin.site.register(VOIP_QUOTE,VOIPAPPAdmin)