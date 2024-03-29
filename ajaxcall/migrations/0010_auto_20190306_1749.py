# Generated by Django 2.1.5 on 2019-03-06 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxcall', '0009_model_number_template'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ajaxform',
            options={'verbose_name': 'Form'},
        ),
        migrations.AlterModelOptions(
            name='model_choices',
            options={'verbose_name': 'List choice'},
        ),
        migrations.AlterModelOptions(
            name='model_choices_group',
            options={'verbose_name': 'Choices Group'},
        ),
        migrations.AlterModelOptions(
            name='model_choices_price',
            options={'verbose_name': 'List choices with price'},
        ),
        migrations.AddField(
            model_name='model_inputs',
            name='property',
            field=models.IntegerField(default=1),
        ),
    ]
