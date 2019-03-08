from django.shortcuts import render , redirect

from .ctl import CTL



#------- DOC -----------




def index(request):
  controller = CTL()
  context = {}
  return render(request, 'voip/Main.html', context )



def submit_ctl(request,name,id=0):
    controller = CTL(id)
    return redirect('voip:index')


