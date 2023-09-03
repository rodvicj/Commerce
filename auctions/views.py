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
    lists = Product.objects.all()

    return render(
        request,
        "auctions/products.html",
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


# def listing(request, list_id):
#     if request.user.id:
#         users = User.objects.all()
#         user = User.objects.get(id=request.user.id)

#         if user in users:
#             list = Product.objects.get(pk=list_id)

#             # if list.current_bid:
#             #     if not list.active and list.current_bid.user == user:
#             #         messages.info(request, "You've won the auction!")

#             context = {
#                 "list": list,
#                 "watchlist": listin user.watchlists.all(),
#                 "comments": list.comments.all().order_by("-date"),
#                 "commentForm": CommentForm(),
#             }

#             # if list.active:
#             # context["bid_form"] = BidForm()
#             # context["close"] = True if list.user == user else False

#             return render(request, "auctions/product_info.html", context)
#     else:
#         list = Product.objects.get(pk=list_id)
#         return render(
#             request,
#             "auctions/product_info.html",
#             {"list": list, "comments": list.comments.all().order_by("-date")},
#         )


@login_required(login_url="auctions:login")
def add_watchlist(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        list_id = int(request.POST["list_id"])
        item = Product.objects.get(pk=list_id)
        watchlists = user.watchlists.all()

        if item not in watchlists:
            item.watchlist.add(user)
            item.save()

        # return HttpResponseRedirect(reverse("auctions:product_info", args=(list_id,)))
        return HttpResponseRedirect(reverse("auctions:index"))


@login_required(login_url="auctions:login")
def remove_watchlist(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        list_id = int(request.POST["list_id"])
        item = Product.objects.get(pk=list_id)
        watchlists = user.watchlists.all()

        if item in watchlists:
            item.watchlist.remove(user)
            item.save()

        # return HttpResponseRedirect(reverse("auctions:product_info", args=(list_id,)))
        return HttpResponseRedirect(reverse("auctions:index"))


# @login_required(login_url="auctions:login")
# def bid(request):
#     if request.method == "POST":
#         list_id = int(request.POST["list_id"])
#         list = Product.objects.get(pk=list_id)

#         if not list.active:
#             messages.error(
#                 request, f"You cannot bid anymore, the auction is already closed!"
#             )
#             return HttpResponseRedirect(reverse("auctions:listing", args=(list_id,)))

#         minAmount = (
#             list.current_bid.amount + 1 if list.current_bid else list.amount
#         )
#         user_id = int(request.POST["user_id"])
#         user = User.objects.get(id=user_id)
#         bid_form = BidForm(request.POST)

#         if bid_form.is_valid():
#             amount = bid_form.cleaned_data["amount"]

#             if amount >= minAmount:
#                 current_bid = Bid(user=user, amount=amount)
#                 current_bid.save()
#                 list.current_bid = current_bid
#                 list.save()
#                 # messages.success(request, "Bid successful!")
#                 return HttpResponseRedirect(
#                     reverse("auctions:listing", args=(list_id,))
#                 )

#             else:
#                 messages.error(request, f"Amount should be at least ${minAmount}")

#                 return HttpResponseRedirect(
#                     reverse("auctions:listing", args=(list_id,))
#                 )
#         else:
#             return HttpResponseRedirect(reverse("auctions:listing", args=(list_id,)))


@login_required(login_url="auctions:login")
def view_watchlist(request):
    user = User.objects.get(id=request.user.id)
    watchlists = user.watchlists.all()

    return render(
        # TODO: create seperate html file for view_watchlist
        request,
        "auctions/products.html",
        {
            "lists": watchlists,
        },
        # "auctions/index.html",
        # {
        #     "lists": watchlists,
        #     "heading": "Watchlists"
        # },
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
    watchlists = (request.user.watchlists.all(),)
    watchlists = list(watchlists)

    return render(
        request,
        "auctions/products.html",
        {
            "lists": products,
            "watchlists": watchlists
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


@login_required(login_url="auctions:login")
def product_info(request, list_id):
    if request.user.id:
        # users = User.objects.all()
        user = User.objects.get(id=request.user.id)

        # if user in users:
        item = Product.objects.get(pk=list_id)

        context = {
            "list": item,
            "watchlist": item in user.watchlists.all(),
            "cartForm": CartForm(max_value=item.quantity),
        }

        return render(request, "auctions/product_info.html", context)
    # else:
    #     list = Product.objects.get(pk=list_id)
    #     return render(
    #         request,
    #         "auctions/product_info.html",
    #         {"list": list, "comments": list.comments.all().order_by("-date")},
    #     )


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
        cart = CartForm(request.POST, max_value=item.quantity)

        if cart.is_valid():
            item = Cart.objects.create(buyer=request.user, quantity=quantity, product=item)

            # return HttpResponseRedirect(reverse("auctions:index"))
            # TODO: show cart icon and add show a number that indicates how many products are in the cart
            return HttpResponseRedirect(reverse("auctions:product_info", args=(item.product.id,)))

        else:
            # TODO: add messages.info
            # messages.info(request, "You've won the auction!")

            if quantity < 1:
                messages.error(request, "Invalid quantity")
            elif quantity > 5:
                messages.info(request, "Maximum item you can add to cart is quanity")
            return HttpResponseRedirect(reverse("auctions:product_info", args=(list_id,)))


@login_required(login_url="auctions:login")
def cart(request):
    return render(
        request,
        "auctions/cart.html",
    )
