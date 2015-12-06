# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .clustering import get_tweets, find_latest

# Create your views here.

def index(request):
    screen_name = request.GET.get('screen_name', None)
    if screen_name != None:
        url = reverse_lazy('map', args=[screen_name])
        return HttpResponseRedirect(url)
    else:
        return render(request, 'mapview/base1.html', {})

def map(request, screen_name):
    all_tweets = get_tweets('flutterbrn')
    latest_tweets = find_latest(all_tweets)
    my_last = latest_tweets[screen_name]
    latest_list = latest_tweets.values()
    ctx = {
        'screen_name': screen_name,
        'all_tweets': all_tweets,
        'latest_tweets': all_tweets,
        'my_last': my_last,
        'latest_list': latest_list,
    }
    return render(request, 'mapview/map.html', ctx)
