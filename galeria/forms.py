from django import forms as forms
from models import *

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album