# Generated by Django 3.2.3 on 2021-06-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refunds', '0005_auto_20210606_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refund',
            name='order_number',
            field=models.CharField(default='00000', max_length=5),
        ),
        migrations.AlterField(
            model_name='refund',
            name='status',
            field=models.IntegerField(choices=[(0, 'unresolved'), (1, 'resolved')], default=0),
        ),
    ]
