import tweepy
 
# API keyws that yous saved earlier
api_key = "Abbwejkbsjgb"
api_secrets = "237hbsdfibnr3277bfwhefoghaohf"
access_token = " nefjhn2q3y7723r5i8"
access_secret = "wefnpiu237bngwniuwe"
 
# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)
 
api = tweepy.API(auth)
 
try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')
