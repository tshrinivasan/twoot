#!/usr/bin/python3

import sys
import tweepy
import os
from mastodon import Mastodon

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key,secret)

# Create API object
tweet_api = tweepy.API(auth)

# Create a tweet
#tweet_api.update_status("Hello from Twoot")



mastodon = Mastodon(
    access_token = 'access_token'
    api_base_url = 'URL of the mastodon instance'
)
#mastodon.toot('Tooting from python using #mastodonpy !')

clear = "clear"
os.system(clear)
print("\n")
#text = input()

lines = []
while True:
    try:
        text =input()
        if text:
            lines.append(text)
        else:
            break
    except EOFError:
        break


user_input = '\n'.join(lines)    

print(len(user_input))

if len(user_input)>280:
    print("text length > 280. Exiting")
    sys.exit()

else:
    tweet_api.update_status(user_input)
    mastodon.toot(user_input)
    print(user_input)
    print("Sent Toot and Tweet !")
    

# links

# https://docs.tweepy.org/en/stable/

# https://mastodonpy.readthedocs.io/en/stable/

# https://shkspr.mobi/blog/2018/08/easy-guide-to-building-mastodon-bots/
# https://notes.ayushsharma.in/2018/09/tweet-toot-building-a-bot-for-mastodon-using-python

# https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api
    
