# Python + Django搭建个人博客 Dya03

##  在后台添加数据，方便测试

## 修改导航显示

1. 在views.py增加方法用来查询所有的导航

   ```python
   from django.shortcuts import render
   
   from .models import Category #将数据模型导入
   # Create your views here.
   
   def getCategory():
       category_list = Category.objects.all() # 获取所有的Category数据
       return category_list
   
   
   def index(request):
       '''显示首页'''
       template_name = "index.html" # 要显示的模板名称
   
       category_list = getCategory() # 获取Category数据
       
       return render(request, template_name, {'category_list':category_list}) #将我们定义好的页面返回到页面
   ```

   - 导入数据模型

     ```python
     from .models import Category #将数据模型导入
     ```

   - 获取模型中所有的数据

     ```python
     category_list = Category.objects.all() # 获取所有的Category数据
     ```

   - 将数据全部返回到页面

     ```python
     return render(request, template_name, {'category_list':category_list}) 
     ```

     这里后面的字典就是将获取的数据，返回到前台页面。

2. 修改base.html页面显示

   这里用到了Django的模板语言

   ```python
   {% for category in category_list %}
   {% endfor %}
   ```

   这里的category_list就是后台方法传过来的参数。通过for循环来获取里面所有的数据

   最后用{% endfor %}结尾。

   修改后的HTML页面为：

   ```html
   {% for category in category_list %}
   <li><a href="about.html">{{category.name}}</a></li>
   {% endfor %}
   ```

   {{category.name}}也是Django的模板语言，用来获取对象中的属性。这里是获取category对象中的name值。

   页面显示效果为：

   ![1547357280974](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547357280974.png)

   这里暂时告一段落，后面还会再修改的。

## 获取文章列表

1. 修改views.py来获取文章列表

   ```python
   def getArticles():
       '''获取所有的文章'''
       article_list = Article.objects.all()
       return article_list
   ```

   添加如上方法

   并在index方法中调用

   ```python
   category_list = getCategory() # 获取Category数据
   # 因为首页不需要将所有的文章都显示出来，这里只显示前6条
   article_list = getArticles()[:6] # 获取Article数据
   ```

   

2. 修改页面，和导航的写法基本类似

   ![1547357735579](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547357735579.png)

   通过分析页面可以看出，所有的的文章都是一个独立的DIV，所以我们这里只要保留一个，其他的通过for循环遍历出来就可以了。修改后的效果：

   ![1547358004161](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547358004161.png)

   接下来就是将数据换成我们自己的数据，通过{{}} 这个标签就可以。

   ![1547358303124](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547358303124.png)

   这里有两个地方还没有修改，一个是用户名，还一个是标签名。

   接下来我们来修改一下：

   - 获取用户信息

     再views.py中添加

     ```python
     from django.contrib.auth import *
     ...
     user_name = request.user.username
     
     ```

     修改前台代码：

     ![1547358755705](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547358755705.png)

     看到效果：

     ![1547358780129](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547358780129.png)

     - 显示标签名

       ```python
       {% for tagInfo in article.tags.all %}
       <a class="label label-default">{{tagInfo.name}}</a>
       {% endfor %}
       ```

       这里的article.tags.all是因为tags是article的一个外联表，所以要通过这样的方式来获取数据。

     - 文章概要，我们这里只显示前15个字，其他的省略。

       ```python
       {% if article.content|length >= 15 %}
       	{{article.content| slice:'15'}}......
       {% else %}
       	{{article.content}}
       {% endif %}
       ```

       {% if article.content|length >= 15 %}是Django模板语言中的判断语句。以{% endif %}结尾。

       这里还用到了Django的选择标签“ |length” 是获取文字的长度，“| slice:'15' ”这个类似于切片操作。效果如下：

       ![1547360053162](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547360053162.png)

     暂时修改到这里，后面还要修改。

## 标签展示

1. 修改views.py

   ```python
   def getTags():
       '''获取所有的标签'''
       tags = Tag.objects.all()
       return tags
   
   ....
   def index(request):
       .....
       tags= getTags() # 获取所有的标签
       
   ```

   

2. 修改base.html页面

   ![1547360758608](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547360758608.png)

   观察页面可以看出一个标签就是一个a标签，这里我们只保留一个，其他的用循环来获取。

   ```html
   <div class="labelList">
       {% for tag in tags %}
       <a class="label label-default" href="/tag/jQuery选择器">{{tag.name}}</a>
       {% endfor %}
   </div>
   ```

   效果如下：

   ![1547360950397](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547360950397.png)

   

## 最新发布文章列表

1. 修改views.py

   ```python
   def index(request):
       ....
       article_list_new = Article.objects.all().order_by('add_date')[:10] # 根据发布时间来排序,展现前10条
   ```

   

2. 修改base.html

   ```html
   {% for article in article_list_new %}
   <li>
       <a href="/post/04928311">{{article.title}}</a>
   </li>
   {% endfor %}
   ```

   效果如下：

   ![1547361689519](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547361689519.png)

   但是感觉顺序不太对，因该是倒序。

   所以需要修改一下代码：

   ```python
   article_list_new = Article.objects.all().order_by('-add_date')[:10] # 根据发布时间来排序,展现前10条
   ```

## 友情链接

和之前的做法一下，这里略。

## 文章详情页面

1. 修改views.py

   ```python
   def readArticle(request, id):
       template_name = "article_detail.html" # 要显示的模板名称
       print(type(id))
       article = Article.objects.filter(id = id )
       print(article)
       return render(request, template_name,{'article':article})
   ```

   这里：

   ```python
   article = Article.objects.filter(id = id )
   ```

   是根据传入的id来获取指定的博客信息

   为了传入博客id需要修改一下index.html， 修改如下

   ![1547364729955](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547364729955.png)

   Django调用url用的是{% url 'url名' %}url名是我们定义再urls.py中的。后面接的article.id就是要传入的参数，对应的是url的\<int:id>

   ![1547364908367](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547364908367.png)

2. 修改urls.py

   ```python
   path('read/<int:id>', readArticle, name='readArticle'),
   ```

   定义路由规则

3. 修改html

   因为我们需要用到markdown的内容，所以需要修改一下

   这里用的是django-mdeditor

   地址：https://github.com/pylixm/django-mdeditor

   - 安装插件

     ```python
      pip install django-mdeditor
     ```

     ![1547365441197](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547365441197.png)

   - models.py

     ```python
     from mdeditor.fields import MDTextField
     ....
     class Article(models.Model):
         ....
         content = MDTextField() # 使用markdown格式
     ```

   - 修改settings.py urls.py安装官方文档进行就可以。

     创建一个uploads文件夹

     并重新同步一下数据库

     ```python
     python .\manage.py makemigrations
     python .\manage.py migrate
     ```

   - 运行一下程序看看

     ![1547377606637](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547377606637.png)

     后台已经有了makdown功能了，接下来再前台添加。

   - 需要再base.html中添加一些样式和js可以参照例子

     地址：https://github.com/pylixm/django-mdeditor/blob/master/mdeditor_demo_app/templates/show.html

     运行效果如下：

     ![1547378445006](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547378445006.png)

     同时也发现了导航和右侧的内容没有了。

     修改一下我们的views.py

   ## 添加category信息

   1. 为文章添加一个外键，将博客细分到各个分类中。

      ```python
      class Article(models.Model):
          ...
          category = models.ForeignKey("Category", verbose_name='分类', on_delete=models.CASCADE, blank=True, null=True)
      ```

      

   2. 根据不同的分类显示不同的文章列表

      ![1547379384030](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1547379384030.png)

      - 修改views.py 和urls.py

        ```python
        
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
        
        ```

##  今天的内容就是这些，下回的内容

1. 细节修改
2. 更换数据库
3. 上传服务器，正式发布



