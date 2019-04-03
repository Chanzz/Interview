# 二分查找
def BinarySearch(list, val):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == val:
            return mid
        elif list[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return


if __name__ == '__main__':
    wlist = [1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 9, 9]
    print(BinarySearch(wlist, 5))
