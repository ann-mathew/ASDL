from django.contrib import admin

from .models import Station, Train, Ticket

class StationAdmin(admin.ModelAdmin):
    pass

class TrainAdmin(admin.ModelAdmin):
    pass


class TicketAdmin(admin.ModelAdmin):
    pass

admin.site.register(Station, StationAdmin)
admin.site.register(Train, TrainAdmin)
admin.site.register(Ticket, TicketAdmin)
