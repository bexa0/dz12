from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.shortcuts import render, redirect
from shop_side.models import *


def product_create_view(request):
    context = {'category_list': Category.objects.all()}

    form = (request.POST or None)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')

        product = Product()

        if name[0].islower():
            raise ValidationError('Имя не должно начинаться с маленькой буквы')
        else:
            product.name = name

        if not price:
            raise ValidationError('Что-то не так')
        else:
            product.price = price

        if not quantity:
            raise ValidationError('Что-то пошло не так!')
        else:
            product.quantity = quantity

        product.category = Category.objects.get(pk=category)
        product.save()

        return redirect('product_list')

    return render(request, 'shop_side/product_create.html', context)
