from django.urls import path
from .views import (
    home,
    players,
    new_match,
    new_player,
    update_player,
    # new_player1,
    # new_player2,
    winner,
    new_playerstats,
)
from . import views

urlpatterns = [
    path('', home, name='manager-home'),
    path('new-match/', new_match, name="new_match"),
    path('new-player/', new_player, name="new_player"),
    path('update-player/', update_player, name="update_player"),
    # path('new-player1/', new_player1, name="new_player1"),
    # path('new-player2/', new_player2, name="new_player2"),
    path('winner/', winner, name="winner"),
    path('players/', views.players, name='manager-players'),
]
