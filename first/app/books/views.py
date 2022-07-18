from django_filters.views import FilterView
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.core.paginator import Paginator
from django.shortcuts import render
from django.conf import settings
from app.books.models import Book, Author, PublishingHouse
from app.books.forms import BookForm
from app.books.filters import BooksFilter
from app.books.validators import validation_book_name


# def get_book_list(request):
#     books_query = Book.objects.all()
#     pagination_page = Paginator(books_query, settings.OBJECTS_ON_PAGE)
#
#     context = {
#         'books': pagination_page,
#     }
#
#     return render(request, 'books/book_list.html', context=context)


class BookList(FilterView):

    model = Book
    filterset_class = BooksFilter
    context_object_name = 'books'
    template_name = 'books/book_list.html'
    paginate_by = settings.OBJECTS_ON_PAGE

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['books'] = self.queryset
        context['title'] = 'Городская библиотека'
        return context


def add_books(request):

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            book_name = validation_book_name(form.cleaned_data['book_name'])
            authors = form.cleaned_data['authors']

    form = BookForm()

    context = {
        'form': form,
    }

    return render(request, 'books/add_book.html', context=context)


class BookDetail(DetailView):
    model = Book
    # template_name = 'book_detailfdsa.html'
    pk_url_kwarg = 'pk'


