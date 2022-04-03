# Generated by Django 3.1.7 on 2022-01-25 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weavingHistory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyevent',
            name='img_url',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='historyevent',
            name='introduction',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='historyevent',
            name='time',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='historyevent',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='historyevent',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='historyevent',
            table='history_events',
        ),
    ]
