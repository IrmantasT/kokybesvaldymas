from django.db.models import Model, CharField, DateTimeField, IntegerField, TextField, ForeignKey,DO_NOTHING, ManyToManyField
from django.contrib.auth.models import User


class ErrorCodesForProduct(Model):
    code = CharField(max_length=15)
    type = CharField(max_length=25)
    description = CharField(max_length=150)

    def __str__(self):
        return self.description


class Line(Model):
    line_no = IntegerField()
    description = CharField(max_length=150)

    def __str__(self):
        return self.description


class ProductsToRepair(Model):
    state = CharField(max_length=60)  # good/needs_fixing/is_fixed/cant_fix


class Product(Model):
    serial_no = CharField(max_length=25, unique=True)
    prod_no = CharField(max_length=25)
    line = ForeignKey(Line, on_delete=DO_NOTHING)
    user = ForeignKey(User,on_delete=DO_NOTHING, blank=True)
    date = DateTimeField(auto_now_add=True)
    error_codes = ManyToManyField(ErrorCodesForProduct, blank=True)
    product_state = ForeignKey(ProductsToRepair,on_delete=DO_NOTHING)


class Repair(Model):
    user = ForeignKey(User,on_delete=DO_NOTHING)
    product = ForeignKey(Product, on_delete=DO_NOTHING)
    description = TextField()
    start_time = DateTimeField(auto_now_add=True)
    end_time = DateTimeField()