# Generated by Django 2.2.7 on 2022-12-15 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
