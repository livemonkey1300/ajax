# Generated by Django 2.1.5 on 2019-03-11 15:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virtual_machine', '0002_auto_20190307_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='VIRTUAL_MACHINE_QUOTE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('virtual_machine_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('network_throughput', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('datacenter', models.CharField(choices=[('Canada/Eastern', 'Canada/Eastern'), ('Vancouver, BC', 'Vancouver, BC'), ('Los Angeles, CA', 'Los Angeles, CA'), ('Brasilia, Brasil', 'Brasilia, Brasil'), ('Ottawa, ON', 'Ottawa, ON'), ('Miami, FL', 'Miami, FL'), ('Paris, France', 'Paris, France'), ('Mexico City, MX', 'Mexico City, MX'), ('Miami 3', 'Miami 3')], default='Canada/Eastern', max_length=255)),
                ('operating_system', models.CharField(choices=[('CentOS', 'CentOS'), ('Windows Server', 'Windows Server'), ('Ubuntu', 'Ubuntu'), ('Debian', 'Debian'), ('SUSE Linux', 'SUSE Linux'), ('OpenSUSE', 'OpenSUSE'), ('sense', 'sense')], default='CentOS', max_length=255)),
                ('system_disk', models.CharField(choices=[('HDD SAS Disk', 'HDD SAS Disk'), ('SSD ENT Disk', 'SSD ENT Disk')], default='HDD SAS Disk', max_length=255)),
                ('data_disk', models.CharField(choices=[('HDD SAS Disk', 'HDD SAS Disk'), ('SSD ENT Disk', 'SSD ENT Disk')], default='HDD SAS Disk', max_length=255)),
                ('memory', models.CharField(choices=[('2 GB', '2 GB'), ('4 GB', '4 GB'), ('6 GB', '6 GB')], default='2 GB', max_length=255)),
                ('vcpu', models.CharField(choices=[('2 GB', '2 GB'), ('90 GB', '90 GB')], default='2 GB', max_length=255)),
            ],
            options={
                'verbose_name': 'Virtual Machine QUOTE',
            },
        ),
        migrations.RemoveField(
            model_name='virtual_machineapp',
            name='applications',
        ),
        migrations.RemoveField(
            model_name='virtual_machineapp',
            name='fully_managed',
        ),
        migrations.AlterModelOptions(
            name='applications',
            options={'verbose_name': 'Applications'},
        ),
        migrations.AlterModelOptions(
            name='fully_managed',
            options={'verbose_name': 'Fully Managed'},
        ),
        migrations.DeleteModel(
            name='VIRTUAL_MACHINEAPP',
        ),
        migrations.AddField(
            model_name='virtual_machine_quote',
            name='applications',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='virtual_machine.APPLICATIONS'),
        ),
        migrations.AddField(
            model_name='virtual_machine_quote',
            name='fully_managed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='virtual_machine.FULLY_MANAGED'),
        ),
    ]
