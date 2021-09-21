from django.contrib import admin

# Register your models here.
from facebook.models import Article, Comment, Page

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Page)
