# Generated by Django 2.1.5 on 2019-03-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxcall', '0014_model_choices_price_sub_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_types',
            name='register',
            field=models.CharField(default='', max_length=255),
        ),
    ]
