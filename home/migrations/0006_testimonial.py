# Generated by Django 3.2.18 on 2023-05-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
