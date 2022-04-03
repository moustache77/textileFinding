from django.db import models


# Create your models here.

class HistoryEvent(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=255, default='')
    introduction = models.CharField(max_length=255, default='')
    img_url = models.TextField(max_length=1000, default='')
    time = models.TextField(max_length=255, default='')

    class Meta:
        db_table = 'history_events'
