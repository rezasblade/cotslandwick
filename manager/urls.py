from django.urls import path
from .views import (
    ResultListView,
    ResultDetailView,
    ResultCreateView,
    MatchCreateView,
    ResultUpdateView,
    ResultDeleteView
)
from . import views

urlpatterns = [
    path('', ResultListView.as_view(), name='manager-home'),
    path('results/<int:pk>/', ResultDetailView.as_view(), name='results-detail'),
    path('results/<int:pk>/update/', ResultUpdateView.as_view(), name='results-update'),
    path('results/<int:pk>/delete/', ResultDeleteView.as_view(), name='results-delete'),
    path('results/new', ResultCreateView.as_view(), name='results-create'),
    path('match/new', MatchCreateView.as_view(), name='match-create'),
    # path('playerpoints/', PlayerPointsListView.as_view(), name='playerpoints-list'),
    path('players/', views.players, name='manager-players'),
    path('about/', views.about, name='manager-about'),
]
