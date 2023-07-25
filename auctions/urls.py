from django.urls import path

from . import views

app_name = "auctions"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.new_list, name="new_list"),
    path("listing/<int:list_id>", views.listing, name="listing"),
    # TODO: change addremoveWatchlist to add_watchlist and remove_watchlist
    path("addremoveWatchlist", views.watchlist, name="watchlist"),
    path("add_watchlist", views.add_watchlist, name="add_watchlist"),
    path("remove_watchlist", views.remove_watchlist, name="remove_watchlist"),
    path("bid", views.bid, name="bid"),
    path("comment", views.add_comment, name="add_comment"),
    path("watchlist", views.view_watchlist, name="view_watchlist"),
    path("category", views.view_category, name="view_category"),
    path("category/<str:category_name>", views.view_by_category_name, name="view_by_category_name"),
    path("close_listing/<int:list_id>", views.close_listing, name="close_listing")
]
