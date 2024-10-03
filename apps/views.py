from django.shortcuts import render
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import(
    CreateAPIView, ListAPIView, ListCreateAPIView,
    RetrieveAPIView, UpdateAPIView, DestroyAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import ProductFilter
from .models import Category, Product
from .serializers import UserCreateSerializer, UserListSerializer, UserUpdateSerializer, ProductListSerializer, \
    CategoryListSerializer


# class UserCreateApiView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer


class UserCreateApiView(APIView):

    def post(self, request):
        a = request.data
        serializer = UserCreateSerializer(data=a)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_201_CREATED,
                'message': 'User successfully created',
                'data': serializer.data

            }
            return Response(data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
#
# class UserListApiView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserListSerializer


class UserListApiView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True).data
        data = {
            "users": len(serializer),
            'status': status.HTTP_200_OK,
            'data': serializer
        }
        return Response(data)


# class UserDetailApiView(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserListSerializer


class UserDetailApiView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            # user = User.objects.filter(id=pk).first()
            serializer = UserListSerializer(user).data
            # print(serializer)
            # print(user)
            data = {
                'status': status.HTTP_200_OK,
                'data': serializer
            }
            return Response(data)
        except:
            data = {
                'status': status.HTTP_404_NOT_FOUND,
                'data': "Bunday foydalanuvchi yo'q"
            }
            return Response(data)


# class UserUpdateApiView(UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserUpdateSerializer


class UserUpdateApiView(APIView):

    def put(self, request, pk):
        user = User.objects.get(id=pk)
        a = request.data
        serializer = UserUpdateSerializer(data=a, instance=user, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_201_CREATED,
                'message': 'User successfully updated',
                'data': serializer.data

            }
            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class UserDeleteApiView(DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserListSerializer


class UserDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            # print(user)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)



class UserListCreateApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('first_name', 'last_name', 'email', 'username')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserListSerializer
        elif self.request.method == 'POST':
            return UserCreateSerializer

        return super().get_serializer_class()


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = DjangoFilterBackend, SearchFilter
    search_fields = ['name', 'description']
    # filterset_fields = ('category', 'owner')
    # filterset_class = ProductFilter












