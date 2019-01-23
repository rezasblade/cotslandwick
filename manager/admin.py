from django.contrib import admin
# from .models import Player
# from .models import Team
# from .models import Venue
# from .models import Match
# from .models import Result
# from .models import PlayerPoint

from .models import Player
from .models import MatchDay
from .models import MatchDaySquadRed
from .models import MatchDaySquadBlue
from .models import Results
from .models import Team
from .models import PlayerPoints

# Register your models here.

# admin.site.register(Player)
# admin.site.register(Team)
# admin.site.register(Venue)
# admin.site.register(Match)
# admin.site.register(Result)
# admin.site.register(PlayerPoint)

admin.site.register(Player)
admin.site.register(MatchDay)
admin.site.register(MatchDaySquadRed)
admin.site.register(MatchDaySquadBlue)
admin.site.register(Results)
admin.site.register(Team)
admin.site.register(PlayerPoints)
