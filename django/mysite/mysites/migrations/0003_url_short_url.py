# Generated by Django 3.0.3 on 2020-03-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysites', '0002_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='short_url',
            field=models.URLField(default=''),
        ),
    ]
