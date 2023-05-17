from django.db import models
from django.urls import reverse
import uuid
#explicacion del codigo: https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Models#modelo_book
# Create your models here.
class genre(models.Model):
    genre = models.CharField(max_length=200, help_text="Ingrese un genero del libro")
    def __str__(self):
        return self.genre

class Book(models.Model):
    Title=models.CharField(max_length=200)
    Author=models.ForeignKey('Author', on_delete=models.SET_NULL,null=True)
    summary= models.TextField(max_length=1000, help_text="agregue una descripcion del libro")
    isbn=models.CharField('ISBN', max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(genre, help_text="Seleccione un genero para este libro")
    Language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.Title
    def get_absolute_url(self):
     return reverse('Book-detail', args=[str(self.id)])

    
class BookInstance(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID UNICO PARA ESTE LIBRO PARTICULAR")
    imprint=models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    Book=models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)

    LOAN_STATUS =(
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserver'),
    )
    status=models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')
    class Meta:
        ordering = ["due_back"]


    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id,self.Book.Title)
    
class Author(models.Model):
    """
    Modelo que representa un autor
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('autor-detail', args=[str(self.id)])


    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.last_name, self.first_name)
    
class Language(models.Model):
    name = models.CharField(max_length=200,
    help_text="Ingresa el lenguaje del libro")

    def __str__(self):
        
        return self.name
    
