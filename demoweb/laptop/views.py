from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import laptopForm
from .models import laptopModel
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    bm = laptopModel.objects.all()
    paginator = Paginator(bm, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'laptop/index.html', {'page_obj': page_obj})

def laptop_detail(request, id):
    ld = laptopModel.objects.get(id = id)
    return render(request, 'laptop/detail.html', {'ld': ld})

def add_laptop(request):
    lf = laptopForm(request.POST, request.FILES)
    if lf.is_valid():
        lf.save()
        return redirect('laptop:laptop')
    
    return render(request, 'laptop/add.html', {'lf': lf})

def laptop_delete(request, id):
    ld = laptopModel.objects.get(id = id)
    ld.delete()

    return redirect('laptop:laptop')

def laptop_update(request, id):
    ld = laptopModel.objects.get(id = id)
    lf = laptopForm(request.POST or None, request.FILES or None, instance=ld)
    if lf.is_valid():
        lf.save()
        return redirect('laptop:laptop')
    
    return render(request, 'laptop/update.html', {'lf': lf})
