from django import template
from django.template import Template
from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from django.urls import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def get_menu(context):
  content = {}
  urls = []
  urls.append({ 'Name' : 'virtual_machine' , 'url' : reverse('General:create_virtual_machine') })
  content.update( { 'urls' : content } )
  return mark_safe(render_to_string('General/Menu.html' , content ))