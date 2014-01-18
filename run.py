from app import authorization, retrieving_trends
from ifeel.settings import *
from utils import json_utils


if __name__ == "__main__":
    # Authorization.
    twitter_api = authorization.oauth(
        OAUTH_TOKEN,
        OAUTH_TOKEN_SECRET,
        CONSUMER_KEY,
        CONSUMER_SECRET,
    )

    # Get trends.
    # Valid ids: WORLD_WOE_ID, US_WOE_ID, PE_WOE_ID, LI_WOE_ID
    trends = retrieving_trends.get_trends(twitter_api, WORLD_WOE_ID)
    json_utils.pretty_json(trends)

    # Computing the intersection of two sets of trends
    common_trends = retrieving_trends.intersection_trends(
        twitter_api,
        WORLD_WOE_ID,
        US_WOE_ID,
    )
    print common_trends
