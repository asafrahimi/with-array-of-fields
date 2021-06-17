# Generated by Django 2.2 on 2021-06-17 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=20)),
                ('num_home', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_profession', models.CharField(max_length=20)),
                ('second_profession', models.CharField(max_length=20)),
                ('thrid_profession', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Studentarr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.IntegerField(blank=True, null=True)),
                ('n', models.CharField(blank=True, max_length=50, null=True)),
                ('g', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Id',
            fields=[
                ('i_d', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('snipping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a', to='student.Studentarr')),
            ],
            options={
                'ordering': ['i_d'],
            },
        ),
    ]