from __future__ import unicode_literals
from django.test import TestCase
from .clustering import get_tweets, extract_brainstate, cluster_brains, find_latest, Tweet

# Create your tests here.
class MapViewTests(TestCase):
    """
    TODO: Document the shit out of this class.
    """
    def test_get_tweets(self):
        """
        This is the test_get_tweets method. It tests get_tweets()!
        """
        brains = find_latest(get_tweets('flutterbrn')).values()
        model, result = cluster_brains(brains)
        for b in brains:
            print u'{}'.format(b)
