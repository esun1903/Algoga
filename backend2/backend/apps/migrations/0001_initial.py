# Generated by Django 3.1.7 on 2021-03-26 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeBoard',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.TextField()),
                ('explanation', models.TextField()),
                ('free_write', models.TextField()),
                ('public', models.IntegerField()),
                ('register_date', models.DateTimeField()),
                ('like_cnt', models.IntegerField()),
            ],
            options={
                'db_table': 'code_board',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('register_date', models.DateTimeField()),
                ('like_cnt', models.IntegerField()),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FollowUser',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'follow_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'information',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'language',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('correct_user', models.IntegerField()),
                ('submission_cnt', models.IntegerField()),
                ('correct_rate', models.FloatField()),
                ('level', models.IntegerField()),
                ('avg_try', models.FloatField()),
            ],
            options={
                'db_table': 'problem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecommendProblem',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'recommend_problem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecommendUser',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('baek_id', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'recommend_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('baek_id', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('profile_image', models.CharField(blank=True, max_length=500, null=True)),
                ('register_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InformationOfProblem',
            fields=[
                ('information_seq', models.OneToOneField(db_column='information_seq', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='apps.information')),
            ],
            options={
                'db_table': 'information_of_problem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TypeOfProblem',
            fields=[
                ('type_seq', models.OneToOneField(db_column='type_seq', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='apps.type')),
            ],
            options={
                'db_table': 'type_of_problem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserProblem',
            fields=[
                ('problem_seq', models.OneToOneField(db_column='problem_seq', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='apps.problem')),
                ('correct', models.IntegerField()),
            ],
            options={
                'db_table': 'user_problem',
                'managed': False,
            },
        ),
    ]
