from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView, TemplateView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryCreateFormAdmin, ProductCreateFormAdmin
from authapp.models import User
from mainapp.mixin import CustomDispatchMixin, BaseClassContextMixin
from mainapp.models import Product, ProductCategory


class IndexTemplateView(TemplateView):
    template_name = 'admins/admin.html'


class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'Админка | Пользователи'


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Создать пользователя'


class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Обновить пользователя'


class UserDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Удалить пользователя'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'
    title = 'Админка | Список категорий'


class CategoryCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-create.html'
    form_class = CategoryCreateFormAdmin
    success_url = reverse_lazy('admins:admin_category')
    title = 'Админка | Создание категорий'


class CategoryUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    form_class = CategoryCreateFormAdmin
    success_url = reverse_lazy('admins:admin_category')
    title = 'Админка | Обновление категорий'


class CategoryDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    form_class = CategoryCreateFormAdmin
    success_url = reverse_lazy('admins:admin_category')
    title = 'Админка | Удаление категорий'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-read.html'
    title = 'Админка | Продукты'

    def get_queryset(self):
        return Product.objects.all().select_related()


class ProductCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductCreateFormAdmin
    success_url = reverse_lazy('admins:admin_products')
    title = 'Админка | Создать продукт'


class ProductUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductCreateFormAdmin
    success_url = reverse_lazy('admins:admin_products')
    title = 'Админка | Обновить продукт'


class ProductDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_products')
    title = 'Админка | Удалить продукт'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_update(request, pk):
#     product_select = Product.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = ProductCreateFormAdmin(data=request.POST, instance=product_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#         return HttpResponseRedirect(reverse('admins:admin_products'))
#     else:
#         form = ProductCreateFormAdmin(instance=product_select)
#         context = {
#             'title': 'Geekshop - Админ | Обновление продукта',
#             'form': form,
#             'product_select': product_select
#         }
#
#         return render(request, 'admins/admin-products-update-delete.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_delete(request, pk):
#     if request.method == 'POST':
#         product = Product.objects.get(pk=pk)
#         product.delete()
#     return HttpResponseRedirect(reverse('admins:admin_products'))
