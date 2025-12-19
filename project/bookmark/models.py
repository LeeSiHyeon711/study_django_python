from django.db import models

class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)  # 글자수 100자 제한, 공백 허용
    url = models.URLField('URL', unique=True)  # 유일한 URL 필드값 허용

    def __str__(self):
        return self.title