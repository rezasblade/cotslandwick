from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm  # , PostScoreUpdate
from django import forms

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, you can now log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


@staff_member_required
def scoreupdateview(request):
    #     if request.method == 'POST':
    #         scoreupd_form = PostScoreUpdate(request.POST)
    #         if scoreupd_form.is_valid():
    #             scoreupd_form.save()
    #             return redirect('manager-home')
    #     else:
    #         scoreupd_form = PostScoreUpdate()

    #     return render(request, 'users/scoreupdate.html', {'scoreupd_form': scoreupd_form})
    # # fields = ['matchdate', 'redsscore', 'bluescore']

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

    # return render(request, 'winner.html', content)
    return render(request, 'users/scoreupdate.html', content)
