# Generated by Django 4.1.5 on 2023-03-19 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showSchool', '0002_hotschoolsearch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotschoolsearch',
            name='school_name',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='showSchool.schoolimg'),
        ),
    ]
