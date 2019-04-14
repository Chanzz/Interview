# 1
# 8
# 2 1 1 2 2
# 2 1 1 1 4
# 2 1 1 2 2
# 2 2 2 1 4
# 0
# 0
# 1 1 1
# 1 1 1

# 取出帧数
import sys

s = sys.stdin.readlines()
for i in range(len(s)):
    s[i] = list(map(int, s[i].split()))
M = s[1][0]
zhen = []

# 遍历每帧的特征数
num = []
for i in range(M):
    num.append(s[i + 2][0])

# 遍历每帧的特征储存在数组
tezhen = []
for i in range(len(num)):
    for k in range(num[i]):
        tezhen.append([s[i + 2][k * 2 + 1], s[i + 2][k * 2 + 2]])
print(tezhen)
max = []
for i in range(len(tezhen)):
    a = 0
    for k in tezhen:
        if tezhen[i] == k:
            a += 1
    print(a)
print(max)
# now=tezhen[0]
# now_no=0
# flag=0
# for i in num:
#     if i!=0:
#         now_no+=i
#         print(now_no)
#         if now==tezhen[now_no]:
#             flag+=1
#     # else:
#     #     now=tezhen[now_no]
