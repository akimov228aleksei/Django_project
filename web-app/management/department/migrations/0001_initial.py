# Generated by Django 3.1.6 on 2021-03-09 21:27

import department.models.employee
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Department:')),
            ],
        ),
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Employee:')),
                ('date1', models.DateField(max_length=30, verbose_name='Date:')),
                ('date2', models.DateField(max_length=30, verbose_name='Date:')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Employee:')),
                ('salary', models.IntegerField(max_length=30, verbose_name='Salary:')),
                ('position', models.CharField(max_length=30, verbose_name='Position:')),
                ('date', models.DateField(max_length=30)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
        ),
    ]
