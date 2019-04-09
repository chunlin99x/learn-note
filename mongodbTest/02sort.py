from pymongo import MongoClient
conn = MongoClient("127.0.0.1",27017)
db = conn.mydb # 连接mydb数据库，如果没有就自动创建
# 创建 table
col = db.col
doc = col.find().sort("alexa")
doc = col.find().sort("alexa",-1)
## 按照降序排列
for i in doc:
    print(i)