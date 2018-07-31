import json

file = open('tweets.json', 'r')
data = json.load(file)

for d in data:
    # for info_categories, info in d.items():
    #     print(info_categories, info)
    # for user_mentions in d['user_mentions']:
    #     print(user_mentions['screen_name'])
    print(d['retweet_count'])
    print (d['user']['favourites_count'])
    print(d['text'])
    break
