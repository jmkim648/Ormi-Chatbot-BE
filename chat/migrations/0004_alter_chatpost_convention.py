# Generated by Django 4.0.3 on 2023-11-30 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_rename_chatpost_id_chatmessage_chatpost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatpost',
            name='convention',
            field=models.CharField(blank=True, default='없음', max_length=100, null=True),
        ),
    ]
