from django.db import models
from django.urls import reverse
import uuid

class Genre(models.Model):
    name = models.CharField(max_length=50, help_text="Enter the genre's name, e.g., fiction, drama, anime, etc.")
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=100, help_text="Enter the book's title")
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    #isbn = models.CharField(max_length=20, verbose_name='ISBN')
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Caracteres <a target="_blank" href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField('Genre', help_text='choose a genre for this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, blank=True)
    
    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
    
    display_genre.short_description = 'Genre'
    
    class Meta:
        ordering = ['title', 'author']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])
    
    
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID unico para este libro en toda la biblioteca')
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o','On loan'),
        ('a','Available'),
        ('r','Reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='book availability')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    
    class Meta:
        ordering = ["due_back"]
    
    def __str__(self):
        return f'{self.id} ({self.book.title})'
    
class Author(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Dead', null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])
    
    
    def __str__(self):
        return self.name
    
class Language(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name