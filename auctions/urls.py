from django.urls import path

from . import views

app_name = "auctions"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createNewList, name="createNewList"),
    path("listing/<int:list_id>", views.listing, name="listing"),
    path("addremoveWatchlist", views.Watchlist, name="Watchlist"),
    path("bid", views.bid, name="bid"),
    path("comment", views.addComment, name="addComment"),
    path("watchlist", views.viewWatchlist, name="viewWatchlist"),
    path("category", views.viewCategory, name="viewCategory"),
    path("category/<str:categoryName>", views.viewCategoryName, name="viewCategoryName"),
    path("closeListing/<int:list_id>", views.closeListing, name="closeListing")
]
