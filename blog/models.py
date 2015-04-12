from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from sanitizer.models import SanitizedCharField, SanitizedTextField

class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'

class Article(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=240)
    content = SanitizedTextField(allowed_tags=['h3', 'h4', 'p', 'a', 'img', 'b', 'i', 'span', 'br', 'ul', 'ol', 'li', 'pre', 'blockquote', 'hr'],
                                 allowed_attributes=['href', 'src', 'style'],
                                 allowed_styles=['font-style', 'font-weight', 'text-decoration', 'vertical-align', 'text-align', 'color', 'background-color', 'float', 'margin', 'padding'],
                                 strip=False)
    publication_date = models.DateTimeField()
    author = models.ForeignKey(User, default=1)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.publication_date:
            self.publication_date = timezone.now()
        return super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publication_date']

class Like(models.Model):
    user = models.ForeignKey(User)
    article = models.ForeignKey(Article)

