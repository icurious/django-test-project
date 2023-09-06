# Generated by Django 2.2 on 2023-09-05 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='nsapp.Author'),
        ),
    ]