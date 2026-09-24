"""
解释：
  第一轮. 假定第一个元素为分界值，次数：比该值小的都放左边，比该值大于或等于的放右边
  第二轮，2个分界值，上一轮左边数据找个分界值，右边的数据再找个分界值
  第三轮，4个分界值。。。依此类推
"""


def quick_sort(list, start, end):
    """
    :param list
    :param start 起始索引
    :param end 结束索引
    :return：
    """

    if len(list) == 0 or start >= end:
        return
    left = start
    right = end
    mid = list[start]

    while left < right:
        # 把分界值右边比分界值小的数据放左边
        while list[right] >= mid and left < right:
            right -= 1
        # 说明List[right]比mid小
        list[left] = list[right]

        while list[left] < mid and left < right:
            left += 1
        list[right] = list[left]

    # 说明分界值的位置已经找到，赋值
    my_list[left] = mid

    # 递归，处理左侧边
    quick_sort(my_list, start, left - 1)

    quick_sort(my_list, right + 1, end)


if __name__ == "__main__":
    my_list = [33, 14, 1, 56, 123, 123123]
    quick_sort(my_list, 0, len(my_list) - 1)
    print(my_list)
