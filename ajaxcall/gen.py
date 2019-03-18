from jinja2 import Environment
from jinja2 import FileSystemLoader
import os
import shutil

class FieldGen:
    def __init__(self,Form):
        self.Form = Form
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.fields = []
        self.models = []
        self.user_map = self.Form.user_map
        self.get_field()

    def get_dict(self):
        print(dir(self.Form))

    def get_field(self):
        for i in self.Form.Field.all():
            print(i)
            if i.valid_model():
                self.fields.append({ 'Name' : i.get_model_name() , 'model' : i.valid_model_type() })
            else:
                self.models.append({ 'Name' : i.get_model_name() , 'Choice' : i.valid_model_entery() , 'verbose_name' : i.Name ,  'nice_name' : i.Name  })

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

    def gen_model_main(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('Main_HTML.j2')
        rendered_file = template.render({ 'APP' : self.Form.get_form_name() , 'APP_NAME' : self.Form.Name , 'fields' : self.fields , 'models' : self.models })
        return rendered_file

    def gen_model_form_html(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('Form_HTML.j2')
        rendered_file = template.render({ 'APP' : self.Form.get_form_name() , 'APP_NAME' : self.Form.Name , 'fields' : self.fields , 'models' : self.models })
        return rendered_file

    def gen_model_json(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('json_import.j2')
        rendered_file = template.render({ 'APP' : self.Form.get_form_name() , 'APP_NAME' : self.Form.Name , 'fields' : self.fields , 'models' : self.models })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.Form.get_form_name() , 'json_import.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_templates(self):
        blank = ''
        path1 = '%s/tmp/%s/%s' % ( self.dir_path , self.Form.get_form_name() , 'templates')
        path2 = '%s/%s' % ( path1 ,  self.Form.get_form_name() )
        if not os.path.exists(path1):
            os.makedirs(path1)
        if not os.path.exists(path2):
            os.makedirs(path2)
        with open('%s/%s' % ( path2 ,'Main.html') , "w") as fh:
            fh.write(self.gen_model_main())
        with open('%s/%s' % ( path2 ,'form.html') , "w") as fh:
            fh.write(self.gen_model_form_html())

    def create_app_dir(self):
        if not os.path.exists('%s/tmp/%s' % ( self.dir_path , self.Form.get_form_name() )):
            os.makedirs( '%s/tmp/%s' % ( self.dir_path , self.Form.get_form_name()))
        self.gen_model()
        self.gen_model_admin()
        self.gen_model_url()
        self.gen_model_views()
        self.gen_model_forms()
        self.gen_templates()
        self.gen_model_json()




class FieldGen_ALL:
    def __init__(self,Form=[],name='General'):
        self.name = name
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.Form = Form
        self.Forms = {}
        self.init_Forms()

    def init_Forms(self):
        for i in self.Form:
            for key , val in i.items():
                try:
                    self.Forms[key].append( val )
                except KeyError:
                    self.Forms[key] = [val]
        self.gen_model()
        self.gen_urls()
        self.gen_views()
        self.get_rendered_template()

    def gen_model(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general/models.j2')
        rendered_file = template.render({ 'APP' : self.name , 'models' : self.Forms['models'] , 'APPS' : self.name  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'models.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_urls(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general/urls.j2')
        rendered_file = template.render({ 'APP' : self.name , 'urls' : self.Forms['urls'] , 'APPS' : self.name  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'urls.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_views(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general/views.j2')
        rendered_file = template.render({ 'APP' : self.name , 'views' : self.Forms['views'] , 'APPS' : self.name  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'views.py' )  , "w") as fh:
                fh.write(rendered_file)

    def get_rendered_template(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general/model_html_template.j2')
        path1 = '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'templates')
        path2 = '%s/%s/MODEL_TPL' % ( path1 ,  self.name )
        for i in self.Forms['render']:
            if not os.path.exists( path2 ):
                os.makedirs( path2 )
            with open( '%s/%s' % ( path2 , '%s.html' % i['new_name'])  , "w") as fh:
                    fh.write(i['render'])
        # j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        # template = j2_env.get_template('general/models.j2')
        # rendered_file = template.render({ 'APP' : self.name , 'models' : self.Forms['models'] , 'APPS' : self.name  })
        # with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'models.py' )  , "w") as fh:
        #         fh.write(rendered_file)

    # def create(self):
    #     for i in self.Form :
    #         i.create_app_dir()
    #
    # def create_app_dir(self):
    #     if not os.path.exists('%s/tmp/%s' % ( self.dir_path , self.name )):
    #         os.makedirs( '%s/tmp/%s' % ( self.dir_path , self.name ))
    #     if not os.path.exists('%s/tmp/%s/migrations' % ( self.dir_path , self.name )):
    #         os.makedirs( '%s/tmp/%s/migrations' % ( self.dir_path , self.name ))
    #     self.gen_model()
    #     self.gen_model_admin()
    #     self.gen_model_url()
    #     self.gen_model_views()
    #     self.gen_model_forms()
    #     self.gen_templates()
    #     self.gen_model_json()
    #     self.get_rendered_template()
    #     self.gen_model_accounts()
    #     self.gen_apps()
    #     self.gen_test()
    #     self.gen_menu_tag()
    #     self.gen_app_init()
    #     self.gen_config_doc()
    #     self.gen_kickstart()
    #     self.gen_zip_file()
    #
    #
    # def gen_zip_file(self):
    #     shutil.make_archive('%s/tmp/%s' % ( self.dir_path , self.name ) , 'zip', '%s/tmp/%s' % ( self.dir_path , self.name ))
    #
    # def gen_model(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/models.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'models.py' )  , "w") as fh:
    #             fh.write(rendered_file)
    #
    # def gen_config_doc(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/models.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'models.py' )  , "w") as fh:
    #             fh.write(rendered_file)
    #
    # def gen_model_admin(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/doc.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'doc.txt' )  , "w") as fh:
    #             fh.write(rendered_file)
    #
    # def gen_model_url(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/urls.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'urls.py' )  , "w") as fh:
    #             fh.write(rendered_file)
    #
    # def gen_model_views(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/views.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'views.py' )  , "w") as fh:
    #             fh.write(rendered_file)
    #
    # def gen_model_forms(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/forms.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'forms.py' )  , "w") as fh:
    #             fh.write(rendered_file)
    #
    # def gen_model_accounts(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/accounts.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'accounts.py' )  , "w") as fh:
    #             fh.write(rendered_file)
    #
    # def gen_model_main(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/Main_HTML.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     return rendered_file
    #
    # def gen_model_menu_html(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/Menu_HTML.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     return rendered_file
    #
    #
    # def gen_model_mail_html(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/Menu_HTML.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     return rendered_file
    #
    # def gen_model_form_html(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/Form_HTML.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     return rendered_file
    #
    # def gen_model_json(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/json_import.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'json_import.py' )  , "w") as fh:
    #             fh.write(rendered_file)
    #
    # def gen_test(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/tests.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'tests.py' )  , "w") as fh:
    #             fh.write(rendered_file)
    #
    # def gen_app_init(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/__init__.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , '__init__.py' )  , "w") as fh:
    #             fh.write(rendered_file)
    #     with open( '%s/tmp/%s/migrations/%s' % ( self.dir_path , self.name , '__init__.py' )  , "w") as fh:
    #             fh.write(rendered_file)
    #     with open( '%s/tmp/%s/templatetags/%s' % ( self.dir_path , self.name , '__init__.py' )  , "w") as fh:
    #             fh.write(rendered_file)
    #
    # def gen_kickstart(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('kickstart.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     with open( '%s/tmp/%s' % ( self.dir_path , 'kickstart.sh' )  , "w") as fh:
    #             fh.write(rendered_file)
    #
    # def gen_apps(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/apps.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'apps.py' )  , "w") as fh:
    #             fh.write(rendered_file)
    #
    # def gen_menu_tag(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/menu_tag.j2')
    #     rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
    #     with open( '%s/tmp/%s/templatetags/%s' % ( self.dir_path , self.name , 'menu_tags.py' )  , "w") as fh:
    #             fh.write(rendered_file)
    #
    # def get_rendered_template(self):
    #     j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
    #     template = j2_env.get_template('general/model_html_template.j2')
    #     path1 = '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'templates')
    #     path2 = '%s/%s' % ( path1 ,  self.name )
    #     for key , value in self.Forms.items():
    #         rendered_file = template.render({ 'values' : value , 'APP' : key })
    #         with open('%s/%s' % ( path2 ,'%s.html' % key ) , "w") as fh:
    #             fh.write(rendered_file)
    #
    # def gen_templates(self):
    #     blank = ''
    #     path1 = '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'templates')
    #     path3 = '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'templatetags')
    #     path2 = '%s/%s' % ( path1 ,  self.name )
    #     if not os.path.exists(path1):
    #         os.makedirs(path1)
    #     if not os.path.exists(path2):
    #         os.makedirs(path2)
    #     if not os.path.exists(path3):
    #         os.makedirs(path3)
    #     with open('%s/%s' % ( path2 ,'Main.html') , "w") as fh:
    #         fh.write(self.gen_model_main())
    #     with open('%s/%s' % ( path2 ,'form.html') , "w") as fh:
    #         fh.write(self.gen_model_form_html())
    #     with open('%s/%s' % ( path2 ,'Menu.html') , "w") as fh:
    #         fh.write(self.gen_model_menu_html())


class FieldGen_ALL_CMS:
    def __init__(self,Form=[]):
        self.name = 'General_CMS'
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.Form = Form
        self.Forms = {}
        self.init_Forms()
        self.create_app_dir()

    def init_Forms(self):
        for i in self.Form :
            self.Forms[i.Form.get_form_name()] = { 'models' : i.models , 'fields' :  i.fields , 'user_map' : i.user_map }
        print(self.Forms)

    def create(self):
        for i in self.Form :
            i.create_app_dir()

    def create_app_dir(self):
        if not os.path.exists('%s/tmp/%s' % ( self.dir_path , self.name )):
            os.makedirs( '%s/tmp/%s' % ( self.dir_path , self.name ))
        self.gen_model()
        self.gen_model_admin()
        self.gen_model_url()
        self.gen_model_views()
        self.gen_model_forms()
        self.gen_templates()
        self.gen_model_json()
        self.get_rendered_template()
        self.gen_model_plugin()

    def gen_model(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general_CMS/models.j2')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'models.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_model_admin(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general_CMS/admin.j2')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'admin.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_model_url(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general_CMS/urls.j2')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'urls.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_model_views(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general_CMS/views.j2')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'views.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_model_forms(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general_CMS/forms.j2')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'forms.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_model_main(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general_CMS/Main_HTML.j2')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        return rendered_file

    def gen_model_form_html(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general_CMS/Form_HTML.j2')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        return rendered_file

    def gen_model_menu_html(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general_CMS/Form_HTML.j2')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        return rendered_file

    def gen_model_json(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general_CMS/json_import.j2')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'json_import.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_model_plugin(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general_CMS/cms_plugins.j2')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'cms_plugins.py' )  , "w") as fh:
                fh.write(rendered_file)

    def get_rendered_template(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general_CMS/model_html_template.j2')
        path1 = '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'templates')
        path2 = '%s/%s' % ( path1 ,  self.name )
        for key , value in self.Forms.items():
            rendered_file = template.render({ 'values' : value , 'APP' : key })
            with open('%s/%s' % ( path2 ,'%s.html' % key ) , "w") as fh:
                fh.write(rendered_file)

    def gen_templates(self):
        blank = ''
        path1 = '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'templates')
        path2 = '%s/%s' % ( path1 ,  self.name )
        if not os.path.exists(path1):
            os.makedirs(path1)
        if not os.path.exists(path2):
            os.makedirs(path2)
        with open('%s/%s' % ( path2 ,'Main.html') , "w") as fh:
            fh.write(self.gen_model_main())
        with open('%s/%s' % ( path2 ,'form.html') , "w") as fh:
            fh.write(self.gen_model_form_html())
