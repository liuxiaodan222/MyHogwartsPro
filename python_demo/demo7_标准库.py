"""
os , time, urllib, math
"""
import os

# 创建目录
# os.mkdir('testdir')
# 查看目录下的文件和目录
# print(os.listdir("./"))

# 删除目录
# os.removedirs('testdir')

# print(os.getcwd())

# 判断文件是否存在
# print(os.path.exists("b"))
# if not os.path.exists("b"):
#     os.mkdir("b")
# if not os.path.exists("b/test.txt"):
#     f = open("b/test.txt", "w")
#     f.write("hello, os using")
#     f.close()


import time

# print(f"asctime: {time.asctime()}")
# print(f"time: {time.time()}")
print(f"localtime: {time.localtime()}")
print("当前时间为：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取两天前的时间
now_timestamp = time.time()
tow_day_before = now_timestamp - 60*60*24*2
time_tuple = time.localtime(tow_day_before)
print(time_tuple)
# UnicodeEncodeError: 'locale' codec can't encode character '\u5e74' in position 2: Illegal byte sequence
# print(time.strftime("%Y年%m月%d日 %H:%M:%S", time_tuple))
print("两天前的时间为：", time.strftime("%Y{y}%m{m}%d{d} %H:%M:%S", time_tuple).format(y='年', m='月',d= '日'))

# 三天后
three_days_after = now_timestamp + 60*60*24*3
time_tuple1 = time.localtime(three_days_after)
print("三天后的时间为：", time.strftime("%Y{}%m{}%d{} %H:%M:%S", time_tuple1).format('年', '月','日'))