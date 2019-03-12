from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
import json

from .models import EXCHANGE_QUOTE
from .forms import EXCHANGE_QUOTE_Form
from .json_import import FORM


def index(request):
  context = {}
  context.update({ 'exchange' : { 'item' : EXCHANGE_QUOTE.objects.all() , 'edit' : 'edit_exchange_QUOTE' ,  'create' : 'create_exchange_QUOTE' }})
  return render(request, 'exchange/Main.html', context )



def create_exchange_QUOTE(request):
    if request.method == 'POST':
        form = EXCHANGE_QUOTE_Form(request.POST)
        if form.is_valid():
          form.save()
    else:
        form = EXCHANGE_QUOTE_Form()
    return render(request, 'exchange/form.html', {'form': form})

def edit_exchange_QUOTE(request,pk):
    exchange_instance = get_object_or_404(EXCHANGE_QUOTE, pk=pk)
    if request.method == 'POST':
        form = EXCHANGE_QUOTE_Form(request.POST,instance=exchange_instance)
        if form.is_valid():
          form.save()
          return redirect('exchange:index')
    else:
        form = EXCHANGE_QUOTE_Form(instance=exchange_instance)
    return render(request, 'exchange/form.html', {'form': form})


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