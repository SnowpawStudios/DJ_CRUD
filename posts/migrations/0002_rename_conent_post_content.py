# Generated by Django 4.0.3 on 2022-04-04 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='conent',
            new_name='content',
        ),
    ]