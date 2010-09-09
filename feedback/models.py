from django.db import models

#modelo para almacenar las sugerencias
class Feedback(models.Model):
	nombre = models.CharField(max_length=30)
	email = models.EmailField(null=True)
	site = models.URLField(max_length=50, null=True)
	mensaje = models.CharField(max_length=500)
	fecha = models.DateField(null=True)
	
	def __str__(self):
		return self.nombre + ' ' + self.mensaje
	
	class Meta:
		verbose_name = "Sugerencias"
		verbose_name_plural = "Sugerencias"	
