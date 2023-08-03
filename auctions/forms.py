from django import forms
# from django.forms import widgets
from django.utils.translation import gettext_lazy as _
# from django.core.exceptions import ValidationError

from .models import Product, Comment, Cart

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


class ListForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'amount', 'category', 'description', 'image_url']
        labels = {'amount': _('Amount($):')}

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.image.com'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name']
#         labels = {'name': _('Category (e.g. Fashion, Toys, Electronics, Home, etc.)')}

#         widgets = {
#             # 'category': forms.Select(attrs={'class': 'form-control'}),
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#         }



class CloseListingForm(forms.ModelForm):

        class Meta:
            model = Product
            fields = ['active']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['data']
        labels = {'data': _('')}

        widgets = {
            'data': forms.Textarea(attrs={'class': 'new-comment-textarea-container'}),
        }


class CartForm(forms.ModelForm):

    class Meta:
        model = Cart
        fields = ['quantity']
        # quantity = forms.NumberInput(min=4),
        # labels = {'data': _('')}
        labels = {'quantity': _('quantity:')}

        # quantity = models.PositiveIntegerField(blank=False, default=1)
        widgets = {
            # 'quantity': forms.Textarea(attrs={'class': 'new-comment-textarea-container'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '2' }),
            # 'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'quantity': forms.NumberInput(attrs={'min': '2' }),
        }
