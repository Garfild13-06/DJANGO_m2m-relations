# Generated by Django 4.2.6 on 2023-10-09 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_rename_ismain_scope_is_main_alter_tag_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
