# Generated by Django 5.1.5 on 2025-03-14 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='commissions.commission'),
        ),
    ]
