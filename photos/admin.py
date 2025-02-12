from django.contrib import admin
from .models import Gallery, Photo



class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [PhotoInline]
