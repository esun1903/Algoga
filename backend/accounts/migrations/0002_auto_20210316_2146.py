# Generated by Django 3.1.7 on 2021-03-16 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_profile_image',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_nickname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_password',
            field=models.CharField(max_length=30),
        ),
    ]
