from django import template

register = template.Library()


@register.filter
def in_watchlist(product, user):
    if watchlists := user.watchlists.all():
        return product in watchlists
    else:
        return False
    # try:
    #     return product in user.watchlists.all()
    # except user.watchlists.DoesNotExist:
    #     return False
