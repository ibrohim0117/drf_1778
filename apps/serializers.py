from django.contrib.auth.models import User
from rest_framework import serializers

from apps.models import Category, Product


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email',  'last_name', 'password']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_staff', 'date_joined', 'last_login', 'is_active', 'user_permissions', 'groups')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', )


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'slug', 'price', 'image', 'description', 'category', 'owner')