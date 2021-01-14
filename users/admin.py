from django.contrib import admin
from .models import User, Passenger

# Register your models here.

class UserModelAdmin(admin.ModelAdmin):
	list_display = ["username", "password"]           
	
	class Meta:                     
		model = User

class PassengerModelAdmin(admin.ModelAdmin):
	pass

admin.site.register(User, UserModelAdmin)
admin.site.register(Passenger, PassengerModelAdmin)