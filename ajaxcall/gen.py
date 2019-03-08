from jinja2 import Environment
from jinja2 import FileSystemLoader
import os
class FieldGen:
    def __init__(self,Form):
        self.Form = Form
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.fields = []
        self.models = []
        self.get_field()

    def get_dict(self):
        print(dir(self.Form))

    def get_field(self):
        for i in self.Form.Field.all():
            print(i)
            if i.valid_model():
                self.fields.append({ 'Name' : i.get_model_name() , 'model' : i.valid_model_type() })
            else:
                self.models.append({ 'Name' : i.get_model_name() , 'Choice' : i.valid_model_entery() })

    def gen_model(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('models.j2')
        rendered_file = template.render({ 'APP' : self.Form.get_form_name() , 'APP_NAME' : self.Form.Name , 'fields' : self.fields , 'models' : self.models })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.Form.get_form_name() , 'models.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_model_admin(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('admin.j2')
        rendered_file = template.render({ 'APP' : self.Form.get_form_name() , 'APP_NAME' : self.Form.Name , 'fields' : self.fields , 'models' : self.models })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.Form.get_form_name() , 'admin.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_model_url(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('urls.j2')
        rendered_file = template.render({ 'APP' : self.Form.get_form_name() , 'APP_NAME' : self.Form.Name , 'fields' : self.fields , 'models' : self.models })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.Form.get_form_name() , 'urls.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_model_views(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('views.j2')
        rendered_file = template.render({ 'APP' : self.Form.get_form_name() , 'APP_NAME' : self.Form.Name , 'fields' : self.fields , 'models' : self.models })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.Form.get_form_name() , 'views.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_model_forms(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('forms.j2')
        rendered_file = template.render({ 'APP' : self.Form.get_form_name() , 'APP_NAME' : self.Form.Name , 'fields' : self.fields , 'models' : self.models })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.Form.get_form_name() , 'forms.py' )  , "w") as fh:
                fh.write(rendered_file)


    def create_app_dir(self):
        if not os.path.exists('%s/tmp/%s' % ( self.dir_path , self.Form.get_form_name() )):
            os.makedirs( '%s/tmp/%s' % ( self.dir_path , self.Form.get_form_name()))
        self.gen_model()
        self.gen_model_admin()
        self.gen_model_url()
        self.gen_model_views()
        self.gen_model_forms()
