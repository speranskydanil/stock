from django import forms
from blog.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'title', 'content']

        widgets = {
            'content': forms.Textarea(attrs={ 'class': 'summernote' })
        }

