from django import forms
from django.forms import inlineformset_factory

from .models import Author, Book


class AuthorForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = '__all__'


BookFormSet = inlineformset_factory(Author, Book, fields=('title','cover'), extra=1)