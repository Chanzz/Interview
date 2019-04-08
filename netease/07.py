# 现在有一组正整数序列a1,a2,……,aN,请计算出其中满足最大公约数为1的三个数ai,aj,ak的组合的数量，ai,aj,ak范围为1<=i<j<k<=N

# 输入
# 8
# 1 2 3 4 5 6 7 8
# 输出
# 52
import itertools
import sys

#排序
def Sort_xyz(x, y, z):
    l = [x, y, z]
    l.sort()
    return l

#求三个数的最大公倍数
def Gcd3(x, y, z):
    x, y, z = Sort_xyz(x, y, z)
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x

    if y < z:
        temp = y
        y = z
        z = temp

    while y != z:
        if y > z:
            y = y - z
        else:
            z = z - y
    return z


s = sys.stdin.readlines()
list1 = list(map(int, s[1].split()))
#求出所有组合
a = itertools.combinations(list1, 3)
out = 0
for b in a:
    x = b[0]
    y = b[1]
    z = b[2]
    if Gcd3(x, y, z) == 1:
        out += 1
print(out)
