from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView



from .models import Waifu

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
  return render(request, 'waifus/detail.html', { 'waifu': waifu })

# # http request to get image from api
# def get_image(request):
#   url = 'http://api.adorable.io/avatars/100/'
#   r = requests.get(url)
#   waifuimg = r.json()
#   return HttpResponse(waifu.image, content_type='image/png')


# http request to get a list of waifus 
def APIimg(request):
  url = 'http://api.adorable.io/avatars/100/'
  r = requests.get(url)
  waifus = r.json()
  return render(request, 'waifus/index.html', { 'waifus': waifus })


class WaifuCreate(CreateView):
  model = Waifu
  fields = '__all__'

class WaifuUpdate(UpdateView):
  model = Waifu
  fields = '__all__'

class WaifuDelete(DeleteView):
  model = Waifu
  success_url = '/waifus/'