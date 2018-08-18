# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-21 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbconnlab', '0007_auto_20180719_2120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderresults',
            options={'permissions': (('techval', 'Technical validating results'), ('medval', 'Medical validating result'), ('repeat', 'Repeating result'))},
        ),
        migrations.AlterField(
            model_name='historyorders',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='historyorder_test', to='bbconnlab.Tests', verbose_name='Tes'),
        ),
        migrations.AlterField(
            model_name='orderextended',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='bbconnlab.Orders'),
        ),
        migrations.AlterField(
            model_name='orderresults',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orderresults_test', to='bbconnlab.Tests', verbose_name='Tes'),
        ),
        migrations.AlterField(
            model_name='ordertests',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_tests', to='bbconnlab.Tests', verbose_name='Tes'),
        ),
        migrations.AlterField(
            model_name='results',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='results_order', to='bbconnlab.Orders', verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='results',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='results_test', to='bbconnlab.Tests', verbose_name='Tes'),
        ),
        migrations.AlterField(
            model_name='testparameters',
            name='test',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='bbconnlab.Tests'),
        ),
        migrations.AlterField(
            model_name='testprices',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bbconnlab.Priority', verbose_name='Prioritas'),
        ),
        migrations.AlterField(
            model_name='testprices',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='test_price', to='bbconnlab.Tests', verbose_name='Tes'),
        ),
        migrations.AlterField(
            model_name='testrefranges',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='refranges_test', to='bbconnlab.Tests', verbose_name='Tes'),
        ),
    ]
