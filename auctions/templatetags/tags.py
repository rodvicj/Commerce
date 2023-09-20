from django import template

register = template.Library()


@register.filter
def in_wishlist(product, user):
    if wishlists := user.wishlists.all():
        return product in wishlists
    else:
        return False
    # try:
    #     return product in user.watchlists.all()
    # except user.watchlists.DoesNotExist:
    #     return False
