from django import forms as forms
from models import *
import datetime

class FeedBackForm(forms.ModelForm):
	date = datetime.date.today()
	hoy = date.strftime("%Y-%m-%d")	
	nombre = forms.CharField(label=u'Nombre (*) ')
	mensaje = forms.CharField(label=u"Sugerencia (*) ", widget=forms.Textarea())
	#site =  forms.CharField(label=u"Sitio Web", initial="www.tu-web.com")
	fecha = forms.DateField(label=u"", initial=hoy)
	
	class Meta:
		model = Feedback
		exclude = ['site']
