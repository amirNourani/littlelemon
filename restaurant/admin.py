from django.contrib import admin
from .models import Booking, Menu


# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ["name", "no_of_guests", "booking_data"]


class MenuAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "inventory"]


admin.site.register(Booking, BookingAdmin)
admin.site.register(Menu, MenuAdmin)
