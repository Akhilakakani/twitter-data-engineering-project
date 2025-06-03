import pandas as pd
!pip install s3fs
!pip install tweepy
import tweepy
import json
import s3fs
from datetime import datetime

bearer_token = " "
client = tweepy.Client(bearer_token=bearer_token)
user_resp = client.get_user(username="elonmusk")
user_id = user.data.id
tweets_resp = client.get_users_tweets(id=user_id, max_results=10, tweet_fields=["created_at", "public_metrics"])

tweet_list = []
for tweet in tweets_resp.data:
    metrics = tweet.public_metrics
    refined_tweet={"user":user_resp.data.username, 'text':tweet.text,
                   'favorite_count':metrics["like_count"],
                   'retweet_count':metrics["retweet_count"],
                   'created_at':tweet.created_at}
    tweet_list.append(refined_tweet)

df = pd.DataFrame(tweet_list)
df.to_csv("elonmusk_twitter_data.csv")
