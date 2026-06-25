from django.urls import path
from . import views
# 注册应用程序命名空间
app_name = 'famous'

urlpatterns = [
    path('', views.index, name='famous_index'),
]

