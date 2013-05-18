__author__ = 'ericr'

import pymongo

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
db = connection.q7

rows = db.images.find().sort("_id", pymongo.DESCENDING)
for i in rows:
    foundin=db.albums.find({"images": i['_id']})
    if foundin.count() == 0:
        db.images.remove({'_id': i['_id']})
    #for j in foundin:
    #    print i['_id']
    #    print j


