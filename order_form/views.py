from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from .forms import *

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'order_form/upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ProductForm()
    return render(request, 'order_form/upload.html', {'form': form})

def product_image_view(request):
  
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProductForm()
    return render(request, 'order_form/upload.html', {'form' : form})

# def success(request):
#     return HttpResponse('successfully uploaded')

def wholesale_form(request):
    products = Product.objects.all()
    return render(request, 'order_form/wholesale_form.html', {'products': products})
