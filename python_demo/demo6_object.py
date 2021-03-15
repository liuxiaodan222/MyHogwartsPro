"""
1. 什么是面向对象
2. 类、方法、类变量的定义
3. 实例引用、实例变量使用

self ：代表实例

实例变量和类变量：
实例变量
类变量

实例方法和类方法：
类方法 @classmethod
类名.类方法名
类不能访问实例方法

实例方法
实例对象.实例方法
"""

class Person:
    # 类属性
    name = "default"
    age = 0
    gender = "male"
    weight = 100

    def __init__(self, name, age, gender):
        # 实例属性
        self.name = name
        self.age = age
        self.gender = gender

    # 实例方法
    def eat(self):
        print(f"{self.name} is eating")
        print(self.weight)

    # 类方法
    @classmethod
    def sleep(cls):
        print(f"{cls.name} is sleepping")

# 类属性： 可以通过类名直接访问
# print(Person.gender)
# 类方法： 可以通过类名直接访问
# Person.sleep()
# 实例方法： 不可以通过类名直接访问，需要进行实例化
# Person.eat()

# 对象实例化
xm = Person("小明", 18, "male")
xm.eat()
xm.sleep()
print(xm.weight)