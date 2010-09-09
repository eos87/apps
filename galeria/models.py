from django.db import models
from django.template.defaultfilters import slugify
import datetime

class Album(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=200, null=True, blank=True)
    slug = models.CharField(max_length=100, editable=False, unique=True)

    def __unicode__(self):
        return self.nombre

    def save(self):
        self.slug = slugify(self.nombre)
        super(Album, self).save()


class Foto(models.Model):
    album = models.ForeignKey(Album)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=400)

    def __unicode__(self):
        return "%s-%s" % (self.id, self.nombre)

class Comentario(models.Model):
    foto = models.ForeignKey(Foto)
    usuario = models.CharField(max_length=60)
    comentario = models.TextField()
    fecha = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return "Comentario de %s" % self.usuario

    class Meta:
        ordering = ['fecha']        
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

