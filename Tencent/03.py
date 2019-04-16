# 小Q打算穿越怪兽谷。他不会打怪，但是他有钱。他知道，只要给怪兽一定的金币，怪兽就会一直护送着他出谷。
# 在谷中，他会依次遇到N只怪兽，每只怪兽都有自己的武力值和要‘贿赂’它所需的金币数。如果小Q没有‘贿赂’某只怪兽，而这只怪兽的武力值又大于护送他的怪兽武力值之和，这只怪兽就会攻击他。
# 小Q想知道，要想成功穿越怪兽谷而不被攻击，他最少要准备多少金币。
#
# 3
# 6 5 8
# 1 1 2

import sys

s = sys.stdin.readlines()
N = int(s[0])
monster_list = list(map(int, s[1].split()))
max_monster = max(monster_list)
monster_money = list(map(int, s[2].split()))
if N == 0:
    print(0)
if N == 1:
    print(monster_money[0])
B = []
for i in range(50):
    B.append(0)
B = [B] * (N + 1)
for k in range(N):
    for C in range(50):
        value1 = B[k - 1][C - monster_list[k]] + monster_money[k]
        value2 = B[k - 1][C]
        if value1 > value2:
            B[k][C] = value1
        else:
            B[k][C] = value2

print(B)
