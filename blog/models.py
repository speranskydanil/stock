from django.db import models

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

    def __unicode__(self):
        return self.title

