from django import forms
from django.forms import ModelForm
from .models import  TIME_MANAGEMENT  
from .json_import import FORM

def ajax_init(request,form_name=False,field=False):
    request.session.modified = True
    field_Name = field['name']
    field_data = field['initial']
    field_type = field['type']
    price = 0
    current = 0
    try:
        session = request.session[form_name]
    except KeyError:
        request.session[form_name] = {}
        session = request.session[form_name]
    try:
        price = FORM[field_Name][field_data]['price']
    except KeyError:
        price = FORM[field_Name][field_data]['value']
    try:
         current = float(field_data) *  price
    except Exception as e:
         current = price *  1
    value = field_data
    if field_type == 'checkbox':
        if field_data:
            value = 'on,'
        else:
            value = ''
    try:
        session[field_Name] = { 'price' : price , 'value' : value , 'current' : current }
    except KeyError:
        session[field_Name] = { 'price' : price , 'value' : value , 'current' : current }


class TIME_MANAGEMENT_Form(forms.ModelForm):
  class Meta:
    model = TIME_MANAGEMENT
    fields = ( 'time_management_name' , 'scheduled_date','time_scheduled','subject','description','creator',)

    def get_field(self,request=False,form_name=False):
      fields = []
      for item in self.fields.items():
          field = { 'initial' : item[1].initial , 'name' : item[0] , 'type' : item[1].widget.input_type }
          try:
              ajax_init(request,form_name,field)
          except Exception as e:
              pass
          fields.append(field)
      return fields

