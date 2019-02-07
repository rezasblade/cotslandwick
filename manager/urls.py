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
    player_detail,
    playerlist,

)
from . import views
from .views import PlayerListView

urlpatterns = [
    path('', home, name='manager-home'),
    path('new-match/', new_match, name="new_match"),
    path('playertable/', views.players, name='manager-players'),
    path('winner/', winner, name="winner"),

    path('new-player/', views.new_player, name="new_player"),
    # above uses class NewPlayerForm(forms.ModelForm):

    path('playerlist/', views.playerlist, name='playerlist'),

    path('update-player/', update_player, name="update_player"),
    # above uses class NewPlayerForm(forms.ModelForm):


    path('players/<int:pk>/', views.player_detail, name='manager-players_detail'),
    path('players/<int:pk>/edit/', views.player_edit, name='manager-players_edit'),



    # path('players/', PlayerListView.as_view(), name='manager-players'),

]
