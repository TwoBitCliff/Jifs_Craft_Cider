# Generated by Django 3.2.3 on 2021-05-29 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                 serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'),
                (1, 'Publish')], default=0)),
                ('user_profile', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.SET_NULL,
                 related_name='blog_post', to='profiles.userprofile')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
