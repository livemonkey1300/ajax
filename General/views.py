from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
import json

from .models import  EXCHANGE ,  VOIP ,  VIRTUAL_MACHINE
from .forms import  EXCHANGE_Form ,  VOIP_Form ,  VIRTUAL_MACHINE_Form
from .json_import import FORM




def index(request):
  context = {}
  context.update({ 'exchange' : { 'item' : EXCHANGE.objects.all() , 'edit' : 'edit_exchange' ,  'create' : 'create_exchange' }})
  context.update({ 'voip' : { 'item' : VOIP.objects.all() , 'edit' : 'edit_voip' ,  'create' : 'create_voip' }})
  context.update({ 'virtual_machine' : { 'item' : VIRTUAL_MACHINE.objects.all() , 'edit' : 'edit_virtual_machine' ,  'create' : 'create_virtual_machine' }})
  return render(request, 'General/Main.html', context )

def get_price(request,form_name):
  session = request.session[form_name]
  total = 0
  for key , val in session.items():
      total += float(val['current'])
  return round(total,2)

def create_exchange(request):
    if request.method == 'POST':
        form = EXCHANGE_Form(request.POST)
        form.get_field(request,'EXCHANGE')
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = EXCHANGE_Form()
        form.get_field(request,'EXCHANGE')
    location = reverse('General:create_exchange')
    call = reverse('General:call' , kwargs={'form_name': 'EXCHANGE' } )
    return render(request, 'General/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'EXCHANGE')})



def edit_exchange(request,pk):
    exchange_instance = get_object_or_404(EXCHANGE, pk=pk)
    if request.method == 'POST':
        form = EXCHANGE_Form(request.POST,instance=exchange_instance)
        form.get_field(request,'EXCHANGE')
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = EXCHANGE_Form(instance=exchange_instance)
        form.get_field(request,'EXCHANGE')
    location = reverse('General:edit_exchange' , kwargs={'pk': pk} )
    call = reverse('General:call' , kwargs={'form_name': 'EXCHANGE' } )
    return render(request, 'General/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'EXCHANGE')  } )

def create_voip(request):
    if request.method == 'POST':
        form = VOIP_Form(request.POST)
        form.get_field(request,'VOIP')
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = VOIP_Form()
        form.get_field(request,'VOIP')
    location = reverse('General:create_voip')
    call = reverse('General:call' , kwargs={'form_name': 'VOIP' } )
    return render(request, 'General/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'VOIP') })



def edit_voip(request,pk):
    voip_instance = get_object_or_404(VOIP, pk=pk)
    if request.method == 'POST':
        form = VOIP_Form(request.POST,instance=voip_instance)
        form.get_field(request,'VOIP')
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = VOIP_Form(instance=voip_instance)
        form.get_field(request,'VOIP')
    location = reverse('General:edit_voip' , kwargs={'pk': pk} )
    call = reverse('General:call' , kwargs={'form_name': 'VOIP' } )
    return render(request, 'General/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'VOIP')  } )

def create_virtual_machine(request):
    if request.method == 'POST':
        form = VIRTUAL_MACHINE_Form(request.POST)
        form.get_field(request,'VIRTUAL_MACHINE')
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = VIRTUAL_MACHINE_Form()
        form.get_field(request,'VIRTUAL_MACHINE')
    location = reverse('General:create_virtual_machine')
    call = reverse('General:call' , kwargs={'form_name': 'VIRTUAL_MACHINE' } )
    return render(request, 'General/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'VIRTUAL_MACHINE')  })



def edit_virtual_machine(request,pk):
    virtual_machine_instance = get_object_or_404(VIRTUAL_MACHINE, pk=pk)
    if request.method == 'POST':
        form = VIRTUAL_MACHINE_Form(request.POST,instance=virtual_machine_instance)
        form.get_field(request,'VIRTUAL_MACHINE')
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = VIRTUAL_MACHINE_Form(instance=virtual_machine_instance)
        form.get_field(request,'VIRTUAL_MACHINE')
    location = reverse('General:edit_virtual_machine' , kwargs={'pk': pk} )
    call = reverse('General:call' , kwargs={'form_name': 'VIRTUAL_MACHINE' } )
    return render(request, 'General/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'VIRTUAL_MACHINE')  } )



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
