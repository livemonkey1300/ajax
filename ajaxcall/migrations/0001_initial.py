# Generated by Django 2.1.5 on 2019-03-04 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model_Inputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, unique=True)),
                ('field_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('Attribute', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'All Fields',
            },
        ),
        migrations.CreateModel(
            name='Model_Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Types',
            },
        ),
        migrations.AddField(
            model_name='model_inputs',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ajaxcall.Model_Types'),
        ),
    ]
