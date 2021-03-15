"""
字面量
1. 格式化 %
2. format()
3. f'{变量名}'
"""

# 格式化 %  数据格式需要匹配
name = "Herry"
age = 23
num = 1.234
# print("My name is %s, my age is %d, num is %.2f" % (name, age, num))

# format() 不需要指定数据类型
# print("My name is {}, my age is {}, num is {}".format(name, age, num))
# print("My name is {1}, my age is {0}, num is {2}, {0}{1}{2}".format(age, name, num))
#
list1 = [1, 3, 5]
dict1 = {"name": "tom", "gender": "male"}
# print("the list is {}, the dict is {}".format(list1, dict1))
#
#
namelist = ["tom", "jerry", "cat"]
# # 列表解包
# print("our name : {}、{} and {}".format(*namelist))
#
# # 字典解包
# print("my name is {name}, gender is {gender}".format(**dict1))



# F-strings python3.6以上版本可用    使用方法：f'变量名'
print(f"my name is {name}, age is {age} ")
print(f"my list is {list1}, dict is {dict1}")
print(f"my name is {dict1['name']}, gender is {dict1['gender']}")


