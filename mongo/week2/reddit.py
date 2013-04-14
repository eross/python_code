import pymongo
import urllib2
import json

connection = pymongo.Connection("mongodb://localhost",safe=True)
db = connection.reddit
stories = db.stories

reddit_page = urllib2.urlopen("http://www.reddit.com/r/technology/.json")

parsed = json.loads(reddit_page.read())

stories.drop()

for i in parsed:
    print i

doc = parsed['data']['children']

for i in doc:
    stories.insert(i['data'])