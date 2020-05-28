from django.urls import path

from . import views

app_name = 'general'
urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('<str:city_url>/', views.general_city, name='city_url'),
]
