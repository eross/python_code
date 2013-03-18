import couchdb

svr = couchdb.Server('https://saldb.vcd.hp.com')
db = svr['sandbox']

rec = db.get('ep2')

config = {'printername': "eric1",'jid':'ABCDEFGHI'}
rec['config']=config
# or just merge the fields...
# for i in config:
#     rec[i] = config[i]
#
# print out the _id and the new _rev
print db.save(rec)

