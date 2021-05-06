# import pymongo
# from pymongo import MongoClient
# client = MongoClient()
# print(client)
# client = MongoClient(host="localhost", port=27017)
# db = client.rptutorials
# print(db)

import pymongo
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://admin:admin123@cluster1.ycoy8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test
db = client["myFirstDatabase"]
# print(db)
collection = db["chatbots"]
# print(collection)

# post_count = collection.count_documents({})
# print(post_count)


# x = collection.find({},{"_id": "6050a11132a76a543d4be5a5","agentName":"abcd"})
# x = collection.find({})
# print(x)

#Retrieving the first record using the find_one() method
# print("First record of the collection: ")
# print(collection.find({"agentName": "xyz"})[0])

# for x in collection.find({},{"agentName":"acbd"}):
#     print(x)
