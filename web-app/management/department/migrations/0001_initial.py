# Generated by Django 3.1.6 on 2021-03-26 17:10

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
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Department:')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_employee', models.CharField(max_length=30, unique=True, verbose_name='Employee:')),
                ('salary', models.IntegerField(verbose_name='Salary:')),
                ('position', models.CharField(max_length=30, verbose_name='Position:')),
                ('date', models.DateField(verbose_name='Date:')),
                ('dep', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.department')),
            ],
        ),
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField(verbose_name='Date start:')),
                ('date2', models.DateField(verbose_name='Date end:')),
                ('name_vacation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.employee', to_field='name_employee')),
            ],
        ),
    ]
