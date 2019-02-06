from django import forms
from .models import Player


# class NewPlayerForm(forms.Form):
#     name = forms.CharField()


class NewPlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('name', 'preferredfoot', 'position', 'trait')


class UpdatePlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ['name', 'preferredfoot', 'position', 'trait']
