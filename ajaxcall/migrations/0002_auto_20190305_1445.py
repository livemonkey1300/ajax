# Generated by Django 2.1.5 on 2019-03-05 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxcall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AjaxForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Model_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('min', models.IntegerField(default=1)),
                ('max', models.IntegerField(default=1)),
                ('default', models.IntegerField(default=1)),
                ('step', models.IntegerField(default=1)),
                ('price_calculate', models.BooleanField(default=True)),
                ('price', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Number',
            },
        ),
        migrations.CreateModel(
            name='Model_Regular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ajaxcall.Model_Types')),
            ],
            options={
                'verbose_name': 'Regular',
            },
        ),
        migrations.RemoveField(
            model_name='model_inputs',
            name='Attribute',
        ),
        migrations.RemoveField(
            model_name='model_inputs',
            name='field_Name',
        ),
        migrations.RemoveField(
            model_name='model_inputs',
            name='type',
        ),
        migrations.RemoveField(
            model_name='model_inputs',
            name='value',
        ),
        migrations.AlterField(
            model_name='model_inputs',
            name='Name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ajaxform',
            name='Field',
            field=models.ManyToManyField(to='ajaxcall.Model_Inputs'),
        ),
        migrations.AddField(
            model_name='model_inputs',
            name='number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ajaxcall.Model_Number'),
        ),
        migrations.AddField(
            model_name='model_inputs',
            name='regular',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ajaxcall.Model_Regular'),
        ),
    ]
