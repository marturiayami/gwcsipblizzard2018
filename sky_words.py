'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
tweets = []


# Continue your program below!
for tweet in tweetData:
    tweets.append(tweet['text'])
giant_string =' '.join(tweets)

tb = TextBlob(giant_string)
list_of_words = giant_string.split()

word_count = {}
neutral = {}
positive = {}
negative = {}

for word in list_of_words:
    word = word.lower().rstrip().lstrip()
    if 'http'in word:
        continue
    if word[0] in {',', '?', '.', ':', '#', '@', "'", '"'}:
        word = word[1:]
    if len(word) < 4:
        continue
    if word[-1] in {',', '.', '/', '?', '!', ':', ';', "''", '""'}:
        word = word [:-1]
    list_of_words[words] = list_of_words.get(word, 0) + 1
    word_polarity = TextBlob(word).polarity
    if word_polarity < -0.25:
        negative.append(word)
    if word_polarity < 0.25:
        neutral.append(word)
    else:
        positive.append(word)



for words in list_of_words:
    word_count[words] = word_count.get(words, 0) + 1
print(len(word_count))

word_count2 = {}
for word, count in word_count.items():
    if count < 2:
        continue
    else:
        word_count2[word] = count

print(word_count2)

wordcloud = WordCloud().generate_from_frequencies(word_count2)
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()


# Textblob sample:
# tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.polarity)
