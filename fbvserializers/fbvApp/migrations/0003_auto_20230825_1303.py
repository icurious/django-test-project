# Generated by Django 2.2 on 2023-08-25 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbvApp', '0002_auto_20230825_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.IntegerField(),
        ),
    ]
