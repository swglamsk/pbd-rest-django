from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url


urlpatterns = [
    #wszystkie endpointy, endpoint login/ jest customowym endpointem który korzysta z naszego tokena
    path('login/', views.CustomObtainAuthToken.as_view()),
    path('categories/', views.CategoryListView.as_view()),
    path('categories/create/', views.CategoryCreateView.as_view()),
    path('categories/<pk>', views.CategoryRetrieveView.as_view()),
    path('categories/<pk>/update/', views.CategoryUpdateView.as_view()),
    path('categories/<pk>/delete/', views.CategoryDeleteView.as_view()),
    path('authors/', views.AuthorListView.as_view()),
    path('authors/create/', views.AuthorCreateView.as_view()),
    path('authors/<pk>', views.AuthorRetrieveView.as_view()),
    path('authors/<pk>/update/', views.AuthorUpdateView.as_view()),
    path('authors/<pk>/delete/', views.AuthorDeleteView.as_view()),
    path('posts/', views.PostListView.as_view()),
    path('posts/create/', views.PostCreateView.as_view()),
    path('posts/<pk>', views.PostRetrieveView.as_view()),
    path('posts/<pk>/update/', views.PostUpdateView.as_view()),
    path('posts/<pk>/delete/', views.PostDeleteView.as_view()),
    path('tags/', views.TagListView.as_view()),
    path('tags/create/', views.TagCreateView.as_view()),
    path('tags/<pk>', views.TagRetrieveView.as_view()),
    path('tags/<pk>/update/', views.TagUpdateView.as_view()),
    path('tags/<pk>/delete/', views.TagDeleteView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
]
