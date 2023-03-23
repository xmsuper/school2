# Generated by Django 4.1.5 on 2023-03-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApptestAuthor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'apptest_author',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApptestBook',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'apptest_book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('name', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('code', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('feature_id', models.IntegerField()),
            ],
            options={
                'db_table': 'feature',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'province',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProvinceA',
            fields=[
                ('code', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'province_a',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProvinceB',
            fields=[
                ('code', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'province_b',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProvinceOther',
            fields=[
                ('code', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'province_other',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolImg',
            fields=[
                ('school_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('school_img', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'school_img',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolInfo',
            fields=[
                ('is_211', models.IntegerField()),
                ('type_name', models.CharField(blank=True, max_length=50, null=True)),
                ('type_school_name', models.CharField(max_length=50)),
                ('province_area', models.CharField(max_length=10)),
                ('syl', models.IntegerField(blank=True, null=True)),
                ('clicks', models.IntegerField(blank=True, null=True)),
                ('is_985', models.IntegerField(blank=True, null=True)),
                ('is_zihuaxian', models.IntegerField(blank=True, null=True)),
                ('rk_rank', models.IntegerField(blank=True, null=True)),
                ('province_name', models.CharField(blank=True, max_length=20, null=True)),
                ('is_ads', models.IntegerField(blank=True, null=True)),
                ('school_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'school_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learntype', models.CharField(db_column='learnType', max_length=10)),
                ('major_code', models.CharField(max_length=20)),
                ('major_name', models.TextField()),
                ('total', models.CharField(blank=True, max_length=10, null=True)),
                ('politics', models.TextField(blank=True, null=True)),
                ('english', models.TextField(blank=True, null=True)),
                ('procourse', models.TextField(blank=True, null=True)),
                ('procourese2', models.TextField(blank=True, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('school_name', models.TextField(blank=True, null=True)),
                ('school_tel', models.TextField(blank=True, null=True)),
                ('school_email', models.TextField(blank=True, null=True)),
                ('school_web', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'school_score',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolType',
            fields=[
                ('name', models.CharField(max_length=10, unique=True)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('type_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'school_type',
                'managed': False,
            },
        ),
    ]
