import pymongo
import bottle

@bottle.route('/')
def index():
    connection = pymongo.MongoClient('localhost',27017)

    db = connection.test

    thing = db.things

    item = thing.find_one()

    return '<b>Hello %s!</b>' % item['a']

bottle.run(host='localhost',port=8082)