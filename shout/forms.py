from django import forms as forms
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime
from django.contrib.admin import widgets
from models import Comentarios

class CommentsForm(forms.ModelForm):
	coment = forms.CharField(label=u"Mensaje", widget=forms.Textarea(), max_length=20)
	#fecha = forms.DateField(label=u"Fecha", input_formats=['%d-%m-%Y'], widget=AdminDateWidget())		
	#hora = forms.TimeField(input_formats=['%H:%M'])
	
	class Meta:
		model = Comentarios		
		exclude = ['website', 'fecha', 'hora']
