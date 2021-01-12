from django.contrib import admin

from .models import Station, Train, Ticket, LockedSeat, Route

class StationAdmin(admin.ModelAdmin):
    pass

class TrainAdmin(admin.ModelAdmin):
    pass

class RouteAdmin(admin.ModelAdmin):
    pass

class TicketAdmin(admin.ModelAdmin):
    pass

class LockedSeatAdmin(admin.ModelAdmin):
    pass

admin.site.register(Station, StationAdmin)
admin.site.register(Train, TrainAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(LockedSeat, LockedSeatAdmin)
