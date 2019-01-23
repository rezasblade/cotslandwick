from django.db import models
from django.db.models import Count
from django.urls import reverse


class Player(models.Model):

    GOALKEEPER = 'GK'
    DEFENDER = 'DF'
    MIDFIELDER = 'MF'
    STRIKER = 'ST'
    POSITION_CHOICES = (
        (GOALKEEPER, 'Goalkeeper'),
        (DEFENDER, 'Defender'),
        (MIDFIELDER, 'Midfielder'),
        (STRIKER, 'Striker'),
    )

    RIGHT = 'RT'
    LEFT = 'LT'
    BOTH = 'BT'

    FOOT_CHOICE = (
        (RIGHT, 'Right'),
        (LEFT, 'Left'),
        (BOTH, 'Both'),
    )

    name = models.CharField(max_length=128, null=True)
    position = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
        default=DEFENDER,
    )

    preferred_foot = models.CharField(max_length=5, choices=FOOT_CHOICE, default=RIGHT)
    trait = models.TextField(max_length=50, default="")

    totalwins = models.IntegerField(default=0)
    totallosses = models.IntegerField(default=0)
    totaldraws = models.IntegerField(default=0)
    totalpoints = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=128, null=True)

    def __str__(self):
        return '%s' % (self.name)


class MatchDay(models.Model):
    matchdate = models.DateField(primary_key=True)

    FIVEASIDE = '5'
    EIGHTASIDE = '8'

    MATCH_CHOICE = (
        (FIVEASIDE, '5-a-side'),
        (EIGHTASIDE, '8-a-side'),
    )

    matchtype = models.CharField(
        max_length=10,
        choices=MATCH_CHOICE,
        default=FIVEASIDE,
    )
    # matchtype = models.CharField(max_length=128, null=True)

    def __str__(self):
        return '%s' % (self.matchdate)


class MatchDaySquadRed(models.Model):
    matchdate = models.ForeignKey(MatchDay, null=True, blank=True, on_delete=models.SET_NULL)
    playername = models.ManyToManyField(Player)
    teamname = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '%s' % (self.matchdate)


class MatchDaySquadBlue(models.Model):
    matchdate = models.ForeignKey(MatchDay, null=True, blank=True, on_delete=models.SET_NULL)
    playername = models.ManyToManyField(Player)
    teamname = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '%s' % (self.matchdate)


class Results(models.Model):
    matchdate = models.ForeignKey(MatchDay, null=True, blank=True, on_delete=models.SET_NULL)
    redsscore = models.IntegerField()
    bluescore = models.IntegerField()
    winner = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '%s %s %s %s' % (self.matchdate, self.redsscore, self.bluescore, self.winner)

    def get_absolute_url(self):
        # return reverse('results-detail', kwargs={'pk': self.pk})
        return reverse('manager-home')


class PlayerPoints(models.Model):
    name = models.ForeignKey(Player, null=True, blank=True, on_delete=models.SET_NULL)
    matchdate = models.ForeignKey(MatchDay, null=True, blank=True, on_delete=models.SET_NULL)
    goals = models.IntegerField()
    assists = models.IntegerField()

    def __str__(self):
        # return '%s %s(Match Date) %s goals, and %s assists' % (self.name, self.matchdate, self.goals, self.assists)
        return '%s %s %s %s' % (self.name, self.matchdate, self.goals, self.assists)
