from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.db.models import Q
from django.core.exceptions import ValidationError
from .models import Match, Team
from django.template import loader
import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '4e89e43e91b341d6a13e9d2b7a7c939d' }


def get_matches():
    connection.request('GET', '/v2/competitions/BL1/matches', None, headers )
    response = json.loads(connection.getresponse().read().decode())
    matches = response["matches"]
    for match in matches:
        homeTeam = match["homeTeam"]["name"]
        homeScore = match["score"]["fullTime"]["homeTeam"]
        awayTeam = match["awayTeam"]["name"]
        awayScore = match["score"]["fullTime"]["awayTeam"]
        matchID = match["id"]
        match_status = match["status"]
        m, created = Match.objects.get_or_create(match_number = matchID)
        m.home_team = homeTeam
        m.away_team = awayTeam
        m.home_score = homeScore
        m.away_score = awayScore
        m.status = match_status
        if(m.status == 'FINISHED'):
            m.setResult()
        m.save()        

# def get_teams():
#     connection.request('GET', '/v2/competitions/BL1/matches', None, headers )
#     response = json.loads(connection.getresponse().read().decode())
#     matches = response["matches"]
#     for match in matches:
#         print(match)
# get_teams()
    
def home(request):
    context = {}
    return render(request, 'liveTables/homePage.html', context)

def past(request):
    get_matches()
    matches = Match.objects.filter(status = 'FINISHED')
    template = loader.get_template('liveTables/pastMatchList.html')
    context = {
        'matches': matches,
    }
    return HttpResponse(template.render(context, request))

def live(request):
    get_matches()
    matches = Match.objects.filter(status = 'PAUSED') or Match.objects.filter(status = 'IN_PLAY') or Match.objects.filter(status = 'LIVE')
    template = loader.get_template('liveTables/liveMatchList.html')
    context = {
        'matches': matches,
    }
    return HttpResponse(template.render(context, request))

def schedule(request):
    get_matches()
    matches = Match.objects.filter(status = 'SCHEDULED')
    template = loader.get_template('liveTables/scheduledMatchList.html')
    context = {
        'matches': matches,
    }
    return HttpResponse(template.render(context, request))
