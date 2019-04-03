# 递归法的快速排序
def QuickSort(list):
    if len(list) >= 2:
        mid = list[len(list) // 2]
        right = []
        left = []
        list.remove(mid)
        for num in list:
            if num >= mid:
                right.append(num)
            if num < mid:
                left.append(num)
        return QuickSort(left) + [mid] + QuickSort(right)
    else:
        return list


if __name__ == '__main__':
    wlist = [3, 8, 9, 5, 7, 6, 4, 9, 5, 7, 3, 2, 1, 4]
    alist = QuickSort(wlist)
    print(alist)
