"""new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import function#.为当前目录
urlpatterns = [
    path('admin/', admin.site.urls),#网址匹配上就会进入网站
    # path('', admin.site.urls),  # 网址匹配上就会进入网站
    # //代码保存后，刷新网页生效（pycharm默认自动保存）
    # 写一个函数给用户观看一个网页
    path('',function.home),#function是一个py文件，home是一个函数名
    path('count/',function.count),
    path('third/', function.third),
    path('about/', function.about),

]
