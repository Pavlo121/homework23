from django.db import models
from .forms import RegistrationForm
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import connection

class UpperCaseText(models.Model):
    text = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.text = self.text.upper()  # Перевод текста в верхний регистр перед сохранением
        super().save(*args, **kwargs)

    def word_count(self):
        """Метод для подсчета слов в тексте."""
        return len(self.text.split())

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

