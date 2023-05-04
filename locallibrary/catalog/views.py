from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre, Language

def index(request):
    
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()   # all() está implícito por defecto
    num_genres = Genre.objects.all().count()
    num_game_books = Book.objects.filter(title__icontains='game').count()
    
    return render(
        request,
        'index.html',
        context=
        {
            'num_books':num_books,
            'num_instances':num_instances,
            'num_instances_available':num_instances_available,
            'num_authors':num_authors,
            'num_genres':num_genres,
            'num_game_books':num_game_books,
        },
    )
    
    
class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
        
        
class BookDetailView(generic.DetailView):
    model = Book
    # model = BookInstance
    # copies = BookInstance.objects.all().count()
    # context = {'copies':copies}

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

class AuthorDetailView(generic.DeleteView):
    model=Author

