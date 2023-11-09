from django.shortcuts import render
from .models import Game, Collection

# Create your views here.


def home(request):
    collections = Collection.objects.all()
    # use the django ORM to get all instances of Game
    return render(request, 'index.html', {'collections': collections})


def collection_detail(request, pk):
    collection = Collection.objects.get(pk=pk)
    return render(
        request,
        'collection_detail.html',
        {'collection': collection}
    )
