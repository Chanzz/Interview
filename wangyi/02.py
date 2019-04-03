# 有 n 个学生站成一排，每个学生有一个能力值，牛牛想从这 n 个学生中按照顺序选取 k 名学生，要求相邻两个学生的位置编号的差不超过 d
# 使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？
# 3
# 7 4 7
# 2 50


# 36
# 7 -15 31 49 -44 35 44 -47 -23 15 -11 10 -21 10 -13 0 -20 -36 22 -13 -39 -39 -31 -13 -27 -43 -6 40 5 -47 35 -8 24 -31 -24 -1
# 3 31
import sys

s = sys.stdin.readlines()
list_stu = list(map(int, s[1].split()))
lens = int(s[0])
target = list(map(int, s[2].split()))
k = target[0]
d = target[1]
max = 0
max_place = 0
for i in range(lens):
    if list_stu[i] > max:
        max = list_stu[i]
        max_place = i
out = max
for i in range(k - 1):
    new_list = []
    if max_place - d < 0:
        min_list = 0
    else:
        min_list = max_place - d
    if max_place + d > lens:
        max_list = lens
    else:
        max_list = max_place + d
    for n in range(min_list, max_list):
        new_list.append(list_stu[n])
        new_list.sort()
    max = new_list.pop(-2)
    out *= max
    max_place = list_stu.index(max)
print(out)
