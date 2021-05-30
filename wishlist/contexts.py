from django.shortcuts import get_object_or_404
from products.models import Product


def wishlist_contents(request):

    wishlist_items = []
    wishlist = request.session.get('wishlist', {})

    for item_id in wishlist.items():
        product = get_object_or_404(Product, pk=item_id)
        wishlist_items.append({
            'item_id': item_id,
            'product': product,
        })

    context = {
        'wishlist_items': wishlist_items,
    }

    return context
