# Generated by Django 5.0 on 2024-10-08 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='updated_at',
        ),
    ]
