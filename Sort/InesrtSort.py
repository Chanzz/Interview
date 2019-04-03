# 插入排序
def InsertSort(list):
    asorted = [list[0]]
    list.remove(list[0])
    llen = len(list)
    for n in range(1, llen):
        i = n
        print(n)
        if list[0] <= asorted[i-1]:
            print('here')
            while i > 0 and list[0] > asorted[i-1]:
                asorted.insert(i, list[0])
                list.remove(list[0])
                i -= 1
        else:
            asorted.append(list[0])
            list.remove(list[0])


if __name__ == '__main__':
    wlist = [3, 8, 9, 5, 7, 6, 4, 9, 5, 7, 3, 2, 1, 4]
    print(InsertSort(wlist))
