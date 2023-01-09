from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Channel(BaseModel):
    channel_id = models.IntegerField(default=0)
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'Channel'
        verbose_name_plural = 'Channels'
        ordering = ['created_at']

    def __str__(self):
        return f"Channel-{self.channel_id}-{self.name}"

class Stock(BaseModel):
    channel = models.ForeignKey("Channel", related_name="channel", on_delete=models.CASCADE, db_column="channel_id")

    title = models.CharField(max_length=255)  # 국내 대체육 시장 200억 ...
    description = models.TextField()  # 상세 설명
    site_name = models.CharField(max_length=32)  # 연론사 뷰
    url = models.URLField(max_length=255)  # 뉴스 링크
    date = models.DateTimeField()  # 작성 날짜

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
        ordering = ['-created_at']

    def __str__(self):
        return f"Stock-{self.channel}-{self.title}"
