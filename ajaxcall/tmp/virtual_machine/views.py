from django.shortcuts import render , redirect

from .ctl import CTL



#------- DOC -----------




def index(request):
  controller = CTL()
  context = {}
  return render(request, 'virtual_machine/Main.html', context )


def add_applications(request,id=0,iframe=0):
    context =  {'APP': 'applications' }
    controller = CTL(id)
    if id == 0:
          context.update({'Form' : controller.get_applicationsForm() , 'submit' : 'applications' })
    else:
          context.update({'Status': 'Edit' , 'ID' : id })
          context.update({'Form' : controller.init_applicationsForm_id(request) , 'submit' : 'applications' })
    return render(request, 'virtual_machine/add.html', context )

def add_fully_managed(request,id=0,iframe=0):
    context =  {'APP': 'fully_managed' }
    controller = CTL(id)
    if id == 0:
          context.update({'Form' : controller.get_fully_managedForm() , 'submit' : 'fully_managed' })
    else:
          context.update({'Status': 'Edit' , 'ID' : id })
          context.update({'Form' : controller.init_fully_managedForm_id(request) , 'submit' : 'fully_managed' })
    return render(request, 'virtual_machine/add.html', context )


def submit_ctl(request,name,id=0):
    controller = CTL(id)
    if name == 'applications':
        if id != 0:
            controller.init_applicationsForm_id(request)
            return redirect('virtual_machine:index')
        controller.init_AccountsForm(request)
        return redirect('virtual_machine:index')
    if name == 'fully_managed':
        if id != 0:
            controller.init_fully_managedForm_id(request)
            return redirect('virtual_machine:index')
        controller.init_AccountsForm(request)
        return redirect('virtual_machine:index')
    return redirect('virtual_machine:index')


