import twitter


def oauth(oauth_token, oauth_token_secret, consumer_key, consumer_secret):
    auth = twitter.oauth.OAuth(
        oauth_token,
        oauth_token_secret,
        consumer_key,
        consumer_secret,
    )
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api
