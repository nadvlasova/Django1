from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'admins/admin.html')


def admin_users(request):
    return render(request, 'admins/admin-users-read.html')


def admin_users_create(request):
    return render(request, 'admins/admin-users-create.html')


def admin_users_update(request):
    return render(request, 'admins/admin-users-update-delete.html')


def admin_users_delete(request):
    return render(request, 'admins/admin-users-update-delete.html')
