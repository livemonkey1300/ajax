from django import forms
from django.forms import ModelForm
from .models import  VOIP  from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class VOIP_Form(forms.ModelForm):
  class Meta:
    model = VOIP
    fields = ( 'voip_name' , 'business_name','extension','locations','did_existing_local_number','did_new_local_number','fax_numbers','current_phone_provider','number_of_employees','tfs_existing_toll-free_numbers','tfs_new_toll-free_numbers','business_type',)

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



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ( 'email', 'password1', 'password2', )

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ( 'first_name','last_name')