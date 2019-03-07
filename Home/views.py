from django.shortcuts import render

# Create your views here.
from ajaxcall.models import  AjaxForm

def index(request):
  context = { 'APP': 'Page' , 'Forms' : [] , 'Forms_JS' : AjaxForm.objects.all()[0].get_form_js(request) }
  try:
      for i in AjaxForm.objects.all():
          context['Forms'].append( i.get_form(request))
  except AjaxForm.DoesNotExist:
    pass

  return render(request, 'Home/Home.html', context )
