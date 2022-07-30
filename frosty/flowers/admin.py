from django.contrib import admin
from .models import User, Flower, Lot, Feedback, Deal, DealLots


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role')


class FlowersAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'description')


class LotAdmin(admin.ModelAdmin):
    list_display = ('item', 'price', 'stock', 'available')
    list_select_related = ['item']


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('author', 'seller', 'lot', 'text')


class DealLotsAdmin(admin.TabularInline):
    model = DealLots
    extra = 0


class DealAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'seller')
    inlines = [DealLotsAdmin]


admin.site.register(Deal, DealAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Flower, FlowersAdmin)
admin.site.register(Lot, LotAdmin)
