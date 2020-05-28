from django.shortcuts import render
from agents.models import Agent
from django.http import HttpResponseRedirect


def general_city(request, city_url):
    city_list = {elem.city for elem in Agent.objects.all()}
    city_list = sorted(city_list)
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

    if city_url not in city_list:
        city_url = 'Ваш Город'
    return render(request, 'general/index.html', {
        'city': city_url,
        'city_list': city_list,
        'persons': persons,
    })


def first_page(request):
    return HttpResponseRedirect('Курск')
