# Generated by Django 3.1.7 on 2022-01-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weavingCharts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255)),
                ('introduction', models.CharField(default='', max_length=255)),
                ('wordcloud', models.CharField(default='', max_length=255)),
                ('value', models.CharField(max_length=255, null=True)),
                ('category', models.IntegerField(default=0, max_length=10)),
            ],
            options={
                'db_table': 'tree_chart',
            },
        ),
    ]
