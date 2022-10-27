import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://jay:12345@cluster0.wk0nnn6.mongodb.net/?retryWrites=true&w=majority")
db = cluster['mydb']
collection = db['trial']

post1 = {'_id': 0, 'name': 'peter', 'age': 26}
post2 = {'_id': 0, 'name': 'ellen', 'age': 26}
post3 = {'_id': 0, 'name': 'ashrey', 'age': 26}


#collection.insert({'post2':post2, 'post3': post3})
results = collection.findMany({'age': 26})
for result in results:
    print(result)
