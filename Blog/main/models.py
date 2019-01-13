from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.

class Category(models.Model):
    '''导航类'''
    name = models.CharField(verbose_name='导航名称', max_length=50)
    add_date = models.DateField(verbose_name='添加时间', auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '导航'
        verbose_name_plural = verbose_name

class WebInfo(models.Model):
    '''站点公告'''
    indof = models.CharField(verbose_name='公告内容', max_length=50)
    add_date = models.DateField(verbose_name='添加时间', auto_now=True)

    def __str__(self):
        return self.indof

    class Meta:
        verbose_name = '站点公告'
        verbose_name_plural = verbose_name

class Tag(models.Model):
    '''标签'''
    name = models.CharField(verbose_name='标签名称', max_length=50)
    add_date = models.DateField(verbose_name='添加时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

class Article(models.Model):
    '''博客内容'''
    category = models.ForeignKey("Category", verbose_name='分类', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(verbose_name='标题', max_length=50)
    tags = models.ManyToManyField("Tag", verbose_name="标签") #一个文章可以有多个标签，所以选择多对多
    #content = models.CharField(verbose_name='文章内容', max_length=50) # 这里暂时用这个，后面要用markdow格式，这里需要修改
    content = MDTextField() # 使用markdown格式
    add_date = models.DateField(verbose_name='添加时间', auto_now=True)
    view_count = models.IntegerField(verbose_name='阅读量')
    comments = models.IntegerField(verbose_name='留言量')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name

class Links(models.Model):
    '''友情链接'''
    name = models.CharField(verbose_name='网站名', max_length=50)
    url = models.URLField(verbose_name='友情链接地址', max_length=200)
    add_date = models.DateField(verbose_name='添加时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name