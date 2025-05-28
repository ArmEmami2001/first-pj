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
    path('author/<str:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<uuid:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<uuid:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    ]