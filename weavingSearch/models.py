from django.db import models


class Periodicals(models.Model):
    article_url = models.TextField(max_length=1000, default='')
    category = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255, default='')
    authors = models.CharField(max_length=255, default='')
    company_list = models.CharField(max_length=255, default='')
    keywords = models.CharField(max_length=255, default='')
    abstract = models.TextField(max_length=2000, default='')
    id = models.IntegerField(auto_created=True, primary_key=True)

    class Meta:
        db_table = 'literature'


class Patent(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255, default='')
    inventor = models.TextField(max_length=1000, default='')
    applicant = models.CharField(max_length=255, default='')
    sq_date = models.CharField(max_length=255, default='')
    gk_date = models.CharField(max_length=255, default='')
    url = models.TextField(max_length=1000, default='')
    guo_bie = models.CharField(max_length=255, default='')
    bh = models.CharField(max_length=255, default='')

    class Meta:
        db_table = 'patent'


from weavingSearch.mongodb_utils import *


class Periodical(Document):
    _id = StringField(max_length=255)
    title = StringField(max_length=200)
    authors = StringField(max_length=120)
    article_url = StringField(max_length=120)
    category = StringField(max_length=100)
    meta = {'collection': 'data'}

    def __str__(self):
        return "{0}{1}{2}{3}".format(self.category, self.title, self.authors, self.article_url)


class Periodical_details(Document):
    _id = StringField(max_length=255)
    article_id = ObjectIdField()
    title = StringField(max_length=200)
    author_bh = StringField(max_length=120)
    company_list = StringField(max_length=200)
    keywords = StringField(max_length=200)
    abstract = StringField(max_length=3000)

    def __str__(self):
        return "{0}".format(self.abstract)

    meta = {'collection': 'details'}
