from django.db import models


class Api(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    skills = models.CharField(max_length=200, verbose_name='스킬')
    position = models.CharField(max_length=200, verbose_name='담당영역')
    thumbnail = models.URLField(verbose_name='썸네일이미지주소')
    contentImg = models.URLField(verbose_name='메인이미지주소')
    site_view = models.URLField(verbose_name='사이트 주소')
    code_view = models.URLField(verbose_name='깃헙 주소')

    def __str__(self):
        return self.title