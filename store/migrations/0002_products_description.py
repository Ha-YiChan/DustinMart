# Generated by Django 4.2.10 on 2024-12-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(default='No description'),
            preserve_default=False,
        ),
    ]
