# Imports

import tweepy
import random
import time

# Keys and Access Tokens

CONSUMER_KEY    = '0artwTdQmGRTppPa7lMyOMFl0'
CONSUMER_SECRET = '1aMzfoC5uK553srLuJqV62CFIvZDLaht5c8MRbfh3dQcd01Tdp'

ACCESS_TOKEN    = '1017154912189231105-xtKHyGzWoFun45YlpcJxF0MsFNCfvm'
ACCESS_SECRET   = 'HfwxJurKPGzszkvwsO4Q9fzdICVXeupQA5wkOcBheXw2v'

[]

# Authentication

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api  = tweepy.API(auth)

# Update Status
count = 0
while True:
    count =+ 1
    api.update_status("In hoc signo vinces")
