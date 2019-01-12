from django.shortcuts import render

# Create your views here.

def index(request):
    '''显示首页'''
    template_name = "index.html" # 要显示的模板名称
    return render(request, template_name) #将我们定义好的页面返回到页面