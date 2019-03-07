from django.contrib import admin

# Register your models here.
from .models import VOIPAPP


class VOIPAPPAdmin(admin.ModelAdmin):
    inlines = []


admin.site.register(VOIPAPP,VOIPAPPAdmin)