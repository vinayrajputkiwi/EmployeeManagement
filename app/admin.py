from django.contrib import admin
from.models import checkin,checkout,registeremp
# Register your models here.

@admin.register(checkin)
class AdminCheckin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','date_time']

@admin.register(checkout)
class AdminCheckout(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','date_time']

@admin.register(registeremp)
class Adminregisteremp(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','identification_type','identification',
    'gender','mother_name','phone_number','address','country','vehicle_type','vehicle_name',]