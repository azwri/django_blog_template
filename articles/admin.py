from django.contrib import admin
from .models import Article, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'get_tags')

    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_articles')

    def get_articles(self, obj):
        return ', '.join([article.title for article in obj.article_set.all()])