from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404

from .models import APPLICATIONS , FULLY_MANAGED , VIRTUAL_MACHINE_QUOTE
from .forms import APPLICATIONSForm , FULLY_MANAGEDForm , VIRTUAL_MACHINE_QUOTE_Form
from .json_import import FORM


def index(request):
  context = {}
  context.update({ 'applications' : { 'item' : APPLICATIONS.objects.all() , 'edit' : 'edit_applications' ,  'create' : 'create_applications' }})
  context.update({ 'fully_managed' : { 'item' : FULLY_MANAGED.objects.all() , 'edit' : 'edit_fully_managed' ,  'create' : 'create_fully_managed' }})
  context.update({ 'virtual_machine' : { 'item' : VIRTUAL_MACHINE_QUOTE.objects.all() , 'edit' : 'edit_virtual_machine_QUOTE' ,  'create' : 'create_virtual_machine_QUOTE' }})
  return render(request, 'virtual_machine/Main.html', context )


def create_applications(request):
    if request.method == 'POST':
        form = APPLICATIONSForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('virtual_machine:index')
    else:
        form = APPLICATIONSForm()
    return render(request, 'virtual_machine/form.html', {'form': form})


def edit_applications(request,pk):
    applications_instance = get_object_or_404(APPLICATIONS, pk=pk)
    if request.method == 'POST':
        form = APPLICATIONSForm(request.POST,instance=applications_instance)
        if form.is_valid():
          form.save()
          return redirect('virtual_machine:index')
    else:
        form = APPLICATIONSForm(instance=applications_instance)
    return render(request, 'virtual_machine/form.html', {'form': form , 'item' : applications_instance  })


def create_fully_managed(request):
    if request.method == 'POST':
        form = FULLY_MANAGEDForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('virtual_machine:index')
    else:
        form = FULLY_MANAGEDForm()
    return render(request, 'virtual_machine/form.html', {'form': form})


def edit_fully_managed(request,pk):
    fully_managed_instance = get_object_or_404(FULLY_MANAGED, pk=pk)
    if request.method == 'POST':
        form = FULLY_MANAGEDForm(request.POST,instance=fully_managed_instance)
        if form.is_valid():
          form.save()
          return redirect('virtual_machine:index')
    else:
        form = FULLY_MANAGEDForm(instance=fully_managed_instance)
    return render(request, 'virtual_machine/form.html', {'form': form , 'item' : fully_managed_instance  })



def create_virtual_machine_QUOTE(request):
    if request.method == 'POST':
        form = VIRTUAL_MACHINE_QUOTE_Form(request.POST)
        if form.is_valid():
          form.save()
    else:
        form = VIRTUAL_MACHINE_QUOTE_Form()
    return render(request, 'virtual_machine/form.html', {'form': form})

def edit_virtual_machine_QUOTE(request,pk):
    virtual_machine_instance = get_object_or_404(VIRTUAL_MACHINE_QUOTE, pk=pk)
    if request.method == 'POST':
        form = VIRTUAL_MACHINE_QUOTE_Form(request.POST,instance=virtual_machine_instance)
        if form.is_valid():
          form.save()
          return redirect('virtual_machine:index')
    else:
        form = VIRTUAL_MACHINE_QUOTE_Form(instance=virtual_machine_instance)
    return render(request, 'virtual_machine/form.html', {'form': form})


def ajax_call(request,field=False):
    if request.method == 'POST' and field:
      request.session.modified = True
      try :
        request.session[field]['price'] = 0
        request.session[field]['value'] = request.POST.get(field)
      except KeyError:
          request.session[field] = {}
          request.session[field]['price'] = 0
          request.session[field]['value'] = request.POST.get(field)
    return HttpResponse(json.dumps({ 'success' : True , 'field' : request.session[field]['value'] }), content_type="application/json")