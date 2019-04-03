# 现有一个砸金蛋兑积分的玩法，玩法说明如下：
# 1.有n个金蛋，每个标有一个数值，存在数组values中；
# 2.每砸开金蛋i时可以获得积分为values[left]*values[i]*values[right]
# 其中left和right代表和i相邻的两个金蛋；
# 3.当金蛋i被砸开后，其左右金蛋left和right即变成相邻
#
# 求用户砸开所有金蛋兑得的最大值积分。
#
# 说明：
# 可以假设values[-1]=values[n]=1，但注意它们不是真实存在的，所以并不能被砸开。
# o<=n<=200,0<=values[i]<-100

# 输入
# 3 1 5 8

# 输出
# 167


s = input()
a = map(int, list(s.replace(' ', '')))
list_egg = list(a)
out = 0


def find_min(list1):
    min = 100
    if len(list1) > 3:
        for i in range(1, len(list1) - 2):
            if min > list1[i]:
                min = list1[i]
    else:
        min = list1[1]
    return list1.index(min)


for n in range(len(list_egg) - 2):
    egg_index = find_min(list_egg)
    out += list_egg[egg_index - 1] * list_egg[egg_index] * list_egg[egg_index + 1]
    del list_egg[egg_index]
if list_egg[0] > list_egg[1]:
    out += list_egg[0] * list_egg[1]
    del list_egg[1]
else:
    out += list_egg[0] * list_egg[1]
    del list_egg[0]
out += list_egg[0]
print(out)
