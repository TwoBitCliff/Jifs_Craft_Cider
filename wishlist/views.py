from django.shortcuts import render

# Create your views here.


def view_wishlist(request):
    """ A view that renders the user wishlist """

    return render(request, 'wishlist/wishlist.html')
