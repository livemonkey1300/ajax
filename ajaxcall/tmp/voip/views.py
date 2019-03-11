from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404

from .models import VOIP_QUOTE
from .forms import VOIP_QUOTE_Form
from .json_import import FORM


def index(request):
  context = {}
  context.update({ 'voip' : { 'item' : VOIP_QUOTE.objects.all() , 'edit' : 'edit_voip_QUOTE' ,  'create' : 'create_voip_QUOTE' }})
  return render(request, 'voip/Main.html', context )



def create_voip_QUOTE(request):
    if request.method == 'POST':
        form = VOIP_QUOTE_Form(request.POST)
        if form.is_valid():
          form.save()
    else:
        form = VOIP_QUOTE_Form()
    return render(request, 'voip/form.html', {'form': form})

def edit_voip_QUOTE(request,pk):
    voip_instance = get_object_or_404(VOIP_QUOTE, pk=pk)
    if request.method == 'POST':
        form = VOIP_QUOTE_Form(request.POST,instance=voip_instance)
        if form.is_valid():
          form.save()
          return redirect('voip:index')
    else:
        form = VOIP_QUOTE_Form(instance=voip_instance)
    return render(request, 'voip/form.html', {'form': form})


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