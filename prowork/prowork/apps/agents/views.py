from django.shortcuts import render
from .models import Agent
from django.http import HttpResponseRedirect # , Http404
# from django.urls import reverse


def index_city(request, city_url):
    workers_list = Agent.objects.filter(city=city_url).order_by('priority')
    for worker in workers_list:
        worker.serv = worker.services.split('\n')
    city_list = {elem.city for elem in Agent.objects.all()}
    city_list = sorted(city_list)
    if city_url not in city_list:
        city_url = 'Выбрать город'
    persons = [elem for elem in Agent.objects.filter(city=city_url)]
    # tmp_city = []
    # for i in persons:
    #     if i.city not in tmp_city:
    #         tmp_city.append(i.city)
    
    professions = []
    for i in persons:
        if i.profession not in professions:
            professions.append(i.profession)
        else:
            persons.remove(i)
                        
    return render(request, 'agents/index.html', {
        'workers_list': workers_list,
        'city': city_url,
        'city_list': city_list,
        'persons': persons,
    })


def pro(request, city_url, pro):
    workers_list = Agent.objects.filter(city=city_url).filter(profession=pro).order_by('priority')
    for worker in workers_list:
        worker.serv = worker.services.split('\n')
    city_list = {elem.city for elem in Agent.objects.all()}
    city_list = sorted(city_list)
    if city_url not in city_list:
        city_url = 'Выбрать город'
    persons = [elem for elem in Agent.objects.filter(city=city_url)]
    # tmp_city = []
    # for person in persons:
    #     if person.city not in tmp_city:
    #         tmp_city.append(person.city)
    
    professions = []
    for i in persons:
        if i.profession not in professions:
            professions.append(i.profession)
        else:
            persons.remove(i)
            
    
    return render(request, 'agents/index.html', {
        'workers_list': workers_list,
        'city': city_url,
        'city_list': city_list,
        'persons': persons,
    })


def index(request):
    return HttpResponseRedirect('Курск')
