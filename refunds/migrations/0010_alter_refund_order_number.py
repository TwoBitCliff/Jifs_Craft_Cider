# Generated by Django 3.2.3 on 2021-06-08 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refunds', '0009_auto_20210606_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refund',
            name='order_number',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
