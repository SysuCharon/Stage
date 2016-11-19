#-*-coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField('标题',max_length = 100)
    pub_time = models.DateTimeField('创建时间', auto_now_add=True)
    content = models.TextField('正文')
    views = models.IntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="作者", on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-pub_time']
        verbose_name= "新闻"
        permissions = (
            ("add_news", "Can add news"),
            ("delete_news", "can delete news"),
            ("edit_news", "can modify news"),
        )

    def get_absolute_url(self):
        return reverse("news:news_detail", kwargs={'pk':self.id})

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])


