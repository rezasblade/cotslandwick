from django.urls import path
from .views import (
    home,
    players,
    new_match,
    new_player,
    winner,
)
from . import views

urlpatterns = [
    path('', home, name='manager-home'),
    path('new-match/', new_match, name="new_match"),
    path('new-player/', new_player, name="new_player"),
    path('winner/', winner, name="winner"),
    path('players/', views.players, name='manager-players'),
]
