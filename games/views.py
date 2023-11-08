from django.shortcuts import render
from .models import Game

# Create your views here.


def home(request):
    games = Game.objects.all()
    # use the django ORM to get all instances of Game
    return render(request, 'index.html', {'games': games})
