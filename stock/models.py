from django.db import models


class Stock(models.Model):
    channel_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)  # 가치투자클럽
    username = models.CharField(max_length=50)  # corevalue
    date = models.DateTimeField()
