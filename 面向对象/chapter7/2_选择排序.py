"""
原理：
    每轮都假设该轮最前边的元素为最小值，然后去剩下的元素列表里找真正的最小值，最终交换即可，本轮就找到了本轮的最小值
要点：
    1. 比较的总轮数：列表长度-1
    2. 每轮比较的次数：i+1~n
    3. 谁和谁比较： 索引min_index（初值为i）和索引J比较，索引i 和索引min_index的值交换

时间复杂度：
    最优 o(n2)
    最差 o(n2)

扩展：不稳定排序
扩展：
"""


def select_sort(list):
    # 1.获取长度
    n = len(list)
    # 2.外循环，控制比较的轮数
    for i in range(n - 1):
        # 3.定义变量Min_index，记录住本轮真正的最小值的索引
        min_index = i

        # 4.内循环，看着每轮的比较次数
        for j in range(i + 1, n):
            # 5. 索引min_index和索引j比：
            if list[min_index] > list[j]:
                min_index = j
        # 6. 到这里，说明本轮已经找到了最小值，判断，并交换
        if min_index != i:
            list[min_index], list[i] = list[i], list[min_index]
    return list


if __name__ == "__main__":
    my_list = [5, 3, 6, 7, 2]
    # my_list = [1, 2, 3, 4, 5]
    select_sort(my_list)
    print(my_list)
