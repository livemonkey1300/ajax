# Generated by Django 2.1.5 on 2019-03-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxcall', '0018_ajaxform_user_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ajaxform',
            name='SubForm',
            field=models.ManyToManyField(blank=True, to='ajaxcall.AjaxForm_SUB'),
        ),
    ]
