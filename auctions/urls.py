from django.urls import path

from . import views

app_name = "auctions"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.new_list, name="new_list"),
    path("add_watchlist", views.add_watchlist, name="add_watchlist"),
    path("remove_watchlist", views.remove_watchlist, name="remove_watchlist"),
    # TODO: change watchlist to wishlist
    path("watchlist", views.view_watchlist, name="view_watchlist"),
    path("category", views.view_category, name="view_category"),
    path("category/<str:category_name>", views.view_by_category_name, name="view_by_category_name"),
    path("products", views.display_products, name="display_products"),
    path("product/<int:list_id>", views.product_info, name="product_info"),
    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
    path("cart", views.cart, name="cart"),
]
