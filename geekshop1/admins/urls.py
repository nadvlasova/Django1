from django.urls import path

from admins.views import index, \
    admin_products, \
    admin_products_create, admin_products_update, admin_products_delete, UserListView, UserCreateView, UserUpdateView, \
    UserDeleteView, CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

app_name = 'admins'
urlpatterns = [

    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),

    path('category/', CategoryListView.as_view(), name='admin_category'),
    path('category-create/', CategoryCreateView.as_view(), name='admin_category_create'),
    path('category-update/<int:pk>', CategoryUpdateView.as_view(), name='admin_category_update'),
    path('category-delete/<int:pk>', CategoryDeleteView.as_view(), name='admin_category_delete'),

    path('products/', admin_products, name='admin_products'),
    path('products-create/', admin_products_create, name='admin_products_create'),
    path('products-update/<int:pk>', admin_products_update, name='admin_products_update'),
    path('products-delete/<int:pk>', admin_products_delete, name='admin_products_delete'),

]
