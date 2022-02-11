from django.shortcuts import render
# from .models import Post

def wholesale_form(request):
    context = {}
    return render(request, 'order_form/wholesale_form.html', {'context': context})