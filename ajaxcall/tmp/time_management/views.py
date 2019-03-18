from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
import json

from .models import TIME_MANAGEMENT_QUOTE
from .forms import TIME_MANAGEMENT_QUOTE_Form
from .json_import import FORM


def index(request):
  context = {}
  context.update({ 'time_management' : { 'item' : TIME_MANAGEMENT_QUOTE.objects.all() , 'edit' : 'edit_time_management_QUOTE' ,  'create' : 'create_time_management_QUOTE' }})
  return render(request, 'time_management/Main.html', context )



def create_time_management_QUOTE(request):
    if request.method == 'POST':
        form = TIME_MANAGEMENT_QUOTE_Form(request.POST)
        if form.is_valid():
          form.save()
    else:
        form = TIME_MANAGEMENT_QUOTE_Form()
    return render(request, 'time_management/form.html', {'form': form})

def edit_time_management_QUOTE(request,pk):
    time_management_instance = get_object_or_404(TIME_MANAGEMENT_QUOTE, pk=pk)
    if request.method == 'POST':
        form = TIME_MANAGEMENT_QUOTE_Form(request.POST,instance=time_management_instance)
        if form.is_valid():
          form.save()
          return redirect('time_management:index')
    else:
        form = TIME_MANAGEMENT_QUOTE_Form(instance=time_management_instance)
    return render(request, 'time_management/form.html', {'form': form})


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