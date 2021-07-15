from django.forms import ModelForm
from .models import Cameo

class CameoForm(ModelForm):
  class Meta:
    model = Cameo
    fields = ['title', 'medium', 'description']