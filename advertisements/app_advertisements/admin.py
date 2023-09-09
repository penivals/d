from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','price','created_at','auction']
    list_filter = ['auction','created_at']
    auction = ['make_auction_as_false']

    @admin.action(description='Убрать возможность торга.')
    def make_auction_as_false(self,request, queryset):
        queryset.update (auction = False)


admin.site.register(Advertisement,AdvertisementAdmin)


# Register your models here.
