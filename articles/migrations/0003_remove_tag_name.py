# Generated by Django 4.2.6 on 2023-10-09 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_scope'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='name',
        ),
    ]
