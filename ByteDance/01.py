# 1 2 1
# 1 1 0
# 0 1 1
import sys

# 获取输入
s = sys.stdin.readlines()
for i in range(len(s)):
    s[i] = list(map(int, s[i].split()))

# 获取输入的数组大小
height = 0
lenght = len(s[1])
for i in s:
    height += 1


# 查找值为2的index
def find2(s):
    index = []
    for i in range(len(s)):
        for k in range(len(s[i])):
            if s[i][k] == 2:
                index.append([i,k])
    return index


# 遍历周围的数，改为2
def change(index):
    flag = 0
    for key in index:
        if key[0] - 1 >= 0:
            if s[key[0] - 1][key[1]] == 1:
                s[key[0] - 1][key[1]] = 2
                flag = 1
        if key[1] - 1 >= 0:
            if s[key[0]][key[1] - 1] == 1:
                s[key[0]][key[1] - 1] = 2
                flag = 1
        if key[0] + 1 <= height-1:
            if s[key[0] + 1][key[1]] == 1:
                s[key[0] + 1][key[1]] = 2
                flag = 1
        if key[1] + 1 <= lenght-1:
            if s[key[0]][key[1] + 1] == 1:
                s[key[0]][key[1] + 1] = 2
                flag = 1
    return flag


#首先找2
index = find2(s)
a = 0  # 计数器
while index:
    flag = change(index)
    if flag == 1:
        a += 1
    else:
        break
    index = find2(s)

print(a)



