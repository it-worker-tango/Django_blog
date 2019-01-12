from django.contrib import admin

from .models import Category, WebInfo, Tag, Article, Links # 将我们定义好的表导入进来
# Register your models here.

# 将表注册到后台中
admin.site.register(Category)
admin.site.register(WebInfo)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Links)