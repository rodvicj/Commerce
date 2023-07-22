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
    path("addremoveWatchlist", views.watchlist, name="watchlist"),
    path("add_watchlist", views.add_watchlist, name="add_watchlist"),
    path("remove_watchlist", views.remove_watchlist, name="remove_watchlist"),
    path("bid", views.bid, name="bid"),
    path("comment", views.addComment, name="addComment"),
    path("watchlist", views.viewWatchlist, name="viewWatchlist"),
    path("category", views.viewCategory, name="viewCategory"),
    path("category/<str:categoryName>", views.viewCategoryName, name="viewCategoryName"),
    path("closeListing/<int:list_id>", views.closeListing, name="closeListing")
]
