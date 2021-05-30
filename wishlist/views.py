from django.shortcuts import render, redirect

# Create your views here.


def view_wishlist(request):
    """ A view that renders the user wishlist """

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, item_id):
    """ Add an item to the wishlist """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    if item_id in list(wishlist.keys()):
        wishlist[item_id] = quantity
    else:
        wishlist[item_id] = 1

    request.session['wishlist'] = wishlist
    print(request.session['wishlist'])
    return redirect(redirect_url)
