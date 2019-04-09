from pymongo import MongoClient
conn = MongoClient("127.0.0.1",27017)
db = conn.mydb # 连接mydb数据库，如果没有就自动创建
# 创建 table
col = db.col

## 插入数据
#col.insert_one({"name":"zhangsan","age":18})
#col.save({"name":"chunlin","age":26}) ## api过期 不推荐使用
mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
x = col.insert_one(mydict)
print(x) #<pymongo.results.InsertOneResult object at 0x00000201B179B7C8>
print(x.inserted_id) #5cac09d58af1be31389368e4 inserted_id 属性， 它是插入文档的 id 值。

## 出入多个文档
mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]
x = col.insert_many(mylist )
print(x.inserted_ids)
#[ObjectId('5cac0a628af1be3a9000834b'), ObjectId('5cac0a628af1be3a9000834c'), ObjectId('5cac0a628af1be3a9000834d'), ObjectId('5cac0a628af1be3a9000834e'), ObjectId('5cac0a628af1be3a9000834f')]


#### 查询数据
# myquery = {"name":{"$gt":"z"}}
myquery = {"name":{"$regex":"^R"}}

## 查询一条数据
doc = col.find_one()
print(doc)

doc = col.find(myquery).limit(2).skip(0)
for x  in doc:
    print(x)
    


