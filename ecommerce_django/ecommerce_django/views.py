from django.shortcuts import render
from app.models import Category, Product

def Master(request):
    return render(request, 'master.html')

def Index(request):
    category = Category.objects.all()
    product = Product.objects.all()

    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.objects.filter(sub_category=categoryID)
    else:
        product = Product.objects.all()

    context = {
        'category': category,
        'product':product
    }

    return render(request, 'index.html', context)