from django.db import models
import datetime

class Comentarios(models.Model):
	poster = models.CharField(max_length=20, verbose_name = 'Nombre')
	website = models.URLField(max_length=50, null=True)
	coment = models.CharField(max_length=150)
	fecha = models.DateField(null=True)
	hora = models.CharField(max_length=8, null=True)

	def __unicode__(self):
		return self.poster + ' ' + self.coment

	class Meta:
	    ordering = ['poster', 'hora']
	    verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

