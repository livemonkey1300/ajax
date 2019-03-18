from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import  TIME_MANAGEMENT  
from .json_import import FORM


@plugin_pool.register_plugin
class TIME_MANAGEMENTPlugin(forms.ModelForm):
    model = TIME_MANAGEMENT
    name = _("Hello Plugin")
    render_template = 'General_CMS/time_management.html'
    cache = False

    def render(self, context, instance, placeholder):
        context = super(TIME_MANAGEMENTPlugin, self).render(context, instance, placeholder)
        return context

