import  pymongo

client  =  pymongo.MongoClient("mongodb://localhost:27017/")
db = client.mydb
col = db.col

myquery = {"alexa":"10000"}
x = col. update_one(myquery,{"$set":{"alexa":"12345123451234512345"}})
x = col. update_many(myquery,{"$set":{"alexa":"12345123451234512345"}})
print(x,"===")
for x in col.find():
  print(x.get("alexa"))