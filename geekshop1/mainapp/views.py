from django.shortcuts import render

import json
import os

from django.views.generic import DetailView

from mainapp.models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.

def index(request):
    context = {
        'title': 'Geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    # file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'Geekshop | Каталог',
    }

    # context['products'] = json.load(open(file_path, encoding='utf-8'))
    context['products'] = Product.objects.all()
    context['categories'] = ProductCategory.objects.all()

    return render(request, 'mainapp/products.html', context)


# Контроллер вывода информации о продукте
class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'

    # Добавление списка категорий для вывода сайдбара с категориями на странице каталога
    def get_context_data(self, category_id=None, *args, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context
