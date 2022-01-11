from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.http import HttpResponse
from .models import Product
from django.urls import reverse
def index(request):
    return HttpResponse('hi')


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }
    return render(request , 'detail.html' , context)


def like_or_unlike(request, id):
    print('like and unlike product ')
    product = get_object_or_404(Product, id=id)

    if request.user in product.like.all():
        product.like.remove(request.user)
    else:
        product.like.add(request.user)
    
    return redirect(reverse(product_detail , kwargs={'id':product.id}))



def user_favorites(request):
    user_favorites  = Product.objects.filter(like=request.user)
    context  = {
        'user_favorites': user_favorites
    }
    return render(request , 'user_favorites.html' , context)