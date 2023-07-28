from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect  # , HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

# from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .forms import ListForm, BidForm, CommentForm, CategoryForm
from .models import User, Listing, Bid, Comment, Category


def index(request):
    lists = Listing.objects.exclude(active=False).all()

    return render(
        request,
        "auctions/index.html",
        {
            "lists": lists,
        },
    )


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if authentication successful
        if user := authenticate(request, username=username, password=password):
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(
                request,
                "auctions/login.html",
                {
                    "message": "Invalid username and/or password.",
                },
            )
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(
                request,
                "auctions/register.html",
                {
                    "message": "Passwords must match.",
                },
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "auctions/register.html",
                {
                    "message": "Username already taken.",
                },
            )

        login(request, user)
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url="auctions:login")
def new_list(request):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        list_form = ListForm(request.POST)
        category_form = CategoryForm(request.POST)
        list = Listing()

        if list_form.is_valid():
            list.title = list_form.cleaned_data["title"]
            list.description = list_form.cleaned_data["description"]
            list.image_url = list_form.cleaned_data["image_url"]
            list.starting_bid = list_form.cleaned_data["starting_bid"]
            list.user = user
            # newList.category = newCategory

            if category_form.is_valid():
                category = category_form.cleaned_data["name"]

                if len(category) != 0:
                    # new_category = Category()
                    existing = False

                    for existing_category in Category.objects.all():
                        if existing_category.name.lower() == category.lower():
                            list.category = existing_category
                            existing = True

                    if not existing:
                        # new_category.name = category
                        new_category = Category.objects.create(name=category)
                        # new_category.save()
                        list.category = new_category

                list.save()

                return HttpResponseRedirect(
                    reverse("auctions:listing", args=(list.id,))
                )
    else:
        return render(
            request,
            "auctions/new_list.html",
            {"list_form": ListForm(), "category_form": CategoryForm()},
        )


def listing(request, list_id):
    if request.user.id:
        users = User.objects.all()
        user = User.objects.get(id=request.user.id)

        if user in users:
            list = Listing.objects.get(pk=list_id)

            if list.current_bid:
                if not list.active and list.current_bid.user == user:
                    messages.info(request, "You've won the auction!")

            context = {
                "list": list,
                "watchlist": list in user.watchlists.all(),
                "comments": list.comments.all().order_by("-date"),
                "commentForm": CommentForm(),
            }

            if list.active:
                context["bid_form"] = BidForm()
                context["close"] = True if list.user == user else False

            return render(request, "auctions/listing.html", context)
    else:
        list = Listing.objects.get(pk=list_id)
        return render(
            request,
            "auctions/listing.html",
            {"list": list, "comments": list.comments.all().order_by("-date")},
        )


@login_required(login_url="auctions:login")
def add_watchlist(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        id = int(request.POST["list_id"])
        list = Listing.objects.get(pk=id)
        watchlists = user.watchlists.all()

        if list not in watchlists:
            list.watchlist.add(user)
            list.save()

        return HttpResponseRedirect(reverse("auctions:listing", args=(id,)))



@login_required(login_url="auctions:login")
def remove_watchlist(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        id = int(request.POST["list_id"])
        list = Listing.objects.get(pk=id)
        watchlists = user.watchlists.all()

        if list in watchlists:
            list.watchlist.remove(user)
            list.save()

        return HttpResponseRedirect(reverse("auctions:listing", args=(id,)))


@login_required(login_url="auctions:login")
def bid(request):
    if request.method == "POST":
        list_id = int(request.POST["list_id"])
        list = Listing.objects.get(pk=list_id)

        if not list.active:
            messages.error(
                request, f"You cannot bid anymore, the auction is already closed!"
            )
            return HttpResponseRedirect(reverse("auctions:listing", args=(list_id,)))

        minAmount = (
            list.current_bid.amount + 1 if list.current_bid else list.starting_bid
        )
        user_id = int(request.POST["user_id"])
        user = User.objects.get(id=user_id)
        bid_form = BidForm(request.POST)

        if bid_form.is_valid():
            amount = bid_form.cleaned_data["amount"]

            if amount >= minAmount:
                current_bid = Bid(user=user, amount=amount)
                current_bid.save()
                list.current_bid = current_bid
                list.save()
                # messages.success(request, "Bid successful!")
                return HttpResponseRedirect(
                    reverse("auctions:listing", args=(list_id,))
                )

            else:
                messages.error(request, f"Amount should be at least ${minAmount}")

                return HttpResponseRedirect(
                    reverse("auctions:listing", args=(list_id,))
                )
        else:
            return HttpResponseRedirect(reverse("auctions:listing", args=(list_id,)))


@login_required(login_url="auctions:login")
def add_comment(request):
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        list_id = int(request.POST["list_id"])

        if comment_form.is_valid():
            comment = Comment()
            comment.user = request.user
            comment.list = Listing.objects.get(pk=list_id)
            comment.data = comment_form.cleaned_data["data"]
            comment.save()

            return HttpResponseRedirect(reverse("auctions:listing", args=(list_id,)))


@login_required(login_url="auctions:login")
def view_watchlist(request):
    user = User.objects.get(id=request.user.id)
    watchlists = user.watchlists.all()

    return render(
        # TODO: create seperate html file for view_watchlist
        request, "auctions/index.html", {"lists": watchlists, "heading": "Watchlists"}
    )


def view_category(request):
    categories = Category.objects.all()

    return render(
        request,
        "auctions/category.html",
        {"lists": categories},
    )

# categories or category_names
def view_by_category_name(request, category_name):
    category_name = str(category_name)
    category = Category.objects.get(name=category_name)
    lists = Listing.objects.filter(category=category, active=True)

    return render(
        # TODO: create seperate html file for view_by_category_name
        request, "auctions/index.html", {"lists": lists, "heading": category_name}
    )


@login_required(login_url="auctions:login")
def close_listing(request, list_id):
    if request.method == "POST":
        list = Listing.objects.get(pk=list_id)
        if list.active:
            list.active = False
            list.save()

        return HttpResponseRedirect(reverse("auctions:index"))

@login_required(login_url="auctions:login")
def display_products(request):
    # products = Listing.objects.exclude(active=False).all()
    products = Listing.objects.filter(user=request.user).all()

    return render(
        request,
        "auctions/index.html",
        {
            "lists": products,
        },
    )
    
