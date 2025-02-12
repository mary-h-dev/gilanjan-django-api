from django.contrib import admin
from .models import Festival

@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'location')
    list_filter = ('is_active', 'start_date', 'location')
    date_hierarchy = 'start_date'
    ordering = ('-start_date',)
