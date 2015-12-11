# -*- coding: utf-8 -*-
import re
import requests
import base64
import struct
import random
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from dateutil.parser import parse

class Tweet(object):
    def __init__(self, status):
        self.screen_name = status['screen_name']
        self.text = status['text']
        self.classification = None
        self.created_at = parse(status['created_at'])
        self.image_url = status['user']['profile_image_url_https']
        self.lat = self.vector[-2]
        self.long = self.vector[-1]

    def classify(self, classification):
        self.classification = classification

    @property
    def vector(self):
        val = extract_brainstate(self.text)
        if val == None:
            return (1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        else:
            return val

    @property
    def theta(self):
        return abs(self.vector[0])

    @property
    def alpha(self):
        return abs(self.vector[1])

    @property
    def beta(self):
        return abs(self.vector[2])

    @property
    def fmax(self):
        return abs(self.vector[3])

    @property
    def color(self):
        overall_density = self.theta + self.alpha + self.beta
        r = int(self.alpha / overall_density * 255)
        g = int(self.beta / overall_density * 255)
        b = int(self.theta / overall_density * 255)
        return u'#%02x%02x%02x' % (r, g, b)

    def __str__(self):
        if self.vector != None:
            return u'<@{}: {} {} [{}]>'.format(self.screen_name, self.text[:20], self.vector,
                                               self.classification)
        else:
            return u'<@{}: {} [{}]>'.format(self.screen_name, self.text[:20], self.classification)


def get_tweets(hashtag):
    url = u'http://loklak.org:9000/api/search.json?q={}&minified=true'.format(hashtag)
    resp = requests.get(url)
    data = resp.json()['statuses']
    tweets = []
    for status in data:
        tweets.append(Tweet(status))
    return tweets

def extract_brainstate(text):
    match = re.search(r' [A-Za-z0-9+/=]{24,32} ', text)
    if not match:
        return None
    else:
        raw_brains = match.group(0).strip()
        decoded_brains = base64.b64decode(raw_brains)
        if len(raw_brains) == 24:
            bla = struct.unpack('4f', decoded_brains)
            cooked_brains = (bla[0], bla[1], bla[2], bla[3],
                52.541576 + random.random() / 500, 13.390394 + random.random() / 500)
        else:
            cooked_brains = struct.unpack('6f', decoded_brains)
        return cooked_brains

def cluster_brains(brains):
    vectors = [t.vector for t in brains]
    scaled_vectors = scale(vectors)
    model = KMeans(n_clusters=2)
    results = model.fit_predict(scaled_vectors)
    for result, brain in zip(results, brains):
        brain.classify(result)
    return model, results

def find_latest(tweets):
    latest = {}
    for t in tweets:
        if t.screen_name in latest.keys():
            if latest[t.screen_name].created_at < t.created_at:
                latest[t.screen_name] = t
        else:
            latest[t.screen_name] = t
    return latest



