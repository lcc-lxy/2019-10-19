from django.shortcuts import render
from .models import Book
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def add_book(request):
    if request.method =='GET':
        return render(request,'bookstore/add_book.html')
    if request.method =='POST':
        dic = {}
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = request.POST.get('price')
        market_price = request.POST.get('market_price')
        Book.objects.create(title=title,pub=pub,price=price,market_price=market_price)
        return render(request,'bookstore/add_book.html')
def all_book(request):
    all_info = Book.objects.all()
    return render(request,'bookstore/all_book.html',locals())
def update(request,id):
    book = Book.objects.get(id = id)
    title = book.title
    market_price = book.market_price
    id = id
    return render(request, 'bookstore/update_book.html',locals())
def ultimal(request,id):
    if request.method =='POST':
        market_price = request.POST.get('inp')
        book = Book.objects.get(id=id)
        book.market_price = market_price
        book.save()
        # return render(request,'bookstore/all_book.html')
        return HttpResponseRedirect('/bookstore/all_book.html')
def delete(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return HttpResponseRedirect('/bookstore/all_book.html')
def test(request):
    # return HttpResponse('<h2>hahh,这是test</h2>')
    # all_info = Book.objects.all()
    # return render(request,'bookstore/all_book.html',locals()) #不修改域名,页面直接显示绑定页面的内容
    return HttpResponseRedirect('/bookstore/all_book.html')  #修改域名,跳转页面