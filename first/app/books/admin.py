from django.contrib import admin
from .models import Book, PublishingHouse, Author, BooksInAuthor

'''
list_display - какие атрибуты будут выводиться на экран
list_display_links - какие атрибуты будут ссылками
search_fields - по каким полям будет происходить поиск
list_editable - каки поля можно можно изменить в таблице
list_filter - по каким полям будет происходить фильтрация
fieldsets - настройки для страницы с изменениями
'''


class BookAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'book_name', 'description', 'id_publishing_house', 'date_creation', 'date_add',
        'is_daleted'
    )
    list_display_links = ('id', 'book_name')
    search_fields = ('book_name',)
    list_editable = ('is_daleted',)
    list_filter = ('date_creation', 'book_name', 'is_daleted')
    fieldsets = (
        (None, {
            'fields': ('book_name', 'description', 'id_publishing_house', 'date_creation', 'authors', 'book_img')
        }),
    )


class PublishingHouseAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'publishing_house_name', 'adress', 'contact_phone', 'email', 'website_linck', 'date_add',
        'is_daleted'
    )
    list_display_links = ('id', 'publishing_house_name')
    search_fields = ('publishing_house_name',)
    list_editable = ('is_daleted',)
    list_filter = ('date_add', 'is_daleted')
    fieldsets = (
        (
            (None, {
                'fields': ('publishing_house_name', 'adress')
            }),

            ('Контакты', {
                'fields': ('contact_phone', 'email', 'website_linck')
            })
        )
    )


class AuthorAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'first_name', 'last_name', 'fathername', 'country', 'birthday', 'languages',
        'is_daleted'
    )
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'last_name', 'fathername')
    list_editable = ('is_daleted',)
    list_filter = ('last_name', 'country', 'languages', 'is_daleted')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'fathername', 'country', 'birthday', 'languages',
                       'is_daleted')
        }),
    )

    inlines = [
        BooksInAuthor,
    ]


admin.site.register(Book, BookAdmin)
admin.site.register(PublishingHouse, PublishingHouseAdmin)
admin.site.register(Author, AuthorAdmin)
