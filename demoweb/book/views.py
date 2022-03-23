from django.shortcuts import render
from django.http import HttpResponse
from .forms import bookForm

# Create your views here.
def index(request):
    return render(request, 'book/index.html')

def add_book(request):
    bf = bookForm()
    return render(request, 'book/add.html', {'bf': bf})

def save_book(request):
    if request.method == 'POST':
        g = bookForm(request.POST, request.FILES)
        if g.is_valid():
            g.save()
            return HttpResponse('ok')
        else:
            return HttpResponse('Khong duoc validate')
    else:
        return HttpResponse('Khong phai post')