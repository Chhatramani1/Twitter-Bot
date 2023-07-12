import tweepy
import time

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Create an OAuthHandler instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create a Tweepy API object
api = tweepy.API(auth)

# Define the keyword to search for
keyword = input("Enter the keyword to search for: ")

# Define the tweet content to post
tweet_content = input("Enter the tweet content: ")

# Search and retweet tweets containing the keyword
def retweet_tweets():
    try:
        tweets = api.search(q=keyword, count=10)
        for tweet in tweets:
            if not tweet.retweeted:
                tweet.retweet()
                print("Retweeted: ", tweet.text)
                time.sleep(2)  # Pause for 2 seconds to comply with rate limits
    except tweepy.TweepError as e:
        print("Error occurred while retweeting:", str(e))

# Like tweets containing the keyword
def like_tweets():
    try:
        tweets = api.search(q=keyword, count=10)
        for tweet in tweets:
            if not tweet.favorited:
                tweet.favorite()
                print("Liked: ", tweet.text)
                time.sleep(2)  # Pause for 2 seconds to comply with rate limits
    except tweepy.TweepError as e:
        print("Error occurred while liking tweets:", str(e))

# Reply to mentions with a predefined tweet
def reply_to_mentions():
    try:
        mentions = api.mentions_timeline(count=10)
        for mention in mentions:
            if mention.in_reply_to_status_id is None:
                api.update_status(
                    status=f"@{mention.user.screen_name} {tweet_content}",
                    in_reply_to_status_id=mention.id,
                )
                print("Replied to mention: ", mention.text)
                time.sleep(2)  # Pause for 2 seconds to comply with rate limits
    except tweepy.TweepError as e:
        print("Error occurred while replying to mentions:", str(e))

# Follow users who mentioned the bot
def follow_users():
    try:
        mentions = api.mentions_timeline(count=10)
        for mention in mentions:
            user = mention.user
            if not user.following:
                user.follow()
                print("Followed user: ", user.screen_name)
                time.sleep(2)  # Pause for 2 seconds to comply with rate limits
    except tweepy.TweepError as e:
        print("Error occurred while following users:", str(e))

# Post a tweet
def post_tweet():
    try:
        api.update_status(tweet_content)
        print("Tweeted: ", tweet_content)
    except tweepy.TweepError as e:
        print("Error occurred while posting a tweet:", str(e))

# Perform automated actions
retweet_tweets()
like_tweets()
reply_to_mentions()
follow_users()
post_tweet()
