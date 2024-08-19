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
    list_display = ('title', 'created_at')


admin.site.register(Article)
admin.site.register(Comment)
