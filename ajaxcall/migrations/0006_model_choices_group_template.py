# Generated by Django 2.1.5 on 2019-03-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxcall', '0005_auto_20190305_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_choices_group',
            name='template',
            field=models.CharField(choices=[('checkbox', 'checkbox'), ('radio', 'radio'), ('select', 'select')], default='select', max_length=255),
        ),
    ]
