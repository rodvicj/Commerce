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
            # newList.category = newCategory

            # if category_form.is_valid():
            #     category = category_form.cleaned_data["name"]

            #     if len(category) != 0:
            #         # new_category = Category()
            #         existing = False

            #         for existing_category in Category.objects.all():
            #             if existing_category.name.lower() == category.lower():
            #                 list.category = existing_category
            #                 existing = True

            #         if not existing:
            #             # new_category.name = category
            #             new_category = Category.objects.create(name=category)
            #             # new_category.save()
            #             list.category = new_category

            item.save()

        return HttpResponseRedirect(reverse("auctions:product_info", args=(item.id,)))
    else:
        return render(
            request,
            "auctions/new_list.html",
            # {"list_form": ListForm(), "category_form": CategoryForm()},
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

        # return HttpResponseRedirect(reverse("auctions:product_info", args=(list_id,)))
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

        # return HttpResponseRedirect(reverse("auctions:product_info", args=(list_id,)))
        return HttpResponseRedirect(reverse("auctions:index"))


@login_required(login_url="auctions:login")
def view_wishlist(request):
    user = User.objects.get(id=request.user.id)
    wishlists = user.wishlists.all()

    return render(
        # TODO: create seperate html file for view_watchlist
        request,
        "auctions/products.html",
        {
            "lists": wishlists,
        },
    )


def view_category(request):
    # categories = Category.objects.all()
    choices = Product.choices
    # categories = Product.objects.all()
    categories = []

    for choice in choices:
        categories.append(choice[1])
    # choices = categories.field.choices

    return render(
        request,
        "auctions/category.html",
        {"lists": categories},
    )


# categories or category_names
def view_by_category_name(request, category_name):
    category_name = str(category_name).lower()
    # category = Category.objects.get(name=category_name)
    lists = Product.objects.filter(category=category_name)
    # lists = Product.objects.filter(category=category, active=True)

    return render(
        # TODO: create seperate html file for view_by_category_name
        request,
        "auctions/products.html",
        {
            "lists": lists,
            "heading": category_name
        },
    )


# @login_required(login_url="auctions:login")
# def close_listing(request, list_id):
#     if request.method == "POST":
#         list = Product.objects.get(pk=list_id)
#         if list.active:
#             list.active = False
#             list.save()

#         return HttpResponseRedirect(reverse("auctions:index"))


@login_required(login_url="auctions:login")
def display_products(request):
    # products = Product.objects.exclude(active=False).all()
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


# @login_required(login_url="auctions:login")
# def display_item_info(request):
#     # products = Product.objects.exclude(active=False).all()
#     products = Product.objects.filter(user=request.user).all()

#     return render(
#         request,
#         "auctions/products.html",
#         {
#             "lists": products,
#         },
#     )
#


# @login_required(login_url="auctions:login")
def product_info(request, list_id):
    if request.user.id:
        user = User.objects.get(id=request.user.id)
        item = Product.objects.get(pk=list_id)

        context = {
            "list": item,
            "wishlist": item in user.wishlists.all(),
            "cartForm": CartForm(max_value=item.quantity),
        }

        return render(request, "auctions/product_info.html", context)

    else:
        return render(
            request,
            "auctions/product_info.html",
            {"list": Product.objects.get(pk=list_id)},
        )


# TODO: add pagination to this web app
# def get_context_data(self, **kwargs):
#     context = super(CategoryPageView, self).get_context_data(**kwargs)
#     category = self.get_object()
#     products = Product.objects.filter(category=category)
#     tags = Product.TagsChoices


@login_required(login_url="auctions:login")
def add_to_cart(request):
    if request.method == "POST":
        list_id = int(request.POST["list_id"])
        quantity = int(request.POST["quantity"])
        item = Product.objects.get(pk=list_id)
        max_quantity = item.quantity
        cart = CartForm(request.POST, max_value=max_quantity)

        if cart.is_valid():
            # TODO: everytime a user add to cart something, check for all the users cart first then check if the current
            # product the user's want to add is already one of the items in its cart
            # else create new cart for that product

            # get all current user's cart
            carts = request.user.cart_products.all()

            for cart in carts:
                if item == cart.product:
                    cart.quantity += quantity
                    if cart.quantity > max_quantity:
                        # change quantity to max supported
                        cart.quantity = item.quantity
                        cart.save()

                        # TODO: clear messages.info first before providing new string
                        messages.get_messages(request).used = True

                        messages.info(request, f"Maximum quantity for this item is {max_quantity}")
                        return HttpResponseRedirect(reverse("auctions:product_info", args=(cart.product.pk,)))
                        # return HttpResponseRedirect(reverse("auctions:cart"))

                    else:
                        cart.save()
                        return HttpResponseRedirect(reverse("auctions:product_info", args=(cart.product.pk,)))
                        # return HttpResponseRedirect(reverse("auctions:cart"))

            # if already_in_cart:
            #     # return HttpResponseRedirect(reverse("auctions:index"))
            #     # TODO: show cart icon and add show a number that indicates how many products are in the cart
            #     return HttpResponseRedirect(reverse("auctions:product_info", args=(product_id,)))
            # else:

            item = Cart.objects.create(buyer=request.user, quantity=quantity, product=item)
            # return HttpResponseRedirect(reverse("auctions:product_info", args=(item.product.id,)))
            return HttpResponseRedirect(reverse("auctions:cart"))

        else:
            messages.get_messages(request).used = True
            messages.error(request, "Something went wrong")
            return HttpResponseRedirect(reverse("auctions:product_info", args=(list_id,)))


@login_required(login_url="auctions:login")
def cart(request):
    return render(request, "auctions/cart.html", {"carts": request.user.cart_products.all()})
