from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView, TemplateView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryCreateFormAdmin, ProductCreateFormAdmin
from authapp.models import User
from mainapp.models import Product, ProductCategory


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Создать пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Обновить пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Удалить пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)





@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    context = {
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'admins/admin-category-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_create(request):
    if request.method == 'POST':
        form = CategoryCreateFormAdmin(data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('admins:admin_category'))
    else:
        form = CategoryCreateFormAdmin()
        context = {
            'title': 'Geekshop - Админ | Категории создание ',
            'form': form
        }
        return render(request, 'admins/admin-category-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_update(request, pk):
    category_select = ProductCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryCreateFormAdmin(data=request.POST, instance=category_select)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category'))
    else:
        form = CategoryCreateFormAdmin(instance=category_select)
    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form': form,
        'category_select': category_select
    }

    return render(request, 'admins/admin-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_delete(request, pk):
    if request.method == 'POST':
        category = ProductCategory.objects.get(pk=pk)
        category.delete()
    return HttpResponseRedirect(reverse('admins:admin_category'))


@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'admins/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductCreateFormAdmin(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductCreateFormAdmin()
        context = {
            'title': 'Geekshop - Админ | Регистрация',
            'form': form
        }
        return render(request, 'admins/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, pk):
    product_select = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductCreateFormAdmin(data=request.POST, instance=product_select, files=request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductCreateFormAdmin(instance=product_select)
        context = {
            'title': 'Geekshop - Админ | Обновление продукта',
            'form': form,
            'product_select': product_select
        }

        return render(request, 'admins/admin-products-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_delete(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        product.delete()
    return HttpResponseRedirect(reverse('admins:admin_products'))
