from django.contrib import admin

from .models import Variant, ProductVariant, ProductVariantPrice, Product, ProductImage

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Variant)
admin.site.register(ProductVariant)
admin.site.register(ProductVariantPrice)
