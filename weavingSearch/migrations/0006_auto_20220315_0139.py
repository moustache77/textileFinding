# Generated by Django 3.1.7 on 2022-03-14 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weavingSearch', '0005_auto_20220224_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patent',
            name='inventor',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
