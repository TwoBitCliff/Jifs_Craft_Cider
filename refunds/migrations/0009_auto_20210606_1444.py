# Generated by Django 3.2.3 on 2021-06-06 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refunds', '0008_alter_refund_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refund',
            name='user_profile',
        ),
        migrations.AlterField(
            model_name='refund',
            name='order_number',
            field=models.CharField(default='00000', max_length=5),
        ),
    ]
