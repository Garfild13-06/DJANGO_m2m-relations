# Generated by Django 4.2.6 on 2023-10-09 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default=None, max_length=256, verbose_name='Тэг'),
        ),
    ]