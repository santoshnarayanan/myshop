from django import forms

# allow user to select quantity from 1- 21
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    # coerce=int to convert the input into an integer
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    # set the default value of the override field to False, 
    # whether the existing quantity has to be overridden
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)