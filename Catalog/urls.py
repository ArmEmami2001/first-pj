from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views
app_name="Catalog"
urlpatterns = [ 
    path('', views.HomePageView.as_view(), name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('author/', views.AuthorlistView.as_view(), name='authors'),
    
    ]