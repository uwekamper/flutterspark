# -*- coding: utf-8 -*-
import requests

def get_tweets(hashtag):
    url = u'http://loklak.org:9000/api/search.json?q={}&source=twitter&minified=true'.format(hashtag)
    resp = requests.get(url)
    data = resp.json()
    return data
