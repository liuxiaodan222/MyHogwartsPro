"""
文件读写
1. 打开文件
2. 操作文件
3. 关闭文件
"""

# f = open("file1.txt")
# print(f.readable())
# # print(f.readlines())
# print(f.readline())
# print(f.readline())
# f.close()

#读取图片时，使用“rb”读取二进制文件
with open("file1.txt", "r") as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break
    # print(f.readlines())