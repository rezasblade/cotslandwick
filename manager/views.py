import time
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import UpdateView

from .models import Player, Match, Team, City
from .newplayerform import NewPlayerForm, UpdatePlayerForm


def home(request):
    # list all players, teams and matches
    players = Player.objects.all()
    teams = Team.objects.all()
    matches = Match.objects.all()

    # get dates that have matches
    dates = []
    for match in matches:
        dates.append(match.date.strftime('%Y-%m-%d'))

    # get only unique dates
    dates = list(set(dates))
    dates.sort(key=lambda x: time.mktime(time.strptime(x, "%Y-%m-%d")), reverse=True)

    # list goals by team and date
    team_a_goals = []
    team_b_goals = []

    for date in dates:
        team_a_goals.append(Match.objects.filter(team__id=1).filter(date=date)[0].goals)
        team_b_goals.append(Match.objects.filter(team__id=2).filter(date=date)[0].goals)

    # dictionary to store date and goals
    dates_goals = []
    for i, date in enumerate(dates):
        dates_goals.append([date, team_a_goals[i], team_b_goals[i]])

    content = {
        'dates_goals': dates_goals,
    }
    return render(request, 'manager/home.html', content)


def players(request):
    # descending order player list by points
    players = Player.objects.all().order_by('-points')
    won = Match.objects.filter(won=True)
    lost = Match.objects.filter(won=False)
    tie = Match.objects.filter(won=None)

    player_stats = []

    for player in players:
        print(player.name)
        # print(player.preferredfoot)
        won_matches = len(won.filter(player__name=player.name))
        lost_matches = len(lost.filter(player__name=player.name))
        tie_matches = len(tie.filter(player__name=player.name))
        points = won_matches * 3 + tie_matches
        player_stats.append([player.name, player.preferredfoot, won_matches, tie_matches, lost_matches, points, player.position, player.trait, player.goalsscored, player.assists, player.motmawards])

    content = {
        'player_stats': player_stats
    }

    return render(request, 'manager/players.html', content)


def playerlist(request):
    # descending order player list by points
    players = Player.objects.all().order_by('-points')
    content = {
        'players': players
    }

    return render(request, 'manager/playerlist.html', content)


def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'manager/player_detail.html', {'player': player})


class PlayerListView(ListView):
    model = Player
    template_name = 'manager/players.html'
    context_object_name = 'player_stats'


def new_match(request):
    teams = Team.objects.all()
    players = Player.objects.all()

    content = {
        'teams': teams,
        'players': players,
    }

    different = False
    if request.method == 'POST':
        # lookup for teams
        team_a_id = request.POST['team_a']
        team_a = Team.objects.filter(id=team_a_id)[0]
        team_b_id = request.POST['team_b']
        team_b = Team.objects.filter(id=team_b_id)[0]

        # Don't allow to save if both teams have the same name
        if team_a == team_b:
            different = False
            print('same teams')
            messages.warning(request, 'Your team names are the same! make sure they are different!')

        if team_a != team_b:
            different = True
            print('different teams')

        if request.POST['date'] == '':
            messages.warning(request, 'Please select a match date!')
            return redirect('new_match')

        if request.POST['date'] is not None and different:
            date = request.POST['date']
            team_a = Team.objects.get(name=team_a)
            team_b = Team.objects.get(name=team_b)

            # fetch players names
            if request.POST['name1'] is not None:
                player1 = request.POST['name1']
                player1, created = Player.objects.get_or_create(
                    id=player1
                )
                match1 = Match(
                    player=player1,
                    team=team_a,
                    date=date)
                match1.save()
            if request.POST['name2'] is not None:
                player2 = request.POST['name2']
                player2, created = Player.objects.get_or_create(
                    id=player2
                )
                match2 = Match(
                    player=player2,
                    team=team_a,
                    date=date)
                match2.save()
            if request.POST['name3'] is not None:
                player3 = request.POST['name3']
                player3, created = Player.objects.get_or_create(
                    id=player3
                )
                match3 = Match(
                    player=player3,
                    team=team_a,
                    date=date)
                match3.save()
            if request.POST['name4'] is not None:
                player4 = request.POST['name4']
                player4, created = Player.objects.get_or_create(
                    id=player4
                )
                match4 = Match(
                    player=player4,
                    team=team_a,
                    date=date)
                match4.save()
            if request.POST['name5'] is not None:
                player5 = request.POST['name5']
                player5, created = Player.objects.get_or_create(
                    id=player5
                )
                match5 = Match(
                    player=player5,
                    team=team_a,
                    date=date)
                match5.save()

            if request.POST['name6'] is not None:
                player6 = request.POST['name6']
                player6, created = Player.objects.get_or_create(
                    id=player6
                )
                match6 = Match(
                    player=player6,
                    team=team_b,
                    date=date)
                match6.save()
            if request.POST['name7'] is not None:
                player7 = request.POST['name7']
                player7, created = Player.objects.get_or_create(
                    id=player7
                )
                match7 = Match(
                    player=player7,
                    team=team_b,
                    date=date)
                match7.save()
            if request.POST['name8'] is not None:
                player8 = request.POST['name8']
                player8, created = Player.objects.get_or_create(
                    id=player8
                )
                match8 = Match(
                    player=player8,
                    team=team_b,
                    date=date)
                match8.save()
            if request.POST['name9'] is not None:
                player9 = request.POST['name9']
                player9, created = Player.objects.get_or_create(
                    id=player9
                )
                match9 = Match(
                    player=player9,
                    team=team_b,
                    date=date)
                match9.save()
            if request.POST['name10'] is not None:
                player10 = request.POST['name10']
                player10, created = Player.objects.get_or_create(
                    id=player10
                )
                match10 = Match(
                    player=player10,
                    team=team_b,
                    date=date)
                match10.save()
                messages.success(request, 'Match Created')
                return redirect('manager-home')

    return render(request, 'manager/new_match.html', content)


# def new_player(request):

#     if request.method == 'POST':
#         if request.POST['new_player'] is not None:
#             new_player = request.POST['new_player']
#             new_player_preferredfoot = request.POST['new_player_preferredfoot']
#             new_player_position = request.POST['new_player_position']
#             new_player_trait = request.POST['new_player_trait']
#             new_player, created = Player.objects.get_or_create(
#                 name=new_player, preferredfoot=new_player_preferredfoot, position=new_player_position, trait=new_player_trait
#             )

#     return render(request, 'manager/new_player.html', {})
# THE ABOVE IS NOT USING A FORM TO CREATE THE PLAYER, but recieving the values direct from the post request and using the Player.objects.get_or_create to save the player.

# def new_player1(request):

#     if request.method == 'POST':
#         form = NewPlayerForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']

#             print (name)

#     form = NewPlayerForm()
#     return render(request, 'manager/new_player1.html', {'newplayerform': form})
# THE ABOVE IS A STANDARD FORM TO CREATE A PLAYER

def new_player(request):

    if request.method == 'POST':
        form = NewPlayerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Player has been created')
            print ("CreatedPlayer")
            return redirect('manager-home')

    form = NewPlayerForm()

    return render(request, 'manager/new_player1.html', {'newplayerform': form})


# class update_player(UpdateView):
#     model = Player
#     fields = ['name']
#     template_names = 'manager/update_player.html'
#     context_object_name = 'updateplayerform'


# def update_player(request):
#     # instance = get_object_or_404(Player, id=id)
#     # form = UpdatePlayerForm(request.POST or None, instance=instance)
#     form = UpdatePlayerForm()

#     context = {

#         'updateplayerform': form
#     }


#     if form.is_valid():
#         form.save()
#         print("updated player")
#     return render(request, 'manager/update_player.html', context)

def update_player(request):
    if request.method == "POST":
        form = UpdatePlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.save()
            return redirect('manager-players_detail', pk=player.pk)
    else:
        form = UpdatePlayerForm()
    return render(request, 'manager/update_player.html', {'form': form})


def player_edit(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == "POST":
        form = UpdatePlayerForm(request.POST, instance=player)
        if form.is_valid():
            player = form.save(commit=False)
            player.save()
            return redirect('manager-players_detail', pk=player.pk)
    else:
        form = UpdatePlayerForm(instance=player)
    return render(request, 'manager/update_player.html', {'form': form})


def new_playerstats(request):

    if request.method == 'POST':
        form = NewPlayerForm(request.POST)
        if form.is_valid():
            form.save()
            print ("AddedPlayerStats")

    form = playerstats()
    return render(request, 'manager/new_playerstats.html', {'playerstats': form})


def winner(request):
    # get all players, teams and matches
    players = Player.objects.all()
    teams = Team.objects.all()
    matches = Match.objects.all()

    # get dates with matches
    dates = []
    for match in matches:
        dates.append(match.date.strftime('%Y-%m-%d'))

    # get only unique dates
    dates = list(set(dates))
    dates.sort(key=lambda x: time.mktime(time.strptime(x, "%Y-%m-%d")))
    print(dates)

    # assign goals to the team on that date

    content = {
        'players': players,
        'teams': teams,
        'matches': matches,
        'dates': dates,
    }

    if request.method == 'POST':
        # get goals result
        goals_team_a = request.POST.get('goals_team_a')
        goals_team_b = request.POST.get('goals_team_b')

        if not goals_team_a.isdigit() or not goals_team_b.isdigit():
            messages.warning(request, f'Please enter numbers (0,1,2,3...) for Goals please')

        # get winner id
        if goals_team_a.isdigit() and goals_team_b.isdigit():
            if goals_team_a > goals_team_b:
                team_id = 1
            elif goals_team_a < goals_team_b:
                team_id = 2
            else:
                team_id = 0

            # get match date
            match_date = request.POST.get('date')

            # update database with winner and looser of the match or as tied match
            if team_id != 0:
                won = Match.objects.filter(team__id=team_id).filter(date=match_date).update(won=True)
                lost = Match.objects.exclude(team__id=team_id).filter(date=match_date).update(won=False)
                messages.success(request, f'Match has been updated')
            else:
                tie = Match.objects.filter(date=match_date).update(won=None)
                messages.success(request, f'Match has been updated')

            # update database with each team goals
            goals_team_a = Match.objects.filter(team__id=1).filter(date=match_date).update(goals=goals_team_a)
            goals_team_b = Match.objects.filter(team__id=2).filter(date=match_date).update(goals=goals_team_b)

            # Assign points depending on the matches won
            for player in players:
                wins = Match.objects.filter(player__name=player.name).filter(won=True)
                ties = Match.objects.filter(player__name=player.name).filter(won=None)
                points = len(wins) * 3 + len(ties)
                player = Player.objects.filter(name=player.name).update(points=points)

    return render(request, 'manager/winner.html', content)


def weather(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=5715b122da9a97c73fd770a2c0b32d2d'
    city = 'London'
    # city1 = 'Hatfield'

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        response = requests.get(url.format(city)).json()
        # response1 = requests.get(url.format(city1)).json()

        # create a dictionary to store the response values I am interested in

        city_weather = {
            'city': city.name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

        # city_weather1 = {
        #     'city': city1,
        #     'temperature': response1['main']['temp'],
        #     'description': response1['weather'][0]['description'],
        #     'icon': response1['weather'][0]['icon'],
        # }

    print (city_weather)

    context = {'city_weather': weather_data}
    print(weather_data)

    context = {'weather_data': weather_data}
    return render(request, 'manager/weather.html', context)
