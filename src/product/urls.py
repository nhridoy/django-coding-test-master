from django.urls import path
from django.views.generic import TemplateView, ListView

from .views import CreateProductView, ColorSizeApi, VariantView, VariantCreateView, VariantEditView, ProductListView
from .models import Product

app_name = "product"

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variantsapi/<title>/', ColorSizeApi.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView, name='create.product'),
    path('list/', ProductListView.as_view(), name='list.product'),
]
