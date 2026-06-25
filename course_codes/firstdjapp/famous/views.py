from django.shortcuts import render

# Create your views here.
masterpieces = [
    {"name":"三国演义","author":"罗贯中","year":"1985","price":120},
    {"name":"水浒传","author":"施耐庵","year":"1925","price":150},
    {"name":"红楼梦","author":"罗贯中","year":"1985","price":130},
    {"name":"西游记","author":"吴承恩","year":"1985","price":140}
]

def index(request):
    return render(request, 'famous.html',{'books':masterpieces})