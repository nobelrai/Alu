# Generated by Django 3.2.18 on 2023-05-30 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20230530_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
