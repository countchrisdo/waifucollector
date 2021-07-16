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
  path('waifus/<int:waifu_id>/add_cameo/', views.add_cameo, name='add_cameo'),
  
  path('waifus/<int:waifu_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
  path('waifus/<int:waifu_id>/unassoc_accessory/<int:accessory_id>/', views.unassoc_accessory, name='unassoc_accessory'),
#   path('waifus/<int:waifu_id>/add_photo/', views.add_photo, name='add_photo'),
  path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
  path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
  path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
  path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
  path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),

  path('waifus/<int:waifu_id>/add_photo/', views.add_photo, name='add_photo'),
]