from django import forms
from .models import Player


# class NewPlayerForm(forms.Form):
#     name = forms.CharField()


class PlayerStats(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('name', 'goalsscored', 'assists', 'motmawards')
