# Generated by Django 4.2.1 on 2023-05-18 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='city',
            field=models.CharField(default='Mumbai', max_length=50),
        ),
        migrations.AddField(
            model_name='signup',
            name='comment',
            field=models.CharField(default='No comments', max_length=250),
        ),
        migrations.AddField(
            model_name='signup',
            name='email',
            field=models.EmailField(default='admin@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='signup',
            name='phone',
            field=models.IntegerField(default='123'),
        ),
    ]