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
from django.urls import path
from book.views import *

# 指定应用程序名称，也就是应用命名空间,在团队开发的时候防止命名冲突
app_name = 'book'

urlpatterns = [

    path('', show_books, name='show_books'),
    path('test/', test, name='test'),
    path('query/', query_book_by_id,name='query_by_id'),
    path('item/<int:bid>/',get_book_by_id,name='get_book_by_id'),
]
