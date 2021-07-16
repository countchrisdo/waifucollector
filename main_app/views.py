from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

import uuid
import boto3
import os

from .models import Accessory, Waifu, Photo
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
  accessoriesNull = Accessory.objects.exclude(id__in=waifu.accessories.all().values_list('id'))
  cameo_form = CameoForm()
  return render(request, 'waifus/detail.html', { 'waifu': waifu, 
  'cameo_form': cameo_form,
  'accessories': accessoriesNull })


class WaifuCreate(CreateView):
  model = Waifu
  fields = ['name', 'series', 'description'] 

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

class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'color']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories/'

def assoc_accessory(request, waifu_id, accessory_id):
  Waifu.objects.get(id=waifu_id).accessories.add(waifu_id)
  return redirect('detail', waifu_id=waifu_id)

def unassoc_accessory(request, waifu_id, accessory_id):
  Waifu.objects.get(id=waifu_id).accessories.remove(accessory_id)
  return redirect('detail', waifu_id=waifu_id)

def add_photo(request, waifu_id):
  # photo-file will be the "name" attribute on the <input>
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # build a unique filename keeping the image's original extension
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, waifu_id=waifu_id)
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', waifu_id=waifu_id)
