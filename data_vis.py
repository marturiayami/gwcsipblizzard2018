# '''
# In this project, you will visualize the feelings and language used in a set of
# Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
# need!
# '''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# for tweet in tweetData:
#     print(tweet['text'])
#     break
# Continue your program below!

polarity_values = []
# Textblob sample:
for tweet in tweetData:
    tweet_text = tweet['text']
    tb = TextBlob(tweet_text)
    print('{}: {}'.format(tweet_text, tb.polarity))
    polarity_values.append(tb.polarity)

bins = [-1, -0.5, 0, 0.5, 1]

plt.hist(polarity_values, bins)
plt.title("Tweet Polarity")
plt.ylabel("Count of Tweets")
plt.xlabel("Polarity")
plt.show()
