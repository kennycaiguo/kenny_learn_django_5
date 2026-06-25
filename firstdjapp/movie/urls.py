from django.urls import path
from movie.views import *

# 指定应用程序名称，也就是应用命名空间
app_name = 'movie'

urlpatterns = [
    path('', show_all_movie,name='show_all_movie'), # 注意，这个name非常重要，建议以后每一个路由都加上这个name，方便路由反转操作
    path('query/', query_movie,name='query_movie'),
    path('item/<int:mid>/', get_movie,name='get_movie'),
]


