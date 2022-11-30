from django.contrib import admin

from .models import Address, City, Shop


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'city')
    ordering = ('-city',)


class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'opening_time', 'closing_time')


admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Shop, ShopAdmin)
