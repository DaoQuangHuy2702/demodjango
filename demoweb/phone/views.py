from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import phoneForm
from .models import phoneModel
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    bm = phoneModel.objects.all()
    paginator = Paginator(bm, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'phone/index.html', {'page_obj': page_obj})

def phone_detail(request, id):
    pd = phoneModel.objects.get(id = id)
    return render(request, 'phone/detail.html', {'pd': pd})

def add_phone(request):
    pf = phoneForm(request.POST, request.FILES)
    if pf.is_valid():
        pf.save()
        return redirect('phone:phone')
    
    return render(request, 'phone/add.html', {'pf': pf})

def phone_delete(request, id):
    pd = phoneModel.objects.get(id = id)
    pd.delete()

    return redirect('phone:phone')

def phone_update(request, id):
    pd = phoneModel.objects.get(id = id)
    pf = phoneForm(request.POST or None, request.FILES or None, instance=ld)
    if pf.is_valid():
        pf.save()
        return redirect('phone:phone')
    
    return render(request, 'phone/update.html', {'pf': pf})

