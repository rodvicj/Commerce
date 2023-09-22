from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect  # , HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import CartForm, ListForm
from .models import Cart, Product, User


def index(request):
    return render(
        request,
        "auctions/products.html",
        {
            "lists": Product.objects.all(),
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
        # user = request.user.id
        list_form = ListForm(request.POST)
        # category_form = CategoryForm(request.POST)
        item = Product()

        if list_form.is_valid():
            item.title = list_form.cleaned_data["title"]
            item.category = list_form.cleaned_data["category"]
            item.description = list_form.cleaned_data["description"]
            item.image_url = list_form.cleaned_data["image_url"]
            item.amount = list_form.cleaned_data["amount"]
            item.user = user
            item.save()

        return HttpResponseRedirect(reverse("auctions:product_info", args=(item.id,)))
    else:
        return render(
            request,
            "auctions/new_list.html",
            {"list_form": ListForm()},
        )


@login_required(login_url="auctions:login")
def add_wishlist(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        list_id = int(request.POST["list_id"])
        item = Product.objects.get(pk=list_id)
        wishlists = user.wishlists.all()

        if item not in wishlists:
            item.wishlists.add(user)
            item.save()

        return HttpResponseRedirect(reverse("auctions:index"))


@login_required(login_url="auctions:login")
def remove_wishlist(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        list_id = int(request.POST["list_id"])
        item = Product.objects.get(pk=list_id)
        wishlists = user.wishlists.all()

        if item in wishlists:
            item.wishlists.remove(user)
            item.save()

        return HttpResponseRedirect(reverse("auctions:index"))


@login_required(login_url="auctions:login")
def view_wishlist(request):
    user = User.objects.get(id=request.user.id)
    wishlists = user.wishlists.all()

    return render(
        request,
        "auctions/products.html",
        {
            "lists": wishlists,
        },
    )


def view_category(request):
    choices = Product.choices
    categories = []

    for choice in choices:
        categories.append(choice[1])

    return render(
        request,
        "auctions/category.html",
        {"lists": categories},
    )


def view_by_category_name(request, category_name):
    category_name = str(category_name).lower()
    lists = Product.objects.filter(category=category_name)

    return render(
        request,
        "auctions/products.html",
        {
            "lists": lists,
            "heading": category_name
        },
    )


@login_required(login_url="auctions:login")
def display_products(request):
    products = Product.objects.filter(user=request.user).all()
    wishlists = (request.user.wishlists.all(),)
    wishlists = list(wishlists)

    return render(
        request,
        "auctions/products.html",
        {
            "lists": products,
            "wishlists": wishlists
        },
    )


def product_info(request, list_id):
    if request.user.id:
        user = User.objects.get(id=request.user.id)
        item = Product.objects.get(pk=list_id)

        return render(
            request,
            "auctions/product_info.html",
            {
                "list": item,
                "wishlist": item in user.wishlists.all(),
                "cartForm": CartForm(max_value=item.quantity),
            },
        )

    return render(
        request,
        "auctions/product_info.html",
        {"list": Product.objects.get(pk=list_id)},
    )


@login_required(login_url="auctions:login")
def add_to_cart(request):
    if request.method == "POST":
        list_id = int(request.POST["list_id"])
        quantity = int(request.POST["quantity"])
        item = Product.objects.get(pk=list_id)
        max_quantity = item.quantity
        cart = CartForm(request.POST, max_value=max_quantity)

        if cart.is_valid():
            # get all current user's cart
            carts = request.user.cart_products.all()

            for cart in carts:
                if item == cart.product:
                    cart.quantity += quantity
                    if cart.quantity > max_quantity:
                        # change quantity to max supported
                        cart.quantity = item.quantity
                        cart.save()

                        # clear messages.info first before providing new string
                        messages.get_messages(request).used = True

                        messages.info(
                            request,
                            "Your cart already has the maximum quantity for this item",
                        )
                        return HttpResponseRedirect(reverse("auctions:product_info", args=(cart.product.pk,)))

                    else:
                        cart.save()
                        return HttpResponseRedirect(reverse("auctions:product_info", args=(cart.product.pk,)))

            item = Cart.objects.create(buyer=request.user, quantity=quantity, product=item)
            return HttpResponseRedirect(reverse("auctions:cart"))

        else:
            messages.get_messages(request).used = True
            messages.error(request, "Something went wrong")
            return HttpResponseRedirect(reverse("auctions:product_info", args=(list_id,)))


@login_required(login_url="auctions:login")
def cart(request):
    return render(request, "auctions/cart.html", {"carts": request.user.cart_products.all()})
