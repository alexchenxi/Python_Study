"""
概述：  属于查找类算法，相对效率较高，时间复杂度为O(n)
前提：列表是有序的

"""


def binary_search_recursive(list, target):
    n = len(list)
    if n == 0:
        return False
    mid = n // 2
    if target < list[mid]:
        return binary_search_recursive(list[:mid], target)
    elif target > list[mid]:
        return binary_search_recursive(list[mid + 1 :], target)
    else:
        return True


def binary_search(list, target):
    n = len(list)
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if target < list[mid]:
            end = mid - 1
        elif target > list[mid]:
            start = mid + 1
        else:
            return True
    return False


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(list, 33))
