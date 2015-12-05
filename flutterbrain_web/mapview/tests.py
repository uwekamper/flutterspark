from django.test import TestCase

from .clustering import get_tweets

# Create your tests here.
class MapViewTests(TestCase):
    """
    TODO: Document the shit out of this class.
    """
    def test_get_tweets(self):
        """
        This is the test_get_tweets method. It tests get_tweets()!
        """
        tweets = get_tweets('flutterbrn')
        print tweets
