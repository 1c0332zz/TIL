from django.contrib import admin
from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fields = ["title"]


admin.site.register(Article, ArticleAdmin)
