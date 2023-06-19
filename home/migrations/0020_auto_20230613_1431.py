# Generated by Django 3.2.18 on 2023-06-13 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_items_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='gender',
            field=models.BooleanField(choices=[('M', 'Male'), ('F', 'Female')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]