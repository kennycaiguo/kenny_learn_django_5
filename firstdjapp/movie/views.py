from django.shortcuts import render
from random import sample
from django.http import HttpResponse

movies = [
'肖申克的救赎','霸王别姬','阿甘正传','泰坦尼克号','千与千寻','这个杀手不太冷','美丽人生','星际穿越','盗梦空间','楚门的世界','辛德勒的名单','忠犬八公的故事',
 '海上钢琴师','三傻大闹宝莱坞','放牛班的春天','疯狂动物城','无间道','大话西游之大圣娶亲','教父（第一部）','触不可及','当幸福来敲门','寻梦环游记','怦然心动',
' 蝙蝠侠：黑暗骑士'
]
# Create your views here.
def show_all_movie(request):
    selected_movies = sample(movies, 12)
    movie_str = "<br>".join(selected_movies)
    return HttpResponse(movie_str)

def query_movie(request):
    index = int(request.GET.get('index'))
    return HttpResponse(movies[index])

def get_movie(request,mid):
    return HttpResponse(movies[mid])