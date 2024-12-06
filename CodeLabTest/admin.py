from django.contrib import admin
from CodeLabTest.models import Career

class Carrers(admin.ModelAdmin):
    list_display = ('id','username', 'title', 'content')
    list_display_links = ('id', 'username')
    list_per_page = 20
    search_fields = ('username',)

admin.site.register(Career,Carrers)