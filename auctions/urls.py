from django.urls import path

from . import views

app_name = "auctions"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.add_product, name="add_product"),
    path("add_wishlist", views.add_wishlist, name="add_wishlist"),
    path("remove_wishlist", views.remove_wishlist, name="remove_wishlist"),
    path("wishlist", views.wishlist, name="wishlist"),
    path("category", views.category, name="category"),
    path("category/<str:category_name>", views.category_name, name="category_name"),
    path("added_products", views.added_products, name="added_products"),
    path("product/<int:list_id>", views.product, name="product"),
    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
    path("cart", views.cart, name="cart"),
]
