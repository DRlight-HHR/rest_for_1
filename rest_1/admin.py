from django.contrib import admin
from .models import book, temp


class update(admin.ModelAdmin):
    search_fields = ["name", 'auth']
    list_display = ["name", 'auth']


admin.site.register(book, update)
admin.site.register(temp)
