from django import forms
# from django.forms import widgets
from django.utils.translation import gettext_lazy as _
# from django.core.exceptions import ValidationError

from .models import Listing, Bid, Comment, Category

class BidForm(forms.ModelForm):

    class Meta:
        model = Bid
        fields = ['amount']
        # error_messages = {'min_value': _('Please enter minimum of $10.')}
        labels = {'amount': _('')}
        
        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter your bid here'})
        }


class ListForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ['title', 'starting_bid', 'description', 'image_url']
        labels = {'starting_bid': _('Starting bid($):')}

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.image.com'}),
            # 'category': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'starting_bid': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['categoryName']
        labels = {'categoryName': _('Category (e.g. Fashion, Toys, Electronics, Home, etc.)')}

        widgets = {
            # 'category': forms.Select(attrs={'class': 'form-control'}),
            'categoryName': forms.TextInput(attrs={'class': 'form-control'}),
        }



class CloseListingForm(forms.ModelForm):

        class Meta:
            model = Listing
            fields = ['active']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['data']
        labels = {'data': _('')}

        widgets = {
            'data': forms.Textarea(attrs={'class': 'new-comment-textarea-container'}),
        }

