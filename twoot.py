#!/usr/bin/python3

import sys
import tweepy
import os
from mastodon import Mastodon

twitter_max_char = 280
mastodon_max_char = 5000

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key,secret)

# Create API object
tweet_api = tweepy.API(auth)

# Create a tweet
#tweet_api.update_status("Hello from Twoot")



mastodon = Mastodon(
    access_token = 'access_token',
    api_base_url = 'URL of the mastodon instance'
)
#mastodon.toot('Tooting from python using #mastodonpy !')

clear = "clear"
os.system(clear)
print("\n")
#text = input()
print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to post it.")
lines = []
while True:
    try:
        text = input()
    except EOFError:
        break
    if text.strip():
        lines.append(text)


user_input = '\n'.join(lines)

def splitWordsBySize(word, maxLength):
    if len(word) < maxLength:
        words.append(word)
        return words;
    # Take first max length word
    tempWord = word[0:maxLength]
    # Split the word with space to get last word
    lis = tempWord.split(" ")
    lastWordIndex = len(lis) - 1
    nextWord = lis[0:lastWordIndex][0];
    words.append(nextWord)
    remaingingWord = word[len(nextWord):].strip()
    return splitWordsBySize(remaingingWord, maxLength) 

# For twitter
words = [];
tweet_messages = splitWordsBySize(user_input, twitter_max_char);
tweet_response = ''
for x in range(0, len(tweet_messages)):
    tweet_response = tweet_api.update_status(tweet_messages[x], in_reply_to_status_id = tweet_response)

print("Sent Tweet !")

# For mastodon
words = [];
mastodon_messages = splitWordsBySize(user_input, mastodon_max_char);
mastodon_response = None
for x in range(0, len(mastodon_messages)):
    if mastodon_response is not None:
        mastodon_response = mastodon.status_post(mastodon_messages[x], in_reply_to_id = mastodon_response)
    else:
        mastodon_response = mastodon.toot(mastodon_messages[x])
print("Sent Toot !")



    

# links

# https://docs.tweepy.org/en/stable/

# https://mastodonpy.readthedocs.io/en/stable/

# https://shkspr.mobi/blog/2018/08/easy-guide-to-building-mastodon-bots/
# https://notes.ayushsharma.in/2018/09/tweet-toot-building-a-bot-for-mastodon-using-python

# https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api
    
