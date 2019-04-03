# 冒泡排序
def BubbleSort(list):
    llen = len(list)
    while llen:
        for n in range(llen - 1):
            if list[n] > list[n + 1]:
                list[n], list[n + 1] = list[n + 1], list[n]
                '''
                a = list[n + 1]
                list[n + 1] = list[n]
                list[n] = a
                '''
        llen -= 1
    return list


if __name__ == '__main__':
    wlist = [3, 8, 9, 5, 7, 6, 4, 9, 5, 7, 3, 2, 1, 4]
    print(BubbleSort(wlist))
