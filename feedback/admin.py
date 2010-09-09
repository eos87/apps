from apps.feedback.models import *
from django.contrib import admin

admin.site.register(Feedback,
	list_display = ['nombre', 'email', 'site', 'mensaje', 'fecha'], 
	list_filter = ['nombre', 'site', 'fecha'], 
	ordering = ['fecha', 'nombre'], 
	search_fields = ['nombre'],
)
