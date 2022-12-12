from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name='start'),
    path('tab/', views.index_tab, name='main'),
    path('books/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('add/', views.new_book, name='new_book'),
    path('create/', views.create, name='create'),
    path('book/<int:id>/view/', views.book_view, name='book_view'),
    path('book/<int:id>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:id>/delete/', views.book_delete, name='book_delete'),
]




















