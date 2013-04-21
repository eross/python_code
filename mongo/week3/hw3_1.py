import pymongo
import sys

connection = pymongo.Connection('mongodb://localhost',safe = True)

db = connection.school

students = db.students

cursor = students.find({'scores.type':'homework'})

for s in cursor:
    low = sys.maxint
    lowsc = None
    hwcount = 0
    lowindex = -1
    idx = -1
    for sc in s['scores']:
        idx = idx + 1
        print sc
        if sc['type']=='homework':
            hwcount = hwcount + 1
            if sc['score'] < low:
                low = sc['score']
                lowsc = sc
                lowindex = idx
    if hwcount > 1:
        print 'low',lowsc
        del s['scores'][lowindex]
        db.students.update({'_id': s['_id']},{'$set': {'scores': s['scores']}})
    else:
        print 'SINGLE'

