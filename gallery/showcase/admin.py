from django.contrib import admin

from .models import ArtPiece, Gallery


class ArtPieceInline(admin.TabularInline):
    fields = ['title', 'artist', 'image', 'gallery', 'pub_date']
    model = ArtPiece
    extra = 1


class GalleryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [ArtPieceInline]
    list_display = ('name',)
    search_fields = ['name',]

class ArtPieceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'artist', 'image', 'gallery', 'pub_date']}),
    ]
    list_filter = ['artist', 'pub_date']
    search_fields = ['title', 'artist']


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(ArtPiece, ArtPieceAdmin)
