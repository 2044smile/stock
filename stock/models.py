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
    site_name = models.CharField(max_length=255)  # 연론사 뷰
    url = models.URLField(max_length=255, unique=True)  # 뉴스 링크
    date = models.DateTimeField()  # 작성 날짜

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
        ordering = ['-created_at']

    def __str__(self):
        return f"Stock-{self.channel}-{self.title}"


class PresidentFact(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    link = models.URLField(max_length=255)
    date = models.DateTimeField()

    class Meta:
        verbose_name = 'PresidentFact'
        verbose_name_plural = 'PresidentFacts'
        ordering = ['-created_at']

    def __str__(self):
        return f"PresidentFact-{self.title}"


class PresidentBriefing(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(max_length=255)
    date = models.DateTimeField()

    class MetA:
        verbose_name = 'PresidentBriefing'
        verbose_name_plural = 'PresidentBriefings'
        ordering = ['-created_at']

    def __str__(self):
        return f"PresidentBriefing-{self.title}"
