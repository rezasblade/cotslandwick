from django.db import models
from django.db.models import Count
from django.urls import reverse


class Player(models.Model):
    name = models.CharField(max_length=50, unique=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=24)
    player = models.ManyToManyField(Player, through='Match')

    def __str__(self):
        return self.name


class Match(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    won = models.BooleanField(blank=True, null=True)
    date = models.DateField()
    goals = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.player} - {self.team} - {self.won}"

# class Player(models.Model):

#     name = models.CharField(max_length=128, null=True)
#     matches = models.ManyToManyField("MatchDay", through="PlayerPoints")

#     def __str__(self):
#         return self.name


# class MatchDay(models.Model):
#     matchdate = models.DateField(primary_key=True)
#     matchtype = models.CharField(max_length=128, null=True)

#     def __str__(self):
#         return '%s %s' % (self.matchdate, self.matchtype)


# class Results(models.Model):
#     matchdate = models.ForeignKey(MatchDay, null=True, blank=True, on_delete=models.SET_NULL)
#     redsscore = models.IntegerField()
#     bluescore = models.IntegerField()

#     def __str__(self):
#         return '%s %s %s' % (self.matchdate, self.redsscore, self.bluescore)

#     def get_absolute_url(self):
#         # return reverse('results-detail', kwargs={'pk': self.pk})
#         return reverse('manager-home')


# class PlayerPoints(models.Model):
#     name = models.ForeignKey(Player, null=True, blank=True, on_delete=models.SET_NULL)
#     matchdate = models.ForeignKey(MatchDay, null=True, blank=True, on_delete=models.SET_NULL)
#     goals = models.IntegerField()
#     assists = models.IntegerField()

#     def __str__(self):
#         # return '%s %s(Match Date) %s goals, and %s assists' % (self.name, self.matchdate, self.goals, self.assists)
#         return '%s %s %s %s' % (self.name, self.matchdate, self.goals, self.assists)
