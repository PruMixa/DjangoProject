from django.shortcuts import render

# Create your views here.
def first_pages(request):
    return render(request, 'first_page.html')

def shops(request):
    context = {
        'my_menu': ['Котлетоны', 'Пюрешка', 'Кампот']
    }
    return render(request, 'shop.html', context)

def orders(request):
    return render(request, 'order.html')