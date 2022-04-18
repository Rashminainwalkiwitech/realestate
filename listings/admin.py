from django.contrib import admin

# Register your models here.
from . models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published','price','list_date','realtor')
    list_display_links = ('id','title')
    list_filter = ('realtor',)
    list_editable = ('is_published',) #is_published is used for showing data in front end if we not click on it .it does not show any data in frontend
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price') #for searching the data
    list_per_page = 25
admin.site.register(Listing, ListingAdmin)


