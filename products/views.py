from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Product


@login_required
def product_list(request):
    """
    View to display a list of all products.
    Supports HTML and JSON responses.
    """
    products = Product.objects.all()
    if request.headers.get('Content-Type') == 'application/json':
        products_data = [
            {"id": product.id,
             "name": product.name,
             "description": product.description,
             "price": float(product.price)
             }
            for product in products
        ]
        return JsonResponse(products_data, safe=False)
    return render(request,
                  'products/product_list.html',
                  {'products': products})


@login_required
def product_detail(request, pk):
    """
    View to display details of a single product.
    Supports HTML and JSON responses.
    """
    product = get_object_or_404(Product, pk=pk)
    if request.headers.get('Content-Type') == 'application/json':
        product_data = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": float(product.price),
        }
        return JsonResponse(product_data)
    return render(request, 'products/product_detail.html', {'product': product})


@login_required
def product_create(request):
    """
    View to create a new product.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        price = request.POST.get('price')

        if name and price:
            product = Product.objects.create(name=name, description=description, price=price)
            return redirect('product_list')
        return render(request, 'products/product_create_form.html', {'error': 'All fields are required.'})

    return render(request, 'products/product_create_form.html')


@login_required
def product_update(request, pk):
    """
    View to update an existing product.
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name', product.name)
        product.description = request.POST.get('description', product.description)
        product.price = request.POST.get('price', product.price)
        product.save()
        return redirect('product_list')

    return render(request, 'products/product_edit_form.html', {'product': product})
