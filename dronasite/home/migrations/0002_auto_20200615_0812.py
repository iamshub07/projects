# Generated by Django 3.0.7 on 2020-06-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='streams',
            name='img',
            field=models.ImageField(default=0, upload_to='assets'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='streams',
            name='title',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
    ]
