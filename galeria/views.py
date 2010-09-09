from apps.settings import *
from django.core.mail import send_mail
from django.http import *
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.template import RequestContext
from forms import *
from models import *
import json

def gallery(request, slug):
    album = Album.objects.get(slug=slug)
    images = Foto.objects.filter(album=album)
    return render_to_response('gallery.html', RequestContext(request, locals()))

def crear_galeria(request):
    if request.is_ajax():
        if request.POST['new_album'] != '':
            nombre = request.POST['new_album']
            try:
                new = Album()
                new.nombre = nombre
                new.save()
                return HttpResponse('<ul class="messagelist"><li>Album %s creado con exito</li></ul>' % nombre)
            except:
                return HttpResponse('<ul class="errornote"><li>Ese album ya existe, especifique otro nombre!</li></ul>')
        if request.POST['path']:
            path = request.POST['path']
            try:
                images = sorted([x for x in os.listdir(MEDIA_ROOT + '/' + path) if x.endswith('.jpg') or x.endswith('.png') or x.endswith('.JPG')])
                album = request.POST['path']
                new = Album.objects.get(slug=slugify(request.POST['id_album']))
                for i in images:
                    image = Foto()
                    image.album = new
                    image.nombre = i
                    image.url = IMAGES_ROOT + album + '/' + i
                    image.save()
                return HttpResponse(new.slug)
            except:
                return HttpResponse('<ul class="errornote"><li>No existe el directorio</li></ul>')

    return render_to_response('crear_galeria.html', RequestContext(request, locals()))

def crear_album(request):
    form = AlbumForm()
    return render_to_response('crear_album.html', RequestContext(request, locals()))

def create_comment(request):
    if request.is_ajax():
        id = request.POST['id']
        index = request.POST['index']

        nombre = request.POST['nombre']
        comentario = request.POST['comentario']
        foto = Foto.objects.get(id=id)
        new = Comentario()
        new.usuario = nombre
        new.comentario = comentario
        new.foto = foto
        new.fecha = datetime.datetime.now()
        new.save()

        if index != 'no':
            subject = 'New Comment Photo'
            contenido = render_to_string('new-comment.txt', RequestContext(request, locals()))
            send_mail(subject, contenido, 'info@portalviejano.com', ['rbnmarquez86@gmail.com', 'helmygb@gmail.com'])

        fecha = str(new.fecha.day)+' / '+str(new.fecha.month)+' / '+str(new.fecha.year)
        return HttpResponse(json.dumps({'usuario': new.usuario, 'comentario': new.comentario, 'fecha': fecha}), mimetype='application/json')
    return HttpResponse('END')

def get_comment(request):

    if request.is_ajax():
        id = request.POST['id']
        comentarios = Comentario.objects.filter(foto=Foto.objects.get(id=id))
        return render_to_response('comments.html', RequestContext(request, locals()))

