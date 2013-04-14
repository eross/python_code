import couchdb
from pprint import pprint as pp

def updatep1(db,rec,field, value):
    r = db.get(rec)
    if r == None:
        r = {'_id':rec,field:value }
    else:
        r['field']=value
    pp(db.save(r))

CONFLICT=True


s = couchdb.Server()
d1 = s['s1']
d2 = s['s2']

updatep1(d1,'epr1','name','eric')
if CONFLICT:
    updatep1(d2,'epr1','last','ross')
result = s.replicate(s.resource.url+'/s1',s.resource.url+'/s2')
#pp(result)