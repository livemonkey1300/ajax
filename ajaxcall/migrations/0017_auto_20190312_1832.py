# Generated by Django 2.1.5 on 2019-03-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxcall', '0016_auto_20190312_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='ajaxform_sub',
            name='expend_text',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='ajaxform_sub',
            name='Name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
