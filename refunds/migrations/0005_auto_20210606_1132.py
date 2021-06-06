# Generated by Django 3.2.3 on 2021-06-06 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
        ('refunds', '0004_auto_20210606_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refund',
            name='user',
        ),
        migrations.AddField(
            model_name='refund',
            name='order_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='checkout.order'),
        ),
    ]
