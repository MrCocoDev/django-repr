# Generated by Django 4.2.2 on 2023-06-30 21:09

import django.db.models.deletion
from django.db import migrations, models

import src.django_better_repr.bases


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JustForFKs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='JustForM2Ms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FourOrMoreFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.CharField(max_length=16)),
                ('two', models.CharField(default='Default', max_length=32, null=True)),
                ('three', models.IntegerField(null=True)),
                ('six', models.FloatField()),
                ('five', models.ManyToManyField(to='myapp.justform2ms')),
                ('four', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.justforfks')),
            ],
            bases=(src.django_better_repr.bases.BetterRepr, models.Model),
        ),
        migrations.CreateModel(
            name='FourOrLessFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.CharField(max_length=16)),
                ('two', models.CharField(default='Default', max_length=32, null=True)),
                ('three', models.IntegerField(null=True)),
                ('four', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.justforfks')),
            ],
            bases=(src.django_better_repr.bases.BetterRepr, models.Model),
        ),
    ]
