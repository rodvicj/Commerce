from django import forms

# from django.forms import widgets
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Product, Cart


class ListForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "amount", "category", "description", "image_url"]
        labels = {"amount": _("Amount($):")}

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "image_url": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://www.image.com"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
        }


class CloseListingForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["active"]


class CartForm(forms.ModelForm):
    # NOTE: args = arguments, kwargs = keyword arguments
    def __init__(self, *args, **kwargs):
        max_value = kwargs.pop("max_value")
        super(CartForm, self).__init__(*args, **kwargs)
        self.fields["quantity"].widget = forms.NumberInput(
            attrs={
                # "value": 1,
                "min": 1,
                "max": max_value,
                "class": "form-control d-flex justify-content-between",
            },
        )
        self.fields["quantity"].validators = [
            MinValueValidator(1),
            MaxValueValidator(max_value),
        ]

        # self.fields["quantity"].widgets = {"min_value": "Please enter your name"}

        # self.fields["quantity"].error_messages = {"min_value": _("hi there")}

    class Meta:
        model = Cart
        fields = ["quantity"]


# forms.CharField(error_messages={"required": "Please enter your name"})
# class BidForm(forms.ModelForm):

#     class Meta:
#         model = Bid
#         fields = ['amount']
#         # error_messages = {'min_value': _('Please enter minimum of $10.')}
#         labels = {'amount': _('')}
#
#         widgets = {
#             'amount': forms.NumberInput(attrs={'placeholder': 'Enter your bid here'})
#         }
