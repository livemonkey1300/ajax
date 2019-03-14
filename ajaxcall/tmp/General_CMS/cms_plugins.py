from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import  EXCHANGE ,  VOIP ,  VIRTUAL_MACHINE  
from .json_import import FORM


@plugin_pool.register_plugin
class EXCHANGEPlugin(forms.ModelForm):
    model = EXCHANGE
    name = _("Hello Plugin")
    render_template = 'General_CMS/exchange.html'
    cache = False

    def render(self, context, instance, placeholder):
        context = super(EXCHANGEPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class VOIPPlugin(forms.ModelForm):
    model = VOIP
    name = _("Hello Plugin")
    render_template = 'General_CMS/voip.html'
    cache = False

    def render(self, context, instance, placeholder):
        context = super(VOIPPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class VIRTUAL_MACHINEPlugin(forms.ModelForm):
    model = VIRTUAL_MACHINE
    name = _("Hello Plugin")
    render_template = 'General_CMS/virtual_machine.html'
    cache = False

    def render(self, context, instance, placeholder):
        context = super(VIRTUAL_MACHINEPlugin, self).render(context, instance, placeholder)
        return context

