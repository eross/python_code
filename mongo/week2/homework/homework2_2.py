import pymongo


connection = pymongo.Connection('mongodb://localhost',safe = True)

db = connection.students

grades = db.grades

cursor = grades.find({'type': 'homework'},{'student_id': 1, 'score': 1}).sort([('student_id', pymongo.ASCENDING),('score', pymongo.ASCENDING)])

last_student = None

for s in cursor:
    if s['student_id'] != last_student:
        print s
        last_student = s['student_id']
        grades.remove(s)