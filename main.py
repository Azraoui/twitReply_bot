from dotenv import load_dotenv
import tweepy
import os

load_dotenv()
api_key = os.environ["API_KEY"]
api_secret = os.environ["API_SECRET"]
bearer_token = os.environ["BEARER_TOKEN"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# client.create_tweet(text = "Let's Go!")

client.create_tweet(in_reply_to_tweet_id="1654151396785115137", text="Alhamdo lilah")
