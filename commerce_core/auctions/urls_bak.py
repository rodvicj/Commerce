# from django.urls import path

# from . import views
# from .views.shop import RegisterView

# app_name = "auctions"
# urlpatterns = [
#     # TODO: change to rest api;

#     # authentication
#     path("", views.index, name="index"),
#     path("login", views.login_view, name="login"),
#     path("logout", views.logout_view, name="logout"),
#     path("register", RegisterView.as_view(), name="register"),

#     # path("register", views.register, name="register"),

#     # /products/create
#     path("create", views.add_product, name="add_product"),
#     # /products
#     path("added_products", views.added_products, name="added_products"),
#     # /products/id
#     path("product/<int:list_id>", views.product, name="product"),

#     # wishlist
#     # /wishlists/create
#     path("add_wishlist", views.add_wishlist, name="add_wishlist"),
#     # /wishlists/remove
#     path("remove_wishlist", views.remove_wishlist, name="remove_wishlist"),
#     # /wishlists
#     path("wishlist", views.wishlist, name="wishlist"),

#     # category
#     path("category", views.category, name="category"),
#     path("category/<str:category_name>", views.category_name, name="category_name"),

#     # car
#     path("add_to_cart", views.add_to_cart, name="add_to_cart"),
#     path("cart", views.cart, name="cart"),
# ]
