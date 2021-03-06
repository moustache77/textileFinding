# Generated by Django 3.1.7 on 2022-01-09 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guiding',
            fields=[
                ('uid', models.IntegerField(auto_created=True)),
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='technology_img')),
                ('content', models.TextField()),
            ],
        ),
    ]
