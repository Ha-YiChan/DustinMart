from django.contrib import admin
from .models import Products, Bag

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image_url')
    search_fields = ('name', 'description')
    sortable_by = ('price')

class BagAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'created_at')

admin.site.register(Products, ProductsAdmin)
admin.site.register(Bag, BagAdmin)