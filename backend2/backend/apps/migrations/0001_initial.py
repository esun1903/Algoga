# Generated by Django 3.1.7 on 2021-03-22 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_seq', models.AutoField(primary_key=True, serialize=False)),
                ('user_email', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=50)),
                ('user_baek_id', models.CharField(blank=True, max_length=50, null=True)),
                ('user_nickname', models.CharField(max_length=50)),
                ('user_profile_image', models.CharField(max_length=500)),
                ('user_register_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
