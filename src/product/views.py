import datetime

from django.db.models import Q
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView
from rest_framework import generics
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .forms import VariantForm
from .models import Variant, ProductVariant, Product, ProductImage, ProductVariantPrice
from .serializers import ColorSizeSerializer
from django.core.files.storage import FileSystemStorage


# class CreateProductView(generic.TemplateView):
#     template_name = 'products/create.html'
#
#     def get_context_data(self, **kwargs):
#         print(self.request.POST)
#         context = super(CreateProductView, self).get_context_data(**kwargs)
#         variants = Variant.objects.filter(active=True).values('id', 'title', 'description')
#         context['product'] = True
#         context['variants'] = list(variants.all())
#         return context

def CreateProductView(request):
    variants = Variant.objects.filter(active=True).values('id', 'title', 'description')
    print(request.POST)
    file_list = request.FILES.getlist('file')
    options = request.POST.getlist('option')
    tag_colors = request.POST.getlist('tag_color')
    tag_sizes = request.POST.getlist('tag_size')
    variant_price = request.POST.get('variant_price')
    variant_stock = request.POST.get('variant_stock')
    if request.method == 'POST':
        product = Product.objects.create(title=request.POST.get('product_name'), sku=request.POST.get('product_sku'),
                                         description=request.POST.get('description'))
        product.save()
        # print(file_list)
        for file in file_list:
            myfile = file
            # print(myfile)
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            images = ProductImage.objects.create(product=product)
            images.file_path = uploaded_file_url
            images.save()
        for tag_color in tag_colors:
            color = Variant.objects.get(description=tag_color)
            product_variant = ProductVariant.objects.create(variant_title=tag_color, variant=color, product=product)
            product_variant.save()
        for tag_size in tag_sizes:
            size = Variant.objects.get(description=tag_size)
            product_variant = ProductVariant.objects.create(variant_title=tag_size, variant=size, product=product)
            product_variant.save()
        price = ProductVariantPrice.objects.create(price=variant_price, stock=variant_stock, product=product)
        price.save()
        return redirect('product:list.product')

    context = {
        'variants': variants,
    }
    return render(request, 'products/create.html', context)


class ColorSizeApi(generics.ListAPIView):
    serializer_class = ColorSizeSerializer

    def get_queryset(self):
        title = self.kwargs['title']
        return Variant.objects.filter(title=title)


# Variants


class BaseVariantView(generic.View):
    form_class = VariantForm
    model = Variant
    template_name = 'variants/create.html'
    success_url = '/product/variants'


class VariantView(BaseVariantView, ListView):
    template_name = 'variants/list.html'
    paginate_by = 10

    def get_queryset(self):
        filter_string = {}
        print(self.request.GET)
        for key in self.request.GET:
            if self.request.GET.get(key):
                filter_string[key] = self.request.GET.get(key)
        return Variant.objects.filter(**filter_string)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = True
        context['request'] = ''
        if self.request.GET:
            context['request'] = self.request.GET['title__icontains']
        return context


class VariantCreateView(BaseVariantView, CreateView):
    # form_class = VariantForm
    pass


class VariantEditView(BaseVariantView, UpdateView):
    pk_url_kwarg = 'id'


class ProductListView(ListView):
    template_name = 'products/list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 2
    extra_context = {
        'product': True
    }

    def get_queryset(self):
        # date = self.request.GET['date']
        # print(datetime.date(date))
        try:
            title = self.request.GET['title']
            price_from = self.request.GET['price_from']
            price_to = self.request.GET['price_to']
            variant = self.request.GET['variant']
            date = self.request.GET['date']
            # print(datetime.date(date))
            return Product.objects.filter(title__icontains=title,
                                          productvariantprice__price__range=(price_from, price_to),
                                          productvariant__variant__description__icontains=variant, created_at__date=date)
        except:
            return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['variants'] = Variant.objects.all()
        return context
