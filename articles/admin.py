from django.contrib import admin
from .models import Article, Comment
from markdownx.admin import MarkdownxModelAdmin


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


@admin.register(Article)
class ArticleAdmin(MarkdownxModelAdmin):
    pass


admin.site.register(Comment)
