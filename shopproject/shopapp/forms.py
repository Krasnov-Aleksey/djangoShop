from django import forms
from .models import Product


class ProductForm(forms.Form):
    product_selection = forms.ModelChoiceField(queryset=Product.objects.all())
    description_product = forms.CharField(widget=forms.Textarea)
    price_product = forms.DecimalField(max_digits=8, decimal_places=2, widget=forms.NumberInput)
    quantity_product = forms.DecimalField(max_digits=8, decimal_places=3, widget=forms.NumberInput)
    added_date_product = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class UploadPhoto(forms.Form):
    photo = forms.ImageField()
