from django.urls import path

from . import views

app_name = 'agents'
urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('<str:city_url>/', views.general_city, name='city_url'),
]
