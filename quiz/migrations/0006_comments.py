# Generated by Django 2.2.7 on 2022-12-15 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20221206_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=2000, null=True)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]
