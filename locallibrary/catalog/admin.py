from django.contrib import admin
from .models import Book, Author, BookInstance, Language, Genre

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)

class BookInline(admin.TabularInline):
    model = Book
    exclude = ['summary']
    

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','date_of_birth', 'date_of_death')
    fields = ['name', ('date_of_birth','date_of_death')]
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            "fields": (
                'id', 'book', 'imprint'
            ),
        }),
        ('Availability', {
            'fields':(
                'status','due_back'
            )
        }),
    )
    list_display = ['book', 'status', 'due_back', 'id']
    

