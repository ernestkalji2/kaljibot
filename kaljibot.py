import tweepy
from time import sleep

consumer_key = "plZ5ofgEmmM9yvFSyN4qCe5H5"
consumer_secret = "51b7LGcmQjQJUpsxk2SgWIilTrWdBbpvLcx9jMxvWs5J8pTFpd"

key = "835000394-92ozNG6cIzewNwpN03W84f2JqdacsApFwUmHGfqc"
secret = "idNW5a1PPRITeXMFkEDg9TnUpahehfs5jQuDbj1XVq7Jk"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


# Twitter bot setting for liking Tweets 
LIKE = True

# Twitter bot setting for following user who tweeted 
FOLLOW = False

print("Twitter bot which retweets, like tweets and follow users") 
print("Bot Settings") 
print("Like Tweets :", LIKE) 
print("Follow users :", FOLLOW) 

# Change the hashtags by your choice

for tweet in tweepy.Cursor(api.search, q = ('#zedtwitter OR #zambia OR #lusaka OR #follow4follow OR #happy56th OR #indepenceday OR #happyindepenceday OR #ndola OR #kitwe OR #edgarlungu OR #kopala OR #bowmanlusambo OR #mwebantu -filter:retweets'),lang='en').items(): 
	try: 
		print('\nTweet by: @' + tweet.user.screen_name) 


		# Favorite the tweet 
		if LIKE: 
			tweet.favorite() 
			print('Favorited the tweet') 

		# Follow the user who tweeted 
		# check that bot is not already following the user 
		if FOLLOW: 
			if not tweet.user.following: 
				tweet.user.follow() 
				print('Followed the user') 
		
		# Twitter bot sleep time settings in seconds. Use large delays so that you account will not banned
		sleep(300) # 300 seconds = 5 minute

	except tweepy.TweepError as e: 
		print(e.reason) 

	except StopIteration: 
		break
