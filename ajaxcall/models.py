from django.db import models
from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
# Create your models here.

from abc import ABC, abstractmethod
from .gen import FieldGen
import re

class Model_Types(models.Model):
    Name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Types'

class Model_Choices(models.Model):
    Value = models.CharField(max_length=255,blank=True, null=True,default="",)

    def __str__(self):
        return self.Value

    class Meta:
        verbose_name = 'List choice'

class Model_Sub_Choices(models.Model):
    Value = models.CharField(max_length=255,blank=True, null=True,default="",)

    def __str__(self):
        return self.Value

    class Meta:
        verbose_name = 'List Sub choice'

class Model_Number(models.Model):
    Name = models.CharField(max_length=255,blank=True, null=True,default="",)
    min = models.IntegerField(default=1)
    max = models.IntegerField(default=1)
    default = models.IntegerField(default=1)
    step = models.IntegerField(default=1)
    price_calculate = models.BooleanField(default=True)
    price = models.FloatField(default=1)

    TEMPLATES = (('Slider', 'Slider'),('Number', 'Number'),('Slider_Number', 'Slider_Number'))
    template = models.CharField(max_length=255,choices=TEMPLATES,default='Number',)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Number'

    def get_field_name(self):
        return self.Name.lower().replace(' ','_')

    def get_field(self,request=False,session=False,model_name=False):
        value = self.default
        print('Workds')
        try:
            value = session['value']
        except KeyError:
            session['value'] = self.default
        if self.price_calculate:
            if session['price'] == 0 :
                session['price']  = self.price
        return { 'data' :  self , 'name' : model_name , 'value' : value , 'template' : 'ajaxcall/%s.html' % self.template }
        # return  mark_safe(render_to_string('ajaxcall/%s.html' % self.template , context ))

class Model_Choices_price(models.Model):
    Value = models.CharField(max_length=255,blank=True, null=True,default="",)
    price = models.FloatField(default=1)
    sub_choices = models.ManyToManyField(Model_Sub_Choices,blank=True)
    sub_price = models.ForeignKey(Model_Number,blank=True, null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return '%s - %s $' % ( self.Value , self.price )

    class Meta:
        verbose_name = 'List choices with price'

class Model_Choices_Group(models.Model):
    Name = models.CharField(max_length=255,blank=True, null=True,default="",)
    choices = models.ManyToManyField(Model_Choices, blank=True)
    choices_price = models.ManyToManyField(Model_Choices_price, blank=True)

    TEMPLATES = (('checkbox', 'checkbox'),('radio', 'radio'),('select', 'select'))
    template = models.CharField(max_length=255,choices=TEMPLATES,default='select',)

    def __str__(self):
        return self.Name

    def get_field_name(self):
        return self.Name.lower().replace(' ','_')

    def get_form_choice(self,select=False):
        ch = []
        cho = {}
        if select:
            select_to = ch
            cho = { 'select' : select , 'fields' : select_to }
        if len(self.choices.all()) > 0 :
            for i in self.choices.all():
                ch.append({ 'field' : re.sub('^[0-9]+' , '' , i.Value.lower().replace(' ','').replace('+' , '').replace('-' , '')) , 'verbose_name' : i.Value })
            if select:
                cho['fields'] = ch
                return cho
            return ch
        if len(self.choices_price.all()) > 0 :
            for i in self.choices_price.all():
                print(i)
                ch.append({ 'field' : re.sub('^[0-9]+' , '' ,i.Value.lower().replace(' ','').replace('+' , '').replace('-' , '')) , 'verbose_name' : i.Value })
            if select:
                cho['fields'] = ch
                return cho
            return ch
        return []

    def get_field(self,request=False,session=False,model_name=False):
        value = ''
        print('Inside Get Field' , self.get_field_name())
        try:
            value = session['value']
        except KeyError:
            session['value'] = ''
        if len(self.choices.all()) > 0 :
         return { 'data' :  self.choices.all() , 'name' : model_name , 'value' : value , 'template' : 'ajaxcall/%s.html' % self.template }
         # return  mark_safe(render_to_string('ajaxcall/%s.html' % self.template , context ))
        if len(self.choices_price.all()) > 0:
         try:
            request.session['lookup_table'][model_name] = {}
            session['price'] = float(0)
         except KeyError:
            request.session['lookup_table'] = { model_name : {} }
         if not session['price'] > float(0):
             session['price'] = float(0)
         for i in self.choices_price.all():
            request.session['lookup_table'][model_name].update( { i.id : i.price } )
         val = []
         for i in value:
             val.append(int(i))
         return { 'data' :  self.choices_price.all() , 'name' : model_name , 'value' : val , 'template' : 'ajaxcall/%s.html' % self.template }
         # return  mark_safe(render_to_string('ajaxcall/%s.html' % self.template , context ))

    class Meta:
        verbose_name = 'Choices Group'



class Model_Regular(models.Model):
    Name = models.CharField(max_length=255,blank=True, null=True,default="",)
    type = models.ForeignKey(Model_Types,blank=True,null=True,on_delete=models.CASCADE)
    value = models.CharField(max_length=255,blank=True, null=True)

    class Meta:
        verbose_name = 'Regular'

    def __str__(self):
        return self.Name

    def get_field_name(self):
        return self.Name.lower().replace(' ','_')

    def get_field(self,request=False,session=False,model_name=False):
        value = self.value
        if len(session['value'].strip()) > 0 :
            value = session['value']
        return { 'data' :  self , 'name' : model_name , 'value' : value , 'template' : 'ajaxcall/Fields.html' }
        # return  mark_safe(render_to_string('ajaxcall/Fields.html' , context ))

class Model_Inputs(models.Model):
    Name = models.CharField(max_length=255,blank=True, null=True,default="",)
    regular = models.ForeignKey(Model_Regular,blank=True, null=True,on_delete=models.SET_NULL)
    number = models.ForeignKey(Model_Number,blank=True, null=True,on_delete=models.SET_NULL)
    choices = models.ForeignKey(Model_Choices_Group,blank=True, null=True,on_delete=models.SET_NULL)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return '%s Priority : %s' % (self.Name,self.priority)

    def get_model_name(self):
        return self.Name.lower().replace(' ','_')

    def get_model_name_print(self):
        print(self.Name.lower().replace(' ','_'))

    def valid_model(self):
        if self.number:
            return True
        if self.regular:
            return True
        if self.choices:
            return False

    def valid_model_entery(self):
        if self.choices:
            if self.choices.template == 'checkbox':
                return self.choices.get_form_choice()
        if self.choices:
            if self.choices.template == 'radio' or self.choices.template == 'select':
                print('\n OK \n')
                return self.choices.get_form_choice(self.get_model_name())
        return False

    def valid_model_type(self):
        if self.number:
            return { 'Type' : 'number' , 'field' : True , 'Min' : self.number.min , 'Max' : self.number.max , 'Default' : self.number.default }
        if self.regular:
            return { 'Type' : 'regular' , 'field' : False }

    def get_field(self,request=False,Form_Name=''):
        context = { 'Form_Name' : Form_Name }
        if self.number:
            try:
                session = request.session[Form_Name][self.get_model_name()]
                context.update( self.number.get_field(request,session,self.get_model_name()))
            except KeyError:
                request.session[Form_Name][self.get_model_name()] = { 'value' : '' , 'price' : 0 , 'total' : 0 }
                session = request.session[Form_Name][self.get_model_name()]
                context.update( self.number.get_field(request,session,self.get_model_name()))
            return  mark_safe(render_to_string(context['template'] , context ))
        if self.regular:
            try:
                session = request.session[Form_Name][self.get_model_name()]
                context.update( self.regular.get_field(request,session,self.get_model_name()))
            except KeyError:
                request.session[Form_Name][self.get_model_name()] = { 'value' : '' }
                session = request.session[Form_Name][self.get_model_name()]
                context.update( self.regular.get_field(request,session,self.get_model_name()))
            return  mark_safe(render_to_string(context['template'] , context ))
        if self.choices:
            print(self.choices.get_field_name())
            try:
                print('Succeess')
                session = request.session[Form_Name][self.get_model_name()]
                context.update( self.choices.get_field(request,session,self.get_model_name()))
            except KeyError:
                print('Failed')
                request.session[Form_Name][self.get_model_name()] = { 'value' : '' , 'price' : 0 , 'total' : 0 }
                session = request.session[Form_Name][self.get_model_name()]
                context.update( self.choices.get_field(request,session,self.get_model_name()))
            return  mark_safe(render_to_string(context['template'] , context ))

    class Meta:
        verbose_name = 'All Fields'
        ordering = ['priority']



class AjaxForm(models.Model):
    Name = models.CharField(max_length=255)
    Field = models.ManyToManyField(Model_Inputs)

    def get_form_name(self):
        return self.Name.lower().replace(' ','_')

    def get_form_name_print(self):
        fgen = FieldGen(self)
        fgen.get_dict()
        fgen.create_app_dir()
        print(self.Name.lower().replace(' ','_'))

    def __str__(self):
        return self.Name

    def get_fields(self,request):
        fields = []
        form_name = self.get_form_name()
        for i in self.Field.all():
            try:
                fields.append(i.get_field(request,form_name))
                print('Workds')
            except AttributeError:
                pass
        return fields

    def get_form(self,request):
        request.session.modified = True
        try:
            session = request.session[self.get_form_name()]
        except KeyError:
            request.session[self.get_form_name()] = {}
            request.session[self.get_form_name()]['price_table'] = {}
        context = { 'form_nice_name': self.Name , 'form_name': self.get_form_name() , 'Fields' : self.get_fields(request) }
        return  mark_safe(render_to_string('ajaxcall/Master.html' , context ))

    def get_form_js(self,request):
        context = { 'form_nice_name': self.Name , 'form_name': self.get_form_name() , 'Fields' : self.get_fields(request) }
        return  mark_safe(render_to_string('ajaxcall/Master_JS.html' , context ))

    class Meta:
        verbose_name = 'Form'