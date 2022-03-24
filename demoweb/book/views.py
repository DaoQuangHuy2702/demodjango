from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import bookForm
from .models import bookModel
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    bm = bookModel.objects.all()
    paginator = Paginator(bm, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'book/index.html', {'page_obj': page_obj})

def book_detail(request, id):
    bd = bookModel.objects.get(id = id)
    return render(request, 'book/detail.html', {'bd': bd})

def add_book(request):
    bf = bookForm(request.POST, request.FILES)
    if bf.is_valid():
        bf.save()
        return redirect('book:book')
    
    return render(request, 'book/add.html', {'bf': bf})

def book_delete(request, id):
    bd = bookModel.objects.get(id = id)
    bd.delete()

    messages.success(request, 'Xóa sản phẩm thành công')
    return redirect('book:book')

def book_update(request, id):
    bd = bookModel.objects.get(id = id)
    bf = bookForm(request.POST or None, request.FILES or None, instance=bd)
    if bf.is_valid():
        bf.save()
        return redirect('book:book')
    
    return render(request, 'book/update.html', {'bf': bf})
