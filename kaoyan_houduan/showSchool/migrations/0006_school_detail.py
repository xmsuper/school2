# Generated by Django 4.1.5 on 2023-03-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showSchool', '0005_alter_userinfo_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='school_detail',
            fields=[
                ('school_id', models.IntegerField(primary_key=True, serialize=False)),
                ('belongsTo', models.CharField(max_length=50)),
                ('create_date', models.IntegerField()),
                ('intro', models.TextField()),
                ('num_doctor', models.IntegerField()),
                ('num_lab', models.IntegerField()),
                ('num_master', models.IntegerField()),
                ('num_subject', models.IntegerField()),
                ('school_space', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'school_detail',
                'managed': True,
            },
        ),
    ]
