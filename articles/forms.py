from django import forms
from .models import Article, Tag


class ArticleFormCreate(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'body', 'author', 'tags', 'image', )



class TagFormCreate(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ('name', )