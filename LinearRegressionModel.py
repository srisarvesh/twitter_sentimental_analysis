import tweepy

def get_twitter_api():
    ACCESS_TOKEN = "1333083696757260289-7XGWPCYW53YvDENFTQ5GzCG2mvNODE"
    ACCESS_TOKEN_SECRET = "zIzYpUx7aLEJHcZmG4DWIs37WsS2VY6DsH2f9OIOMt0G5"
    API_KEY = "AGlR4lTVXoFnn2MHImSLTTb9R"
    API_SECRET_KEY = "MsNVEf9WSPUTTLmyBa04TTLRrBsFjnkavRgK2kGDmrm0LaR5yt"

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

def collect_twitter_data(api,twitter_user):
    favorite_data=[]
    retweet_data=[]
    for status in tweepy.Cursor(api.user_timeline,id=twitter_user).items():
        favorite_data.append(status.favorite_count)
        retweet_data.append(status.retweet_count)

    return favorite_data,retweet_data


def main():
    api=get_twitter_api()
    favorite_data,retweet_data=collect_twitter_data(api,"@actorvijay")
    print(favorite_data)
    print(retweet_data)

if __name__=="__main__":
    main()