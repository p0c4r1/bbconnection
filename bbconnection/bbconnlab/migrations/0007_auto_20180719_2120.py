# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-19 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbconnlab', '0006_auto_20180719_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderresults',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderresults_test', to='bbconnlab.Tests', verbose_name='Tes'),
        ),
        migrations.AlterField(
            model_name='ordertests',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_tests', to='bbconnlab.Tests', verbose_name='Tes'),
        ),
        migrations.AlterField(
            model_name='results',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results_order', to='bbconnlab.Orders', verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='results',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results_test', to='bbconnlab.Tests', verbose_name='Tes'),
        ),
        migrations.AlterField(
            model_name='testrefranges',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refranges_test', to='bbconnlab.Tests', verbose_name='Tes'),
        ),
    ]