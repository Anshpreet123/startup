# Generated by Django 4.2.1 on 2023-05-23 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_signup_city_signup_comment_signup_email_signup_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='address',
            field=models.CharField(default='Mumbai', max_length=300),
        ),
        migrations.AddField(
            model_name='signup',
            name='pin',
            field=models.IntegerField(default='222222'),
        ),
    ]