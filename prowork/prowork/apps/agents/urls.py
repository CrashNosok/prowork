from django.urls import path

from . import views

app_name = 'agents'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:city_url>/', views.index_city, name='city_url'),
    path('<str:city_url>/<str:pro>/', views.pro, name='pro'),
]
