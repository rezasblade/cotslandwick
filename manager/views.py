from django.shortcuts import render
from django.http import HttpResponse
from .models import Player
from .models import MatchDay
from .models import MatchDaySquadRed
from .models import MatchDaySquadBlue
from .models import Results
from .models import Team
from .models import PlayerPoints
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.


class StaffRequiredMixin(object):
    @classmethod
    def as_view(self, *args, **kwargs):
        view = super(StaffRequiredMixin, self).as_view(*args, **kwargs)
        return staff_member_required(view)


def home(request):
    context = {
        'results': Results.objects.select_related()
    }
    return render(request, 'manager/home.html', context)


class ResultListView(ListView):
    model = Results
    template_name = 'manager/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'results'
    ordering = ['-matchdate']


class ResultDetailView(DetailView):
    model = Results


class ResultCreateView(StaffRequiredMixin, CreateView):
    model = Results
    fields = ['matchdate', 'redsscore', 'bluescore', 'winner']


class ResultUpdateView(StaffRequiredMixin, UpdateView):
    model = Results
    fields = ['matchdate', 'redsscore', 'bluescore', 'winner']


class ResultDeleteView(StaffRequiredMixin, DeleteView):
    model = Results
    success_url = '/'


class MatchCreateView(LoginRequiredMixin, CreateView):
    model = MatchDay
    fields = ['matchdate', 'matchtype']


# class PlayerPointsListView(ListView):
#     model = PlayerPoints


def tests(request):
    context = {
        'player': Player.objects.all()
    }
    return render(request, 'manager/tests.html', context)


def players(request):
    context = {
        'player': Player.objects.all()
    }
    return render(request, 'manager/players.html', context)


def about(request):
    return render(request, 'manager/about.html', {'title': 'About'})


# def teams(request):
#     context = {
#         'team': Team.objects.all()
#     }
#     return render(request, 'manager/teams.html', context)


# def results(request):
#     context = {
#         'result': Result.objects.all()
#     }
#     return render(request, 'manager/results.html', context)
