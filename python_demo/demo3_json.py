"""
json格式转化
json 由字典和列表组成的
"""
import json

# 定义一个字典
data = {
    "name": ["jerry", "nickname"],
    "age": 16,
    "gender": "male"
}

# 字典转化为json
data1 = json.dumps(data)
print(data1)
print(type(data1))

# json转化为字典
data2 = json.loads(data1)
print(data2)
print(type(data2))

# todo
# json.dump()
# json.load()
