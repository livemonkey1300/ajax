from django.shortcuts import render , redirect
from django.http import HttpResponse
import json
from .models import Model_Types
# Create your views here.


def index(request):
    menu = GetMenu()
    menu.start()
    menu.print_sql()
    return redirect('Form_Handler:index')


def call(request,field=False,fsub=False):
    if field:
     price = 0
     request.session.modified = True
     try:
        print(request.session[fsub])
        request.session[fsub][field]['value'] = request.POST.get(field)
        value = request.session[fsub][field]['value']
        print(value)
        try:
            print(request.session[fsub][field]['price'])
            try:
                print(request.session['lookup_table'][field])
                val = value.split(',')
                if len(val) > 1:
                    val.pop(len(val) - 1)
                request.session[fsub][field]['value'] = val
                calc = 0
                print(request.session)
                for i in request.session[fsub][field]['value']:
                    calc += request.session['lookup_table'][field][i]
                request.session[fsub][field]['price'] = calc
                request.session[fsub][field]['total'] = round(request.session[fsub][field]['price'], 2)
                print(request.session['lookup_table'])
                price = request.session[fsub][field]['total']
            except Exception as e:
                request.session[fsub][field]['total'] = round(request.session[fsub][field]['price'] * float(request.session[fsub][field]['value']), 2)
                price = request.session[fsub][field]['total']
        except Exception as e:
            print(e)
        total = 0
        for key ,val in request.session[fsub].items():
            try:
                total += val['total']
                print(val['total'])
            except Exception as e:
                pass
        return HttpResponse(json.dumps({ 'success' : True , 'price' : price , 'form' : fsub , 'total' : round(total, 2) , 'look' : request.session['lookup_table'] }), content_type="application/json")
     except KeyError:
        return HttpResponse(json.dumps({ 'success' : False  }), content_type="application/json")
        pass
    else:
        return HttpResponse(json.dumps({ 'success' : False  }), content_type="application/json")

def init_types(request):
    with open("./ajaxcall/fields.txt", "r") as ins:
        array = []
        for line in ins:
            nline = line.strip().split(":")
            try:
                mod = Model_Types.objects.get(Name=nline[0])
                mod.register = nline[1]
                mod.save()
            except Model_Types.DoesNotExist:
                mod = Model_Types()
                mod.Name = nline[0]
                mod.register = nline[1]
                mod.save()
    return redirect('Home:index')
