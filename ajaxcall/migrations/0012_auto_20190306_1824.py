# Generated by Django 2.1.5 on 2019-03-06 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxcall', '0011_auto_20190306_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model_Sub_Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Value', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'List Sub choice',
            },
        ),
        migrations.AddField(
            model_name='model_choices_price',
            name='sub_choices',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ajaxcall.Model_Sub_Choices'),
        ),
    ]