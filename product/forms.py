from django.forms import ModelForm, CharField, HiddenInput, ModelChoiceField
from .models import Product, ProductsToRepair


class ProductForm(ModelForm):
    # user = CharField(widget=HiddenInput())
    # product_state = ModelChoiceField(ProductsToRepair.objects.all())
    class Meta:
        model = Product
        fields = ['prod_no', 'serial_no', 'line', 'user', 'error_codes', 'product_state']


class SearchForm(ModelForm):
    class Meta:
        model = Product
        fields = ['serial_no']