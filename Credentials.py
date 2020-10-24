import tweepy
from time import sleep

consumer_key = "plZ5ofgEmmM9yvFSyN4qCe5H5"
consumer_secret = "51b7LGcmQjQJUpsxk2SgWIilTrWdBbpvLcx9jMxvWs5J8pTFpd"

key = "835000394-92ozNG6cIzewNwpN03W84f2JqdacsApFwUmHGfqc"
secret = "idNW5a1PPRITeXMFkEDg9TnUpahehfs5jQuDbj1XVq7Jk"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
