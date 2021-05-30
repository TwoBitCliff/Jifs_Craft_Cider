from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.contrib import messages
# Create your views here.


def view_wishlist(request):
    """ A view that renders the user wishlist """

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, item_id):
    """ Add an item to the wishlist """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    if item_id in list(wishlist.keys()):
        messages.success(request, f'{product.name} already in wishlist.')
    else:
        wishlist[item_id] = quantity
        messages.success(request, f'{product.name} added to wishlist.')

    request.session['wishlist'] = wishlist
    return redirect(redirect_url)
