from django.shortcuts import render

# Create your views here.
def first_pages(request):
    return render(request, 'first_page.html')

def shops(request):
    return render(request, 'shop.html')

def orders(request):
    return render(request, 'order.html')