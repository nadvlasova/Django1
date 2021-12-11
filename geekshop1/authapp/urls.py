from django.urls import path
from authapp.views import LoginListView, RegisterListView, ProfileFormView, Logout

app_name = 'authapp'
urlpatterns = [

    path('login/', LoginListView.as_view(), name='login'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('profile/', ProfileFormView.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),

]
