import re
from django.core.exceptions import ValidationError


def validation_book_name(book_name):
    if re.fullmatch(r"Книга \w*", book_name):
        return book_name
    raise ValidationError(message="не соответствует требованиям")
