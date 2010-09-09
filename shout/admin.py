from apps.shout.models import *
from apps.galeria.models import *
from django.contrib import admin

admin.site.register(Comentarios,
        list_display = ['poster', 'coment', 'fecha', 'hora'],
        list_filter = [ 'poster', 'fecha'],
        ordering = ['-fecha'],
        search_fields = ['poster'],
        )

class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 1

class FotoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'album', 'url')
    fieldsets = [
        (None,               {'fields': ['nombre']}),
        ('Informacion de foto', {'fields': ['album', 'descripcion'], 'classes': ['collapse']}),
    ]
    inlines = [ComentarioInline]

admin.site.register(Album)
admin.site.register(Foto, FotoAdmin)
admin.site.register(Comentario,
    list_display = ['id', 'usuario', 'fecha', 'comentario'],
    search_fields = [ 'usuario', 'fecha'],    
)
