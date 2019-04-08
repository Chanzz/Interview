# 某大型游乐场引进了一个弹射装置，最多可同时将两名游客弹射到位于高处
# 的着陆区。为了确保安全，该项目工作人员为每一个排队的游客标记了
# 权重，体重越大，权重越高；同时设定了每次弹射的权重上限，即，如果2
# 名游客的权重之和超过了权重上限，那么只能安排1名游客弹射，另1名游客等候下次弹射。

# 现在给出排队参与游戏的所有游客的权重和弹射的权重上限，请您帮工作人员计算出最坏情况下所需的弹射次数？

# 输入
# 6 6
# 2 3 3 3 4 5
# 输出
# 5
import sys

s = sys.stdin.readlines()
list1 = list(map(int, s[0].split()))
n = list1[0]
w = list1[1]
list2 = list(map(int, s[1].split()))
end = 0
start=0
bad_list = []
list2.sort()
for i in list2:
    if i > int(w / 2):
        break
    end += 1
b=end
c=1
while end<n:
    bad_list.append(list2[end])
    bad_list.append(list2[end-c])
    end += 1
    c+=2
while start<=end-c:
    bad_list.append(list2[start])
    start += 1
print(bad_list)
a = 0
out = 0
for i in range(n // 2):
    if bad_list[a] + bad_list[a + 1] > w:
        out += 2
    else:
        out += 1
    a += 2
print(out)
