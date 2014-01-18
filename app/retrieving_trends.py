# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.


def get_trends(twitter_api, id):
    trends = twitter_api.trends.place(_id=id)
    return trends


def intersection_trends(twitter_api, id1, id2):
    world_trends = twitter_api.trends.place(_id=id1)
    world_trends_set = set([trend['name']
                           for trend in world_trends[0]['trends']])

    us_trends = twitter_api.trends.place(_id=id2)
    us_trends_set = set([trend['name'] for trend in us_trends[0]['trends']])

    common_trends = world_trends_set.intersection(us_trends_set)
    return common_trends
