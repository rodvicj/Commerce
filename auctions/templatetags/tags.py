from django import template

register = template.Library()


@register.filter
def in_watchlist(product, user):
    try:
        return product in user.watchlists.all()
    except user.watchlists.DoesNotExist:
        return False
