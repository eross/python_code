from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.test
things = db.things
for i in things.find():
    print i
