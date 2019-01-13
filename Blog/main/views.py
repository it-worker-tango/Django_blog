from django.shortcuts import render
from django.contrib.auth import *
from .models import Category, Article, Tag, Links #将数据模型导入
# Create your views here.

def getCategory():
    '''获取导航'''
    category_list = Category.objects.all() # 获取所有的Category数据
    return category_list

def getArticles():
    '''获取所有的文章'''
    article_list = Article.objects.all()
    return article_list

def getTags():
    '''获取所有的标签'''
    tags = Tag.objects.all()
    return tags

def getLinks():
    links = Links.objects.all()
    return links

def index(request):
    '''显示首页'''
    template_name = "index.html" # 要显示的模板名称

    category_list = getCategory() # 获取Category数据
    # 因为首页不需要将所有的文章都显示出来，这里只显示前6条
    article_list = getArticles()[:6] # 获取Article数据

    tags= getTags() # 获取所有的标签
    
    user_name = request.user.username # 获取用户名
    article_list_new = Article.objects.all().order_by('-add_date')[:10] # 根据发布时间来排序,展现前10条

    links = getLinks() # 获取友情链接

    return render(request, template_name, {'category_list':category_list, 'article_list':article_list, 'tags':tags, 'article_list_new':article_list_new, 'links':links, 'user_name':user_name}) #将我们定义好的页面返回到页面


def readArticle(request, id):
    template_name = "article_detail.html" # 要显示的模板名称
    category_list = getCategory() # 获取Category数据
    tags= getTags() # 获取所有的标签
    article_list_new = Article.objects.all().order_by('-add_date')[:10] # 根据发布时间来排序,展现前10条
    links = getLinks() # 获取友情链接
    article = Article.objects.get(id = id )
    
    return render(request, template_name,{'article':article, 'tags':tags, 'category_list':category_list, 'article_list_new':article_list_new, 'links':links})

def getArticleByCategory(request, cid):
    '''根据分类显示文章'''
    '''显示首页'''
    template_name = "index.html" # 要显示的模板名称

    category_list = getCategory() # 获取Category数据
    # 因为首页不需要将所有的文章都显示出来，这里只显示前6条
    article_list = Article.objects.filter(category_id = cid) # 获取Article数据

    tags= getTags() # 获取所有的标签
    
    user_name = request.user.username # 获取用户名
    article_list_new = Article.objects.all().order_by('-add_date')[:10] # 根据发布时间来排序,展现前10条

    links = getLinks() # 获取友情链接

    return render(request, template_name, {'category_list':category_list, 'article_list':article_list, 'tags':tags, 'article_list_new':article_list_new, 'links':links, 'user_name':user_name, 'isActive':cid}) #将我们定义好的页面返回到页面
