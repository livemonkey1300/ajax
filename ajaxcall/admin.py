from django.contrib import admin

# Register your models here.
from .models import Model_Types , Model_Inputs , AjaxForm , Model_Number , Model_Regular , Model_Choices_Group , Model_Choices ,Model_Choices_price , Model_Sub_Choices , AjaxForm_SUB
from .gen import FieldGen_ALL , FieldGen_ALL_CMS

def Gen_APP(modeladmin, request, queryset):
    for entery in queryset:
        entery.get_form_name_print()
Gen_APP.short_description = "Generate App For Form"

def Gen_General(modeladmin, request, queryset):
    entrey_array = []
    for entery in queryset:
        entrey_array.append(entery.get_FieldGen())
    new_gen =  FieldGen_ALL(entrey_array)
    new_gen.create()
Gen_General.short_description = "Generate Central"

def Gen_General_CMS(modeladmin, request, queryset):
    entrey_array = []
    for entery in queryset:
        entrey_array.append(entery.get_FieldGen())
    new_gen =  FieldGen_ALL_CMS(entrey_array)
    new_gen.create()
Gen_General_CMS.short_description = "Generate Central CMS"

class ChoiceInline(admin.TabularInline):
    model = Model_Inputs
    extra = 0

class ChoiceRegular(admin.TabularInline):
    model = Model_Inputs
    extra = 0
    fields = ('Name', 'regular')


class ChoiceInlineNumber(admin.TabularInline):
    model = Model_Inputs
    extra = 0
    fields = ('Name', 'number')

class ChoiceInline_Choice(admin.TabularInline):
    model = Model_Inputs
    extra = 0
    fields = ('Name', 'choices')


class ChoiceNumber_Choice(admin.TabularInline):
    model = Model_Choices_Group.choices_price.through
    extra = 0
    verbose_name = 'Price Choice'
    verbose_name_plural = 'Price Choices'

class ChoiceChoice_Choice(admin.TabularInline):
    model = Model_Choices_Group.choices.through
    extra = 0
    verbose_name = 'Choice'
    verbose_name_plural = 'Choices'

class Field_Selection_Choice(admin.TabularInline):
    model = AjaxForm.Field.through
    extra = 0
    verbose_name = 'Choices'
    verbose_name_plural = 'Choicess'



class Model_InputAdmin(admin.ModelAdmin):
    model = Model_Inputs
    fieldsets = [
        ('Name',               {'fields': ['Name']}),
        ('Priority', {'fields': ['priority'], 'classes': ['wide']}),
    ]

class Model_NumberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Name','template']}),
        ('Attributes', {'fields': ['min','max','default','step'], 'classes': ['wide']}),
        ('Price', {'fields': ['price_calculate','price'], 'classes': ['wide']}),
    ]
    inlines = [ChoiceInlineNumber]

class Model_RegularAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Name' , 'type' , 'value' ]}),
    ]
    inlines = [ChoiceRegular]

class Model_Choices_GroupAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline_Choice,ChoiceNumber_Choice,ChoiceChoice_Choice]
    fieldsets = [
        ('Name',               {'fields': ['Name','template']}),
        # ('Choices', {'fields': ['choices'], 'classes': ['collapse']}),
        # ('Choices With Price', {'fields': ['choices_price'], 'classes': ['collapse']}),
    ]
    # filter_horizontal = ('choices','choices_price',)

class Field_Selection_price_Choice(admin.TabularInline):
    model = Model_Choices_price.sub_choices.through
    extra = 0
    verbose_name = 'Choices'
    verbose_name_plural = 'Choicess'

class AjaxForm_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['Name','SubForm','user_map']}),
        # ('Field', {'fields': ['Field'], 'classes': ['wide']}),
    ]
    filter_horizontal = ('SubForm',)
    inlines = [Field_Selection_Choice]
    actions = [Gen_APP,Gen_General,Gen_General_CMS]

class SUBForm_Admin(admin.ModelAdmin):
    filter_horizontal = ('Field',)

class Model_Sub_Choices_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['Value' , 'price','sub_price' ]}),
        # ('Field', {'fields': ['Field'], 'classes': ['wide']}),
    ]
    filter_horizontal = ('sub_choices',)
    inlines = [Field_Selection_price_Choice]

class HiddenModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, *args, **kwargs):
        perms = admin.ModelAdmin.get_model_perms(self, *args, **kwargs)
        perms['list_hide'] = True
        return perms

admin.site.register(Model_Number,Model_NumberAdmin)
admin.site.register(Model_Inputs,Model_InputAdmin)
admin.site.register(Model_Regular,Model_RegularAdmin)
admin.site.register(Model_Choices_Group,Model_Choices_GroupAdmin)
admin.site.register(Model_Choices)
admin.site.register(Model_Choices_price,Model_Sub_Choices_Admin)
admin.site.register(Model_Sub_Choices)
admin.site.register(AjaxForm_SUB,SUBForm_Admin)
admin.site.register(AjaxForm,AjaxForm_Admin)
