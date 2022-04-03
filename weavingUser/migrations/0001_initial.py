# Generated by Django 3.1.7 on 2021-12-30 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=2)),
                ('registerTime', models.DateTimeField(max_length=30)),
                ('birthday', models.DateField(max_length=30)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]