from django.db import models
from django.template import loader, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
# Create your models here.

from abc import ABC, abstractmethod
from .gen import FieldGen
import re

from jinja2 import Environment
from jinja2 import FileSystemLoader
import os
import shutil


def gnd_mod(mod , dir_path , dir , j2file , file ):
    j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % dir_path ),trim_blocks=True)
    template = j2_env.get_template('tpl/%s.j2' % j2file )
    rendered_file = template.render({ 'APP' : mod , 'Title' : mod.get_form_name_capital() })
    return { 'file' :   '%s/%s' % ( dir, file ) , 'render' : rendered_file , 'new_name' :  mod.get_form_name() }


def gnd(mod):
    render = { 'form' : '' , 'models' : '' , 'urls' : '' , 'render' : '' }
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_root = '%s/tmp/%s' % ( dir_path , 'General' )
    dir_array = ['migrations' , 'templatetags' , 'templates' , 'templates/TPL' , 'templates/MODEL_TPL' , 'templates/Main' ]
    if not os.path.exists( dir_root ):
            os.makedirs( dir_root )
    for i in dir_array:
        if not os.path.exists( '%s/%s' %  ( dir_root , i ) ):
            os.makedirs(  '%s/%s' %  ( dir_root , i ) )
    render.update({ 'models' : gnd_mod(mod , dir_path ,  '%s/%s' %  ( dir_root , 'templates/TPL' ) ,  'models' , 'models.py' ) })
    render.update({ 'form' : gnd_mod(mod , dir_path ,  '%s/%s' %  ( dir_root , 'templates/TPL' ) ,  'form' , 'form.py' ) })
    render.update({ 'urls' : gnd_mod(mod , dir_path ,  '%s/%s' %  ( dir_root , 'templates/TPL' ) ,  'urls' , 'urls.py' ) })
    render.update({ 'views' : gnd_mod(mod , dir_path ,  '%s/%s' %  ( dir_root , 'templates/TPL' ) ,  'views' , 'views.py' ) })
    render.update({ 'render' : gnd_mod(mod , dir_path ,  '%s/%s' %  ( dir_root , 'templates/MODEL_TPL' ) ,  'models_html' , '%s.html' % mod.get_form_name() )  })
    return render




class Model_Types(models.Model):
    Name = models.CharField(max_length=255,unique=True)
    register = models.CharField(max_length=255,default="")
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
        return self.Name.lower().replace(' ','_').replace('-','_').replace('+','_')

    def get_form_choice(self,select=False,nice_name=False):
        ch = []
        cho = {}
        if select:
            select_to = ch
            cho = { 'select' : select , 'fields' : select_to , 'nice_name' : nice_name }
        if len(self.choices.all()) > 0 :
            for i in self.choices.all():
                if select:
                    field = i.Value
                else:
                    field = re.sub('^[0-9]+' , '' , i.Value.lower().replace(' ','').replace('+' , '').replace('-' , ''))
                ch.append({ 'field' :  field , 'verbose_name' : i.Value ,  'nice_name' : nice_name , 'extra' : i  })
            if select:
                cho['fields'] = ch
                return cho
            return ch
        if len(self.choices_price.all()) > 0 :
            for i in self.choices_price.all():
                if select:
                    field = i.Value
                else:
                    field = re.sub('^[0-9]+' , '' , i.Value.lower().replace(' ','').replace('+' , '').replace('-' , ''))
                ch.append({ 'field' : field , 'verbose_name' : i.Value ,  'nice_name' : nice_name  ,  'extra' : i })
            if select:
                cho['fields'] = ch
                return cho
            return ch
        return []

    def get_field(self,request=False,session=False,model_name=False,form_name=False):
        value = ''
        print('Inside Get Field' , self.get_field_name())
        sub = False
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
         sub_choices = []
         for i in self.choices_price.all():
            request.session['lookup_table'][model_name].update( { i.id : i.price } )
            if len(i.sub_choices.all()) > 0:
                request.session[form_name]['sub_%s' % model_name] = {'value': '', 'price': 0.0, 'total': 0}
                try:
                    request.session['lookup_table']['sub_%s' % model_name][i.id] = []
                except KeyError:
                    request.session['lookup_table']['sub_%s' % model_name] = {}
                    request.session['lookup_table']['sub_%s' % model_name][i.id] = []
                for z in i.sub_choices.all():
                    request.session['lookup_table']['sub_%s' % model_name][i.id].append( { z.id : z.Value } )
                    sub_choices.append(z)
                print(sub_choices)
         sub = { 'data' : sub_choices , 'name' : 'sub_%s' % model_name , 'value' : 0 , 'template' : 'ajaxcall/%s.html' % self.template }
         val = []
         for i in value:
             val.append(int(i))
         return { 'data' :  self.choices_price.all() , 'name' : model_name , 'value' : val , 'template' : 'ajaxcall/%s.html' % self.template , 'sub' : sub }
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
        return self.Name.lower().replace(' ','_').replace('-','_').replace('+','_')

    def get_field(self,request=False,session=False,model_name=False):
        value = self.value
        if len(session['value'].strip()) > 0 :
            value = session['value']
        return { 'data' :  self , 'name' : model_name , 'value' : value , 'template' : 'ajaxcall/Fields.html' , 'special' :self }
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
        return self.Name.lower().replace(' ','_').replace('-','_').replace('+','_')

    def get_model_name_print(self):
        print(self.Name.lower().replace(' ','_'))

    def valid_model(self):
        if self.number:
            return True
        if self.regular:
            return True
        if self.choices:
            return False

    def get_field_to_render(self):
        if self.number:
            return { 'item' : 'number' , 'field' : self.number }
        if self.regular:
            return  { 'item' : 'regular' , 'field' : self.regular }
        if self.choices:
            return  { 'item' : 'choices' , 'field' : self.choices }

    def valid_model_entery(self):
        if self.choices:
            if self.choices.template == 'checkbox':
                return self.choices.get_form_choice(nice_name=self.Name)
        if self.choices:
            if self.choices.template == 'radio' or self.choices.template == 'select':
                print('\n OK \n')
                return self.choices.get_form_choice(self.get_model_name(),self.Name)
        return False

    def valid_model_type(self):
        if self.number:
            return { 'Type' : 'number' , 'field' : True , 'Min' : self.number.min , 'Max' : self.number.max , 'Default' : self.number.default , 'price' : self.number.price , 'verbose_name' : self.number.Name ,  'nice_name' : self.number.Name }
        if self.regular:
            return { 'Type' : 'regular' , 'field' : True , 'mod' : self.regular.type.register ,  'verbose_name' : self.regular.Name ,  'nice_name' : self.regular.Name , 'widgets' : self.regular.type.Name }

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
                try:
                    request.session[Form_Name].update({ self.get_model_name() : { 'value' : '' , 'price' : 0 , 'total' : 0 } })
                except KeyError:
                    request.session[Form_Name] = {}
                    request.session[Form_Name].update({ self.get_model_name() : { 'value' : '' , 'price' : 0 , 'total' : 0 } })
                session = request.session[Form_Name][self.get_model_name()]
                context.update( self.choices.get_field(request,session,self.get_model_name(),Form_Name))
            return  mark_safe(render_to_string(context['template'] , context ))

    class Meta:
        verbose_name = 'All Fields'
        ordering = ['priority']

class AjaxForm_SUB(models.Model):
    Name = models.CharField(max_length=255,default="",)
    Field = models.ManyToManyField(Model_Inputs)
    expend_text = models.CharField(max_length=255,default="",)

    def get_form_name(self):
        return self.Name.lower().replace(' ','_')

    def get_form_name_capital(self):
        return self.Name.upper().replace(' ','_')

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
        verbose_name = 'Form Sub'

class AjaxForm(models.Model):
    Name = models.CharField(max_length=255)
    Field = models.ManyToManyField(Model_Inputs)
    SubForm = models.ManyToManyField(AjaxForm_SUB,blank=True)
    user_map = models.BooleanField(default=False)

    def get_form_name_capital(self):
        return self.Name.upper().replace(' ','_')

    def get_form_name(self):
        return self.Name.lower().replace(' ','_')

    def get_form_name_print(self):

        fgen = FieldGen(self)
        fgen.get_dict()
        fgen.create_app_dir()
        print(self.Name.lower().replace(' ','_'))

    def get_FieldGen(self):
        return gnd(self)

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
