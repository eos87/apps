from django.shortcuts import render_to_response
from django.http import *
from forms import CommentsForm
from models import Comentarios

import json

def index(request):
	coments = Comentarios.objects.all().order_by('-id')[:50]
	form = CommentsForm()
	return render_to_response('index.html', {'form': form, 'coments': coments})

def add(request):
	if request.is_ajax():
		try:
			comentarios = Comentarios()
			comentarios.poster = request.POST['poster']
			#comentarios.website = request.POST['website']
			comentarios.coment = request.POST['coment']
			comentarios.fecha = request.POST['fecha']
			comentarios.hora = request.POST['hora']
			comentarios.save()
			return HttpResponse(json.dumps({'poster': comentarios.poster, 'coment': comentarios.coment, 'fecha': comentarios.fecha, 'hora': comentarios.hora }), mimetype='application/json')
		except:
			return HttpResponse('ERROR')
	return HttpResponse('ERROR')

