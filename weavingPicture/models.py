from django.forms import ModelForm
from neomodel import StringProperty, DateTimeProperty, UniqueIdProperty, IntegerProperty, DateProperty
from django.db import models
from datetime import datetime, date
from django_neomodel import DjangoNode


# Create your models here.
# neo4j
# 4DmtatTLMO_gqm0FFM1tT6iKIEwgTyD91wKGl2LzuI4

class Picture(models.Model):
    id = models.CharField('编号', max_length=50, primary_key=True)
    url = models.CharField('链接', max_length=255, null=False)
    introduction = models.CharField('简介', max_length=100, default='')


class Author(models.Model):
    id = models.IntegerField('编号', primary_key=True, auto_created=True)
    name = models.CharField('姓名', max_length=255, null=False)
    company = models.CharField('单位', max_length=255, default='/')
    area = models.CharField('领域', max_length=255, default='/')
    total_papers = models.IntegerField('发文数', default=0)
    main_art1 = models.TextField('代表作1', max_length=1000, default='/')
    main_art2 = models.TextField('代表作2', max_length=1000, default='/')
    main_art3 = models.TextField('代表作2', max_length=1000, default='/')

    class Meta:
        db_table = 'author'


class Book(DjangoNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    title = StringProperty()
    status = StringProperty(choices=(
        ('Available', 'A'),
        ('On loan', 'L'),
        ('Damaged', 'D'),
    ), default='Available')
    created = DateTimeProperty(default=datetime.utcnow)

    class Meta:
        app_label = 'weavingPicture'


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["uid", "title", "status", "created"]


class MyTeenRomanticComedy(DjangoNode):
    id = UniqueIdProperty()
    name = StringProperty()
    age = IntegerProperty()
    created = DateTimeProperty(default=datetime.utcnow)
    birthday = DateProperty(default="2000/10/10")

    class Meta:
        app_label = 'weavingPicture'


class Sport(DjangoNode):
    uid = UniqueIdProperty()
    id = IntegerProperty(unique_index=True)
    name = StringProperty()
    category = StringProperty()
    created = DateTimeProperty(default=datetime.utcnow)

    class Meta:
        app_label = 'weavingPicture'


# 纺织技术节点
class WeavingTech(DjangoNode):
    pass


# 纺织技术关系边
class WeavingRelation(DjangoNode):
    pass
