from django.contrib import admin

from .models import Item

#add a class so I can customize interface.
class ItemAdmin(admin.ModelAdmin):
	list_display = ['title', 'amount']

#register our model with the admin
admin.site.register(Item, ItemAdmin)
