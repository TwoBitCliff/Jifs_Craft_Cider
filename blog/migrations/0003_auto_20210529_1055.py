# Generated by Django 3.2.3 on 2021-05-29 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_on',
        ),
    ]
