# Generated by Django 2.1.5 on 2019-03-06 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxcall', '0013_auto_20190306_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_choices_price',
            name='sub_price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ajaxcall.Model_Number'),
        ),
    ]
