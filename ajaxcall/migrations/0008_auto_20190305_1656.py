# Generated by Django 2.1.5 on 2019-03-05 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxcall', '0007_model_inputs_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_choices_group',
            name='choices',
            field=models.ManyToManyField(blank=True, to='ajaxcall.Model_Choices'),
        ),
        migrations.AlterField(
            model_name='model_choices_group',
            name='choices_price',
            field=models.ManyToManyField(blank=True, to='ajaxcall.Model_Choices_price'),
        ),
    ]
