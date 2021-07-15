from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Waifu
from .forms import CameoForm

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def waifus_index(request):
  waifus = Waifu.objects.all()
  return render(request, 'waifus/index.html', { 'waifus': waifus })

def waifus_detail(request, waifu_id):
  waifu = Waifu.objects.get(id=waifu_id)
  # instanciate CameoForm to be rendered in the template
  cameo_form = CameoForm()
  return render(request, 'waifus/detail.html', { 'waifu': waifu, 'cameo_form': cameo_form })


class WaifuCreate(CreateView):
  model = Waifu
  fields = '__all__'

class WaifuUpdate(UpdateView):
  model = Waifu
  fields = '__all__'

class WaifuDelete(DeleteView):
  model = Waifu
  success_url = '/waifus/'

def add_cameo(request, waifu_id):
  # create a ModelForm instance using the data in request.POST
  form = CameoForm(request.POST)
  waifu = Waifu.objects.get(id=waifu_id)
# validate the form
  if form.is_valid():
       # don't save the form to the db until it
    # has the waifu_id assigned
    new_cameo = form.save(commit=False)
    new_cameo.waifu_id = waifu_id
    new_cameo.save()
    return redirect('detail', waifu_id=waifu_id)