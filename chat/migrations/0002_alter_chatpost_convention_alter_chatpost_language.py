# Generated by Django 4.0.3 on 2023-11-28 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatpost',
            name='convention',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='chatpost',
            name='language',
            field=models.CharField(max_length=20),
        ),
    ]