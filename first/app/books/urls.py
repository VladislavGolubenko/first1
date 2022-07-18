from django.urls import path
from .views import BookList, BookDetail, add_books

urlpatterns = [
    path('', BookList.as_view(), name='main'),
    path('<int:pk>', BookDetail.as_view(), name='detail_book'),
    path('add_book/', add_books, name='add_book'),
]
