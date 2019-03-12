from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
import json

from .models import  EXCHANGE_Form ,  VOIP_Form ,  VIRTUAL_MACHINE_Form  
from .forms import  EXCHANGE_Form ,  VOIP_Form ,  VIRTUAL_MACHINE_Form  
from .json_import import FORM




def index(request):
  context = {}
  context.update({ 'general' : { 'item' : GENERAL_QUOTE.objects.all() , 'edit' : 'edit_general_QUOTE' ,  'create' : 'create_general_QUOTE' }})
  return render(request, 'General/Main.html', context )


def create_exchange(request):
    if request.method == 'POST':
        form = EXCHANGE_Form(request.POST)
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = EXCHANGE_Form()
    location = reverse('General:create_exchange')
    return render(request, 'General/form.html', {'form': form , 'pk' : location }})



def edit_exchange(request,pk):
    exchange_instance = get_object_or_404(EXCHANGE, pk=pk)
    if request.method == 'POST':
        form = EXCHANGE_Form(request.POST,instance=exchange_instance)
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = EXCHANGE_Form(instance=exchange_instance)
    location = reverse('General:edit_exchange' , kwargs={'pk': pk} )
    return render(request, 'General/form.html', {'form': form , 'pk' : location } )


def create_voip(request):
    if request.method == 'POST':
        form = VOIP_Form(request.POST)
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = VOIP_Form()
    location = reverse('General:create_voip')
    return render(request, 'General/form.html', {'form': form , 'pk' : location }})



def edit_voip(request,pk):
    voip_instance = get_object_or_404(VOIP, pk=pk)
    if request.method == 'POST':
        form = VOIP_Form(request.POST,instance=voip_instance)
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = VOIP_Form(instance=voip_instance)
    location = reverse('General:edit_voip' , kwargs={'pk': pk} )
    return render(request, 'General/form.html', {'form': form , 'pk' : location } )


def create_virtual_machine(request):
    if request.method == 'POST':
        form = VIRTUAL_MACHINE_Form(request.POST)
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = VIRTUAL_MACHINE_Form()
    location = reverse('General:create_virtual_machine')
    return render(request, 'General/form.html', {'form': form , 'pk' : location }})



def edit_virtual_machine(request,pk):
    virtual_machine_instance = get_object_or_404(VIRTUAL_MACHINE, pk=pk)
    if request.method == 'POST':
        form = VIRTUAL_MACHINE_Form(request.POST,instance=virtual_machine_instance)
        if form.is_valid():
          form.save()
          return redirect('General:index')
    else:
        form = VIRTUAL_MACHINE_Form(instance=virtual_machine_instance)
    location = reverse('General:edit_virtual_machine' , kwargs={'pk': pk} )
    return render(request, 'General/form.html', {'form': form , 'pk' : location } )




def ajax_call(request,field=False):
    if request.method == 'POST' and field:
      request.session.modified = True
      try :
        request.session[field]['value'] = request.POST.get(field)
        try:
            request.session[field]['price'] = FORM[field][request.session[field]['value']]
        except KeyError:
            try:
                request.session[field]['price'] = FORM[field]['price']
            except KeyError:
                pass
      except KeyError:
          request.session[field] = {}
          request.session[field]['value'] = request.POST.get(field)
          try:
              request.session[field]['price'] = FORM[field][request.session[field]['value']]
          except KeyError:
              try:
                  request.session[field]['price'] = FORM[field]['price']
              except KeyError:
                  request.session[field]['price'] = 0
          request.session[field]['current'] = 0
      try:
         request.session[field]['current'] = float(request.session[field]['value']) *  request.session[field]['price']
      except Exception as e:
         request.session[field]['current'] = request.session[field]['price'] *  1
    return HttpResponse(json.dumps({ 'success' : True , 'field' : request.session[field]['value'] , 'price' : request.session[field]['price'] , 'current' : request.session[field]['current']  }), content_type="application/json")