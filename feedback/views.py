from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
from django.core.mail import send_mail
from django.http import *
from forms import *
from models import *

import datetime
import json

def feedback(request):
	form = FeedBackForm()
	return render_to_response('feedback/index.html', {'form':form})

def enviar(request):
	if request.is_ajax():		
		try:
			sug = Feedback()
			sug.nombre = request.POST['nombre']
			sug.email = request.POST['email']
			#sug.website = request.POST['site']
			sug.mensaje = request.POST['mensaje']
			sug.fecha = getFecha()
			sug.save()
			
			#variables para enviar correo a administradores
			nombre = request.POST['nombre']
			email_poster = request.POST['email']
			mensaje = request.POST['mensaje']
			fecha_sugerencia = getFecha()			
			
			subject = 'Sugerencias @ Portal Viejano'			
			sugerencia = render_to_string('feedback/texto-feedback.txt', RequestContext(request, locals()))
			to_list = ['helmygb@gmail.com', 'rbnmarquez86@gmail.com']		
			send_mail(subject, sugerencia, email_poster, to_list)
			return HttpResponse(json.dumps({'poster': sug.nombre}), mimetype='application/json')
		
		except:			
			return HttpResponse('ERROR')
	
	return HttpResponse('ERROR')

#funcion para obtener la fecha
def getFecha():
	fecha = datetime.date.today()
	hoy = fecha.strftime("%Y-%m-%d")

	return hoy

