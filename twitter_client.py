import tweepy
import os

def twitter_api():
    client = tweepy.Client(
        consumer_key=os.environ["f4DQ3vkDEN3qERLjDkDE0sykw"],
        consumer_secret=os.environ["vrzmhoStf1ZOvcGQITmr8wGokyIRh1Q4jHOgYS0TRlL3bkenD6"],
        access_token=os.environ["1994850095221936128-rHYhPaiTTZBrz1CeIpwONpPZsQJkmW"],
        access_token_secret=os.environ["Uz8JFdl8avDVb2EpwGnO77QMyufhbRqak8Rp8r8LBkCkr"]
    )
    return client

def post_tweet(text):
    client = twitter_api()
    client.create_tweet(text=text)
