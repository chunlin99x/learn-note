from pymongo import MongoClient
conn = MongoClient("127.0.0.1",27017)
db = conn.mydb # 连接mydb数据库，如果没有就自动创建
# 创建 table
col = db.col
myquery = {"name":"Taobao"}
col.delete_one(myquery) ## 删除一个文档
x = col.delete_many(myquery) ## 删除满足条件的多个文档
print(x.delete_count,"文档删除个数")

###  删除集合中所有的文档
col.delete_many({})

### 删除集合
col.drop()



