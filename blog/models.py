from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'

class Article(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=240)
    content = models.TextField()
    publication_date = models.DateTimeField()
    author = models.ForeignKey(User, default=User.objects.get(username='admin').pk)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.publication_date:
            self.publication_date = timezone.now()
        return super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publication_date']

