import os
import tweepy

client = tweepy.Client(os.environ['BEARER_TOKEN'], os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'], os.environ['TOKEN'], os.environ['TOKEN_SECRET'])

def send_post(text, in_reply_to_tweet_id=None):
  return client.create_tweet(text=text, in_reply_to_tweet_id=in_reply_to_tweet_id)