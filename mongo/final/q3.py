from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)
db = client.enron
r = db.messages.find_one({"headers.Message-ID": "<8147308.1075851042335.JavaMail.evans@thyme>"} )



pprint.pprint(r)
to = r['headers']['To']
if "mrpotatohead@10gen.com" not in to:
    to.append(u"mrpotatohead@10gen.com")
pprint.pprint(r)
#db.messages.save(r)