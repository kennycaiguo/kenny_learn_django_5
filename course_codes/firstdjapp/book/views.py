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

class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def info(self):
        return "这是一本非常的书，是四大名著之一"
    
    def __str__(self):
        return f"Name: {self.title}, Author: {self.author}, Price: {self.price}"

def test(request):
    book = Book("三国演义","罗贯中",120)
    author = {'name':'Jason','gender':'male','age':28}
    datas={
        "greeting":"Welcome to Book App",
        "author":author,
        "like":["apple","pear","pineapple"],
        "book":book
    }
    return render(request,'testBook.html',datas)

