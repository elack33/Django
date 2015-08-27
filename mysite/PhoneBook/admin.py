from django.contrib import admin

# Register your models here.
from PhoneBook.models import Entry, City, State, Zip

class EntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Entry, EntryAdmin)

class CityAdmin(admin.ModelAdmin):
    pass
admin.site.register(City, CityAdmin)

class StateAdmin(admin.ModelAdmin):
    pass
admin.site.register(State, StateAdmin)

class ZipAdmin(admin.ModelAdmin):
    pass
admin.site.register(Zip, ZipAdmin)


