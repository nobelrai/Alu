# Generated by Django 3.2.18 on 2023-05-17 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='region',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
