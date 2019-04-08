# 3 3
# 1 100
# 10 1000
# 1000000000 1001
# 9 10 1000000000
# 每个测试用例的第一行包含两个正整数，分别表示工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)。
# 接下来的N行每行包含两个正整数，分别表示该项工作的难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
# 接下来的一行包含M个正整数，分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。

import sys


s = sys.stdin.readlines()

list_n = map(int, s[0].split())
num = []
pay = []
# 遍历工作数量，取出难度和报酬
for i in range(list(list_n)[0]):
    work = map(int, s[i + 1].split())
    list_work = list(work)
    num.append(list_work[0])
    pay.append(list_work[1])
job = dict(zip(num, pay))
# 取出小伙伴能力
fri = list(map(int, s[-1].split()))
out = []
# 初始化输出数组
for i in range(len(fri)):
    out.append(1)
# 遍历小伙伴的能力，取出与遍历工作难度比较
for i in range(len(fri)):
    for key in job:
        if key <= fri[i]:
            out[i] = job[key]
for i in range(len(out)):
    print(out[i])

# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

