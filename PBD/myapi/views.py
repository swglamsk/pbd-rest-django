from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, AuthorSerializer, PostSerializer, TagSerializer, PostAddSerializer, TagAddSerializer, CategoryAddSerializer
from .models import Category, Author, Post, Tag
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

#Customowy token który zwraca też rolę i username i id
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(
            request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        role = Author.objects.get(id=token.user_id).role
        username = User.objects.get(id=token.user_id).username
        return Response({'token': token.key, 'id': token.user_id, 'role': role, 'username': username})

#Widoki dla wszystkich encji, widoki dodawania różnią się tak aby umożliwić dodawanie za pomocą klucza

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryAddSerializer


class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryAddSerializer


class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorCreateView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDeleteView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorUpdateView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostAddSerializer


class PostRetrieveView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostAddSerializer


class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagCreateView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagAddSerializer


class TagRetrieveView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDeleteView(DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagUpdateView(UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagAddSerializer
