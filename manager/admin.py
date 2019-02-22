from django.contrib import admin

from .models import Player, Team, Match, City

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Match)
# admin.site.register(City)


# from .models import Player
# from .models import MatchDay
# from .models import Results
# from .models import PlayerPoints

# # Register your models here.


# admin.site.register(Player)
# admin.site.register(MatchDay)
# admin.site.register(Results)
# # admin.site.register(PlayerPoints)

# # Define the admin class


# class PlayerPointsAdmin(admin.ModelAdmin):
#     pass


# # Register the admin class with the associated model
# admin.site.register(PlayerPoints, PlayerPointsAdmin)
