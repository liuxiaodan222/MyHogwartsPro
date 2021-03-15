"""
模块导入
"""

# 系统模块
import os
import time
import sys

# 第三方开源模块 需要使用 pip install 模块名 安装
import appium
import requests

# 查看当前模块下可以调用的方法与变量

print(dir())
print(dir(sys))
print(sys.path)

# 自定义模块
from python_demo.demo_func1 import func1, func2

func1()
func2()