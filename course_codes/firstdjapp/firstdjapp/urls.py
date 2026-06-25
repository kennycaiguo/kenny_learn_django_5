"""
URL configuration for firstdjapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path,include,reverse
from django.shortcuts import render


def index(request):
    print(reverse('book:show_books'))
    print(reverse('movie:query_movie')+"?index=6") # query string 方式路由反转传参
    print(reverse('book:get_book_by_id',kwargs={'bid':6})) # 路径参数的路由反转传参
    return render(request,"index.html")
urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    # 注册book路由
    path('book/', include('book.urls')),
    # 注册movie路由
    path('movie/', include('movie.urls')),
]
