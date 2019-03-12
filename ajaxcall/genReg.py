
class FieldGen_ALL:
    def __init__(self,Form=[]):
        self.name = 'General'
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.Form = Form
        self.Forms = {}
        self.init_Forms()
        self.create_app_dir()

    def init_Forms(self):
        for i in self.Form :
            self.Forms[i.Form.get_form_name()] = { 'models' : i.models , 'fields' :  i.fields }

    def create(self):
        for i in self.Form :
            i.create_app_dir()

    def create_app_dir(self):
        if not os.path.exists('%s/tmp/%s' % ( self.dir_path , self.name )):
            os.makedirs( '%s/tmp/%s' % ( self.dir_path , self.name ))

    def gen_model(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general/')')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'models.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_model_admin(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general/')')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'admin.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_model_url(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general/')')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'urls.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_model_views(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general/')')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'views.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_model_forms(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general/')')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'forms.py' )  , "w") as fh:
                fh.write(rendered_file)

    def gen_model_main(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general/')')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        return rendered_file

    def gen_model_form_html(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general/')')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        return rendered_file

    def gen_model_json(self):
        j2_env = Environment(loader=FileSystemLoader('%s/generator_engine' % self.dir_path  ),trim_blocks=True)
        template = j2_env.get_template('general/')')
        rendered_file = template.render({ 'APP' : self.name , 'APPS' :self.Forms  })
        with open( '%s/tmp/%s/%s' % ( self.dir_path , self.name , 'json_import.py' )  , "w") as fh:
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
