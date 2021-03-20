from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['prod_no', 'serial_no', 'line', 'user', 'error_codes','product_state']


form_prod = ProductForm()
