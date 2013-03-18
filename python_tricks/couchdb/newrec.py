import couchdb

svr = couchdb.Server('https://saldb.vcd.hp.com')
db = svr['sandbox']
# every rec should be given a unique id.  You can also use the uuid lib in python.
rec={'_id':svr.uuids(1)[0], 'printername': "eric1", 'jid':'ABCDEFGHI'}
# returns the _id and the db generated rev id.
print db.save(rec)

