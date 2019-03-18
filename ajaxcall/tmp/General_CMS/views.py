from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
import json

from .models import  TIME_MANAGEMENT  
from .forms import  TIME_MANAGEMENT_Form  
from .json_import import FORM




def index(request):
  context = {}
  context.update({ 'time_management' : { 'item' : TIME_MANAGEMENT.objects.all() , 'edit' : 'edit_time_management' ,  'create' : 'create_time_management' }})
  return render(request, 'General_CMS/Main.html', context )

def get_price(request,form_name):
  session = request.session[form_name]
  total = 0
  for key , val in session.items():
      total += float(val['current'])
  return total

def create_time_management(request):
    if request.method == 'POST':
        form = TIME_MANAGEMENT_Form(request.POST)
        form.get_field(request,'TIME_MANAGEMENT')
        if form.is_valid():
          form.save()
          return redirect('General_CMS:index')
    else:
        form = TIME_MANAGEMENT_Form()
        form.get_field(request,'TIME_MANAGEMENT')
    location = reverse('General_CMS:create_time_management')
    call = reverse('General:call' , kwargs={'form_name': 'TIME_MANAGEMENT' } )
    return render(request, 'General_CMS/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'TIME_MANAGEMENT')  })



def edit_time_management(request,pk):
    time_management_instance = get_object_or_404(TIME_MANAGEMENT, pk=pk)
    if request.method == 'POST':
        form = TIME_MANAGEMENT_Form(request.POST,instance=time_management_instance)
        form.get_field(request,'TIME_MANAGEMENT')
        if form.is_valid():
          form.save()
          return redirect('General_CMS:index')
    else:
        form = TIME_MANAGEMENT_Form(instance=time_management_instance)
        form.get_field(request,'TIME_MANAGEMENT')
    location = reverse('General_CMS:edit_time_management' , kwargs={'pk': pk} )
    call = reverse('General:call' , kwargs={'form_name': 'TIME_MANAGEMENT' } )
    return render(request, 'General_CMS/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'TIME_MANAGEMENT')  } )



def ajax_call(request,form_name=False,field=False):
    remove = False
    if request.method == 'POST' and field and form_name :
      request.session.modified = True
      session = ''
      try:
          session = request.session[form_name]
      except KeyError:
          request.session[form_name] = {}
          session = request.session[form_name]
      try :
        if session[field]['value'] == 'on,':
            remove = True
        session[field]['value'] = request.POST.get(field)
        try:
            if not remove:
                session[field]['price'] = FORM[field][session[field]['value']]
            else:
                session[field]['price'] = 0
        except KeyError:
            try:
                session[field]['price'] = FORM[field]['price']
            except KeyError:
                pass
      except KeyError:
          session[field] = {}
          session[field]['value'] = request.POST.get(field)
          try:
              session[field]['price'] = FORM[field][session[field]['value']]
          except KeyError:
              try:
                  session[field]['price'] = FORM[field]['price']
              except KeyError:
                  session[field]['price'] = 0
          session[field]['current'] = 0
      try:
         session[field]['current'] = float(session[field]['value']) *  session[field]['price']
      except Exception as e:
         session[field]['current'] = session[field]['price'] *  1
    return HttpResponse(json.dumps({ 'success' : True , 'field' : session[field]['value'] , 'price' : session[field]['price'] , 'current' : session[field]['current'] , 'total'  : get_price(request,form_name) }), content_type="application/json")