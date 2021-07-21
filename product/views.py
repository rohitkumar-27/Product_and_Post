from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list/')
    else:
        form = ProductForm()
    return render(request, 'product/product_create.html', {'form':form})

def product_list(request):
    product = Product.objects.using('product_db').all
    return render(request, 'product/product_list.html', {'product':product})


def product_delete(request, pk):
    product = Product.objects.using('product_db').get(pk=pk)
    product.delete(using='product_db')
    return redirect('product_list')