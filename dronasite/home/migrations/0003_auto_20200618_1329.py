# Generated by Django 3.0.7 on 2020-06-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200615_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streams',
            name='img',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]
