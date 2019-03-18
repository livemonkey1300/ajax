from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
import json


from .json_import import FORM


from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
import json

from .json_import import FORM





def get_price(request,form_name):
  session = request.session[form_name]
  total = 0
  for key , val in session.items():
      total += float(val['current'])
  return total

class TIME_MANAGEMENT(models.Model):

def create_time_management(request):
    if request.method == 'POST':
        form = TIME_MANAGEMENT_Form(request.POST)
        form.get_field(request,'TIME_MANAGEMENT')
        if form.is_valid():
          if request.user.is_authenticated:
            form.save()
            return redirect('Time Management:index')
          else:
            return render(request, 'Time Management/mail.html', {'form': form.cleaned_data ,  'total' :  get_price(request,'TIME_MANAGEMENT') })
    else:
        form = _Form()
        form.get_field(request,'time_management')
    location = reverse('Time Management:create_time_management')
    call = reverse('General:call' , kwargs={'form_name': 'TIME_MANAGEMENT' } )
    return render(request, 'Time Management/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'TIME_MANAGEMENT')  })

def edit_time_management(request,pk):
  if request.user.is_authenticated:
    time_management_instance = get_object_or_404(TIME_MANAGEMENT, pk=pk)
    if request.method == 'POST':
        form = TIME_MANAGEMENT_Form(request.POST,instance=time_management_instance)
        form.get_field(request,'time_management')
        if form.is_valid():
          form.save()
          return redirect('Time Management:index')
    else:
        form = TIME_MANAGEMENT_Form(instance=time_management_instance)
        form.get_field(request,'TIME_MANAGEMENT')
    location = reverse('Time Management:edit_time_management' , kwargs={'pk': pk} )
    call = reverse('General:call' , kwargs={'form_name': 'TIME_MANAGEMENT' } )
    return render(request, 'Time Management/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'TIME_MANAGEMENT')  } )
  else:
    return redirect('Time Management:index')




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


from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
import json

from .json_import import FORM





def get_price(request,form_name):
  session = request.session[form_name]
  total = 0
  for key , val in session.items():
      total += float(val['current'])
  return total

class EXCHANGE(models.Model):

def create_exchange(request):
    if request.method == 'POST':
        form = EXCHANGE_Form(request.POST)
        form.get_field(request,'EXCHANGE')
        if form.is_valid():
          if request.user.is_authenticated:
            form.save()
            return redirect('Exchange:index')
          else:
            return render(request, 'Exchange/mail.html', {'form': form.cleaned_data ,  'total' :  get_price(request,'EXCHANGE') })
    else:
        form = _Form()
        form.get_field(request,'exchange')
    location = reverse('Exchange:create_exchange')
    call = reverse('General:call' , kwargs={'form_name': 'EXCHANGE' } )
    return render(request, 'Exchange/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'EXCHANGE')  })

def edit_exchange(request,pk):
  if request.user.is_authenticated:
    exchange_instance = get_object_or_404(EXCHANGE, pk=pk)
    if request.method == 'POST':
        form = EXCHANGE_Form(request.POST,instance=exchange_instance)
        form.get_field(request,'exchange')
        if form.is_valid():
          form.save()
          return redirect('Exchange:index')
    else:
        form = EXCHANGE_Form(instance=exchange_instance)
        form.get_field(request,'EXCHANGE')
    location = reverse('Exchange:edit_exchange' , kwargs={'pk': pk} )
    call = reverse('General:call' , kwargs={'form_name': 'EXCHANGE' } )
    return render(request, 'Exchange/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'EXCHANGE')  } )
  else:
    return redirect('Exchange:index')




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


from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
import json

from .json_import import FORM





def get_price(request,form_name):
  session = request.session[form_name]
  total = 0
  for key , val in session.items():
      total += float(val['current'])
  return total

class VOIP(models.Model):

def create_voip(request):
    if request.method == 'POST':
        form = VOIP_Form(request.POST)
        form.get_field(request,'VOIP')
        if form.is_valid():
          if request.user.is_authenticated:
            form.save()
            return redirect('VOIP:index')
          else:
            return render(request, 'VOIP/mail.html', {'form': form.cleaned_data ,  'total' :  get_price(request,'VOIP') })
    else:
        form = _Form()
        form.get_field(request,'voip')
    location = reverse('VOIP:create_voip')
    call = reverse('General:call' , kwargs={'form_name': 'VOIP' } )
    return render(request, 'VOIP/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'VOIP')  })

def edit_voip(request,pk):
  if request.user.is_authenticated:
    voip_instance = get_object_or_404(VOIP, pk=pk)
    if request.method == 'POST':
        form = VOIP_Form(request.POST,instance=voip_instance)
        form.get_field(request,'voip')
        if form.is_valid():
          form.save()
          return redirect('VOIP:index')
    else:
        form = VOIP_Form(instance=voip_instance)
        form.get_field(request,'VOIP')
    location = reverse('VOIP:edit_voip' , kwargs={'pk': pk} )
    call = reverse('General:call' , kwargs={'form_name': 'VOIP' } )
    return render(request, 'VOIP/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'VOIP')  } )
  else:
    return redirect('VOIP:index')




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


from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
import json

from .json_import import FORM





def get_price(request,form_name):
  session = request.session[form_name]
  total = 0
  for key , val in session.items():
      total += float(val['current'])
  return total

class VIRTUAL_MACHINE(models.Model):

def create_virtual_machine(request):
    if request.method == 'POST':
        form = VIRTUAL_MACHINE_Form(request.POST)
        form.get_field(request,'VIRTUAL_MACHINE')
        if form.is_valid():
          if request.user.is_authenticated:
            form.save()
            return redirect('Virtual Machine:index')
          else:
            return render(request, 'Virtual Machine/mail.html', {'form': form.cleaned_data ,  'total' :  get_price(request,'VIRTUAL_MACHINE') })
    else:
        form = _Form()
        form.get_field(request,'virtual_machine')
    location = reverse('Virtual Machine:create_virtual_machine')
    call = reverse('General:call' , kwargs={'form_name': 'VIRTUAL_MACHINE' } )
    return render(request, 'Virtual Machine/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'VIRTUAL_MACHINE')  })

def edit_virtual_machine(request,pk):
  if request.user.is_authenticated:
    virtual_machine_instance = get_object_or_404(VIRTUAL_MACHINE, pk=pk)
    if request.method == 'POST':
        form = VIRTUAL_MACHINE_Form(request.POST,instance=virtual_machine_instance)
        form.get_field(request,'virtual_machine')
        if form.is_valid():
          form.save()
          return redirect('Virtual Machine:index')
    else:
        form = VIRTUAL_MACHINE_Form(instance=virtual_machine_instance)
        form.get_field(request,'VIRTUAL_MACHINE')
    location = reverse('Virtual Machine:edit_virtual_machine' , kwargs={'pk': pk} )
    call = reverse('General:call' , kwargs={'form_name': 'VIRTUAL_MACHINE' } )
    return render(request, 'Virtual Machine/form.html', {'form': form , 'pk' : location , 'call' : call , 'total' :  get_price(request,'VIRTUAL_MACHINE')  } )
  else:
    return redirect('Virtual Machine:index')




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