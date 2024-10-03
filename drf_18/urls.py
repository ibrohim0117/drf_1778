"""
URL configuration for drf_18 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.views import (
    UserListCreateApiView, UserRetrieveUpdateDestroyAPIView,
    CategoryListApiView, ProductListApiView, UserListApiView, UserDetailApiView, UserDeleteApiView, UserCreateApiView,
    UserUpdateApiView
)

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('admin/', admin.site.urls),

    #1
    path('user-create/', UserCreateApiView.as_view(), name='user_create'),
    path('users/', UserListApiView.as_view(), name='user_list'),

    # 2
    # path('users/', UserListCreateApiView.as_view(), name='user_create'),

    # --------------------------------------------------------------------

    #1
    path('user/<int:pk>/', UserDetailApiView.as_view(), name='user_detail'),
    path('user-update/<int:pk>/', UserUpdateApiView.as_view(), name='user_update'),
    path('user-delete/<int:pk>/', UserDeleteApiView.as_view(), name='user_delete'),

    #2
    path('user/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user'),

    # path('category', CategoryListApiView.as_view(), name='category_list'),
    # path('products', ProductListApiView.as_view(), name='product_list')

]
