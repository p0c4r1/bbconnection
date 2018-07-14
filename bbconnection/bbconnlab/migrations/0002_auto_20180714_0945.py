# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-14 02:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bbconnlab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_code', models.CharField(max_length=20, null=True, verbose_name='Action code')),
                ('action_user', models.CharField(max_length=20, null=True, verbose_name='Action by')),
                ('action_date', models.DateTimeField(null=True, verbose_name='Action date')),
                ('action_text', models.CharField(max_length=1000, null=True, verbose_name='Action text')),
                ('lastmodification', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Last modified')),
                ('lastmodifiedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Code')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('active', models.BooleanField(default=True, verbose_name='Active?')),
                ('input_path', models.CharField(max_length=100, verbose_name='input path')),
                ('lastmodification', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Last modified')),
                ('lastmodifiedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentFlags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag_code', models.CharField(max_length=100, verbose_name='Host flag code')),
                ('flag_description', models.CharField(max_length=100, verbose_name='Host flag description')),
                ('flag_mark', models.CharField(blank=True, max_length=100, null=True, verbose_name='Host flag mark')),
                ('lastmodification', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Last modified')),
            ],
        ),
        migrations.CreateModel(
            name='Instruments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Code')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('active', models.BooleanField(default=True, verbose_name='Active?')),
                ('driver', models.CharField(blank=True, max_length=100, null=True, verbose_name='Driver name')),
                ('connection_type', models.CharField(blank=True, choices=[('SER', 'Serial'), ('TCP', 'TCP/IP')], max_length=3, null=True, verbose_name='Connection type')),
                ('serial_port', models.CharField(blank=True, choices=[('COM1', 'COM1'), ('COM2', 'COM2'), ('COM3', 'COM3'), ('COM4', 'COM4'), ('COM5', 'COM5'), ('COM6', 'COM6'), ('COM7', 'COM7'), ('COM8', 'COM8'), ('COM9', 'COM9'), ('COM10', 'COM10'), ('COM11', 'COM11'), ('COM12', 'COM12'), ('COM13', 'COM13'), ('COM14', 'COM14'), ('COM15', 'COM15'), ('COM16', 'COM16'), ('COM17', 'COM17'), ('COM18', 'COM18'), ('COM19', 'COM19'), ('COM20', 'COM20'), ('COM21', 'COM21'), ('COM22', 'COM22'), ('COM23', 'COM23'), ('COM24', 'COM24'), ('COM25', 'COM25'), ('COM26', 'COM26'), ('COM27', 'COM27'), ('COM28', 'COM28'), ('COM29', 'COM29'), ('COM30', 'COM30'), ('COM31', 'COM31'), ('COM32', 'COM32'), ('COM33', 'COM33'), ('COM34', 'COM34'), ('COM35', 'COM35'), ('COM36', 'COM36'), ('COM37', 'COM37'), ('COM38', 'COM38'), ('COM39', 'COM39'), ('COM40', 'COM40')], max_length=3, null=True, verbose_name='Serial port name')),
                ('serial_baud_rate', models.CharField(blank=True, choices=[('9600', '9600'), ('19200', '19200')], max_length=3, null=True, verbose_name='Serial baud rate')),
                ('serial_stop_bit', models.CharField(blank=True, choices=[('1', '1'), ('2', '2')], max_length=3, null=True, verbose_name='Serial stop bit')),
                ('serial_data_bit', models.CharField(blank=True, choices=[('N', 'None'), ('E', 'Even')], max_length=3, null=True, verbose_name='Serial parity')),
                ('tcp_conn_type', models.CharField(blank=True, choices=[('S', 'Server'), ('C', 'Client')], max_length=3, null=True, verbose_name='TCP/IP Connection type')),
                ('tcp_host', models.GenericIPAddressField(blank=True, null=True, verbose_name='TCP Host name (IP Address)')),
                ('tcp_port', models.IntegerField(blank=True, null=True, verbose_name='TCP Port')),
                ('lastmodification', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Last modified')),
                ('lastmodifiedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentTests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_code', models.CharField(max_length=100, verbose_name='Host test code')),
                ('result_type', models.CharField(choices=[('R', 'RAW'), ('N', 'NUMBERIC'), ('A', 'ALFANUMERIC')], default='R', max_length=3, verbose_name='Result type')),
                ('lastmodification', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Last modified')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='instrumentflags_instrument', to='bbconnlab.Instruments', verbose_name='Instrument')),
                ('lastmodifiedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
        ),
        migrations.CreateModel(
            name='OrderExtended',
            fields=[
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bbconnlab.Orders')),
                ('result_pdf_url', models.CharField(max_length=500, null=True, verbose_name='Result PDF url')),
                ('lastmodification', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Last modified')),
                ('lastmodifiedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
        ),
        migrations.CreateModel(
            name='OrderResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_header', models.BooleanField(default=False, verbose_name='is header?')),
                ('unit', models.CharField(max_length=100, null=True, verbose_name='Result unit')),
                ('ref_range', models.CharField(max_length=200, null=True, verbose_name='Reference range')),
                ('patologi_mark', models.CharField(max_length=20, null=True, verbose_name='Patologi mark')),
                ('validation_status', models.IntegerField(default=0, verbose_name='Validation status')),
                ('techval_user', models.CharField(max_length=20, null=True, verbose_name='Techical validated by')),
                ('techval_date', models.DateTimeField(null=True, verbose_name='Technical Validated date')),
                ('medval_user', models.CharField(max_length=20, null=True, verbose_name='Medical validated by')),
                ('medval_date', models.DateTimeField(null=True, verbose_name='Medical validated date')),
                ('print_status', models.IntegerField(default=0, verbose_name='Print status')),
                ('print_user', models.CharField(max_length=20, null=True, verbose_name='Print by')),
                ('print_date', models.DateTimeField(null=True, verbose_name='Print date')),
                ('lastmodification', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Last modified')),
                ('lastmodifiedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderresults_order', to='bbconnlab.Orders', verbose_name='Order')),
            ],
        ),
        migrations.CreateModel(
            name='ReceivedSamples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastmodification', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Last modified')),
                ('lastmodifiedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receivedsamples_order', to='bbconnlab.Orders', verbose_name='Order')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receivedsamples_tube', to='bbconnlab.OrderSamples', verbose_name='Specimen')),
                ('supergroup', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receivedsamples_supergrup', to='bbconnlab.SuperGroups', verbose_name='Super Group')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeric_result', models.FloatField(null=True, verbose_name='Numeric result')),
                ('alfa_result', models.CharField(max_length=100, null=True, verbose_name='Alfanumeric result')),
                ('text_result', models.TextField(null=True, verbose_name='Text result')),
                ('image_result', models.BinaryField(null=True, verbose_name='Image result')),
                ('ref_range', models.CharField(max_length=100, null=True, verbose_name='Reference range')),
                ('mark', models.CharField(max_length=3, null=True, verbose_name='Result mark')),
                ('lastmodification', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Last modified')),
                ('flag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='results_instrumentflag', to='bbconnlab.InstrumentFlags', verbose_name='Instrument flag')),
                ('instrument', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='results_instrument', to='bbconnlab.Instruments', verbose_name='Instrument')),
                ('lastmodifiedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='results_order', to='bbconnlab.Orders', verbose_name='Order')),
            ],
        ),
        migrations.CreateModel(
            name='TestParameters',
            fields=[
                ('test', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bbconnlab.Tests')),
                ('method', models.CharField(blank=True, max_length=100, null=True, verbose_name='Method')),
                ('unit', models.CharField(blank=True, max_length=100, null=True, verbose_name='Test unit')),
                ('decimal_place', models.IntegerField(default=1, null=True, verbose_name='Decimal place')),
                ('special_information', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Special information')),
                ('lastmodification', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Last modified')),
                ('lastmodifiedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
        ),
        migrations.CreateModel(
            name='TestRefRanges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_from', models.IntegerField(blank=True, null=True, verbose_name='Age from')),
                ('age_from_type', models.CharField(blank=True, choices=[('D', 'DAY'), ('M', 'MONTH'), ('Y', 'YEAR')], max_length=3, null=True, verbose_name='Age from unit')),
                ('age_to', models.IntegerField(blank=True, null=True, verbose_name='Age to')),
                ('age_to_type', models.CharField(blank=True, choices=[('D', 'DAY'), ('M', 'MONTH'), ('Y', 'YEAR')], max_length=3, null=True, verbose_name='Age to unit')),
                ('operator', models.CharField(blank=True, choices=[('-', 'NA'), ('>', 'GT'), ('>=', 'GTE'), ('<', 'LT'), ('<=', 'LTE')], max_length=3, null=True, verbose_name='Operator')),
                ('any_age', models.BooleanField(default=True, verbose_name='Any age?')),
                ('lower', models.IntegerField(blank=True, null=True, verbose_name='lower limit')),
                ('upper', models.IntegerField(blank=True, null=True, verbose_name='upper limit')),
                ('operator_value', models.IntegerField(blank=True, null=True, verbose_name='operator value')),
                ('alfa_value', models.CharField(blank=True, max_length=100, null=True, verbose_name='Alfanumberic value')),
                ('special_info', models.TextField(blank=True, null=True, verbose_name='Special information')),
                ('lastmodification', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Last modified')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='refranges_gender', to='bbconnlab.Genders', verbose_name='Gender')),
                ('lastmodifiedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='refranges_test', to='bbconnlab.Tests', verbose_name='Test')),
            ],
        ),
        migrations.AddField(
            model_name='results',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='results_test', to='bbconnlab.Tests', verbose_name='Test'),
        ),
        migrations.AddField(
            model_name='orderresults',
            name='result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orderresults_result', to='bbconnlab.Results', verbose_name='Result'),
        ),
        migrations.AddField(
            model_name='orderresults',
            name='sample',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sampleresults_order', to='bbconnlab.OrderSamples', verbose_name='Order Sample'),
        ),
        migrations.AddField(
            model_name='orderresults',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderresults_test', to='bbconnlab.Tests', verbose_name='Test'),
        ),
        migrations.AddField(
            model_name='instrumenttests',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='instrumentflags_test', to='bbconnlab.Tests', verbose_name='Test'),
        ),
        migrations.AddField(
            model_name='instrumentflags',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='instrumenttests_instrument', to='bbconnlab.Instruments', verbose_name='Instrument'),
        ),
        migrations.AddField(
            model_name='instrumentflags',
            name='lastmodifiedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='historyorders',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='historyorder_order', to='bbconnlab.Orders', verbose_name='Order'),
        ),
        migrations.AddField(
            model_name='historyorders',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='historyorder_test', to='bbconnlab.Tests', verbose_name='Test'),
        ),
    ]