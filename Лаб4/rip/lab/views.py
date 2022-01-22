from django.shortcuts import render
from .models import NoteBook


def index(request):
    notebooks = NoteBook.objects.all()
    return render(request, 'index.html', {'notebooks': notebooks})


def details(request, id):
    notebook = NoteBook.objects.get(id=id)
    return render(request, 'details.html', {'notebook': notebook})