# Generated by Django 4.2.6 on 2023-10-09 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_tag_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='isMain',
            new_name='is_main',
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Тэг'),
        ),
    ]
