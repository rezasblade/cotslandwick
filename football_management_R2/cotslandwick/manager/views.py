import time

from django.shortcuts import render

from .models import Player, Match, Team


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
        won_matches = len(won.filter(player__name=player.name))
        lost_matches = len(lost.filter(player__name=player.name))
        tie_matches = len(tie.filter(player__name=player.name))
        points = won_matches * 3 + tie_matches
        player_stats.append([player.name, won_matches, tie_matches, lost_matches, points])

    content = {
        'player_stats': player_stats
    }

    return render(request, 'manager/players.html', content)


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
        if team_a != team_b:
            different = True

        if request.POST['date'] is not None and different:
            date = request.POST['date']
            team_a = Team.objects.get(name=team_a)
            team_b = Team.objects.get(name=team_b)

            # fetch players names
            if request.POST['name1'] is not None:
                player1 = request.POST['name1']
                player1, created = Player.objects.get_or_create(
                    name=player1
                )
                match1 = Match(
                    player=player1,
                    team=team_a,
                    date=date)
                match1.save()
            if request.POST['name2'] is not None:
                player2 = request.POST['name2']
                player2, created = Player.objects.get_or_create(
                    name=player2
                )
                match2 = Match(
                    player=player2,
                    team=team_a,
                    date=date)
                match2.save()
            if request.POST['name3'] is not None:
                player3 = request.POST['name3']
                player3, created = Player.objects.get_or_create(
                    name=player3
                )
                match3 = Match(
                    player=player3,
                    team=team_a,
                    date=date)
                match3.save()
            if request.POST['name4'] is not None:
                player4 = request.POST['name4']
                player4, created = Player.objects.get_or_create(
                    name=player4
                )
                match4 = Match(
                    player=player4,
                    team=team_a,
                    date=date)
                match4.save()
            if request.POST['name5'] is not None:
                player5 = request.POST['name5']
                player5, created = Player.objects.get_or_create(
                    name=player5
                )
                match5 = Match(
                    player=player5,
                    team=team_a,
                    date=date)
                match5.save()

            if request.POST['name6'] is not None:
                player6 = request.POST['name6']
                player6, created = Player.objects.get_or_create(
                    name=player6
                )
                match6 = Match(
                    player=player6,
                    team=team_b,
                    date=date)
                match6.save()
            if request.POST['name7'] is not None:
                player7 = request.POST['name7']
                player7, created = Player.objects.get_or_create(
                    name=player7
                )
                match7 = Match(
                    player=player7,
                    team=team_b,
                    date=date)
                match7.save()
            if request.POST['name8'] is not None:
                player8 = request.POST['name8']
                player8, created = Player.objects.get_or_create(
                    name=player8
                )
                match8 = Match(
                    player=player8,
                    team=team_b,
                    date=date)
                match8.save()
            if request.POST['name9'] is not None:
                player9 = request.POST['name9']
                player9, created = Player.objects.get_or_create(
                    name=player9
                )
                match9 = Match(
                    player=player9,
                    team=team_b,
                    date=date)
                match9.save()
            if request.POST['name10'] is not None:
                player10 = request.POST['name10']
                player10, created = Player.objects.get_or_create(
                    name=player10
                )
                match10 = Match(
                    player=player10,
                    team=team_b,
                    date=date)
                match10.save()

    return render(request, 'manager/new_match.html', content)


def new_player(request):

    if request.method == 'POST':
        if request.POST['new_player'] is not None:
            new_player = request.POST['new_player']
            new_player, created = Player.objects.get_or_create(
                name=new_player
            )

    return render(request, 'manager/new_player.html', {})


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
            else:
                tie = Match.objects.filter(date=match_date).update(won=None)

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
