"""
异常
try:
    执行代码
except:
    发生异常时执行的代码
else:
    没有异常时执行的代码
finally:
    不管是否有异常，都会执行的代码
"""


def func1(a, b):
    return  a / b

# print(func1('a', 0))
# 捕获异常
try:
    print(func1(1, 0))
# 捕获具体的异常
except ZeroDivisionError as e:
    print(f"数据异常: {e}")
# 捕获多个异常
except TypeError as e1:
    print(f"类型异常：{e1}")
finally:
    print("finally 内容")


# 抛出异常 开发人员使用较多
# def set_age(num):
#     if num <=0 or num>200:
#         # raise ValueError
#         raise ValueError("值错误")
#     else:
#         print(f"设置的年龄为{num}")
#
# set_age(0)


# 自定义异常
class MyException(Exception):
    def __init__(self, msg):
        print(f'这是一个异常：{msg}')
def set_age(num):
    if num <=0 or num>200:
        # raise ValueError
        raise MyException("值错误")
    else:
        print(f"设置的年龄为{num}")

set_age(0)