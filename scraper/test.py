import pymongo

client = pymongo.MongoClient("mongodb://ian:secretPassword@35.192.66.152/cool_db") # defaults to port 27017

db = client.cool_db

# print the number of documents in a collection
print(db)