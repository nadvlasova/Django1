from django.urls import path

from ordersapp.views import OrderList, OrderCreate, OrderUpdate, OrderDelete, OrderDetail, order_forming_complete

app_name = 'ordersapp'
urlpatterns = [

    path('', OrderList.as_view(), name='list'),
    path('create/', OrderCreate.as_view(), name='create'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='delete'),
    path('read/<int:pk>/', OrderDetail.as_view(), name='read'),
    path('forming_complete/<int:pk>/', order_forming_complete, name='forming_complete'),

]
