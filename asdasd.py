import pymongo
import requests, json
url = 'http://search.twitter.com/search.json?q=python%20pandas'
data = json.loads(requests.get(url).text)
con =pymongo.Connection('loclhost',port=27017)

tweets = con.db.tweets
for tweet in data['results']:
    tweets.save(tweet)
cursor =tweets.find({'from_user':'wesmckinn'})

tweet_fields = ['creted_at', 'from_user', 'id', 'text']
result = DataFrame(list(cursor), columns=tweet_fields)
