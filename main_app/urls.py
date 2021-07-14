from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('waifus/', views.waifus_index, name='index'),
    path('waifus/<int:waifu_id>/', views.waifus_detail, name='detail'),
    path('waifus/create/', views.WaifuCreate.as_view(), name='waifus_create'),
    path('waifus/<int:pk>/update/', views.WaifuUpdate.as_view(), name='waifus_update'),
    path('waifus/<int:pk>/delete/', views.WaifuDelete.as_view(), name='waifus_delete'),
]