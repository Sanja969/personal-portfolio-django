# Generated by Django 4.0.5 on 2022-06-04 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='Blog',
        ),
    ]
