from django.shortcuts import render
from random import sample
from django.http import HttpResponse


# Create your views here.
books = [
        "JavaScript 100 days","Java from 0 to hero","cpp from 0 to hero","Python from 0 to hero",
        "Java 100 days","Python 100 days","Qt 100 days","QtQuick 100 days","blender 100 days"
    ]
def show_books(request):

    selected = sample(books, 4)
    res = "<br>".join(selected)
    return HttpResponse(res)

def query_book_by_id(request):
    idx = int(request.GET.get('index',0))
    return HttpResponse(books[idx])

def get_book_by_id(request,bid):
    print(bid)
    return HttpResponse(books[bid])

