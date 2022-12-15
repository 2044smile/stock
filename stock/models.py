from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Channel(BaseModel):
    channel_id = models.IntegerField(default=0)
    name = models.CharField(max_length=32)

class Stock(BaseModel):
    channel = models.ForeignKey("Channel", related_name="channel", on_delete=models.CASCADE, db_column="channel_id")

    title = models.CharField(max_length=255)  # 국내 대체육 시장 200억 ...
    description = models.CharField(max_length=255)  # 상세 설명
    site_name = models.CharField(max_length=16)  # 연론사 뷰
    url = models.URLField(max_length=255)  # 뉴스 링크
    date = models.DateTimeField()  # 작성 날짜
