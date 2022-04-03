from django.db import models


# Create your models here.

# 机构
class Inistitution(models.Model):
    pass


class News(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=255, default='')
    url = models.CharField(max_length=255, default='')
    date = models.CharField(max_length=255, default='')
    abstract = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 'news'


class Tree(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255, default='')
    introduction = models.CharField(max_length=255, default='')
    wordcloud = models.CharField(max_length=255, default='')
    value = models.CharField(max_length=255, null=True)
    category = models.IntegerField(default=0)
    url=models.TextField(default='')

    class Meta:
        db_table = 'tree_chart'
