# Generated by Django 4.2.6 on 2023-10-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(default='new', max_length=256, verbose_name='Тэг'),
        ),
    ]
