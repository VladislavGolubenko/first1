from django import forms
from django.contrib.admin import widgets
from app.books.models import Book, Author


class BookForm(forms.Form):

    author_query = Author.objects.all()

    author_array = (
        [author.last_name, author.last_name] for author in author_query
    )

    book_name = forms.CharField(label='Название книги')
    authors = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        choices=author_array,
        label='Ааторы',
        required=True
    )
