"""
原理：
    把列表分成两部分，假设第一个元素是有序的，剩下的是无序的，每次从无需列表中获取一个，和它前边的所有元素比较，决定它的位置并插入
流程：
    第一轮： 1次    索引1和0比较
    第二轮： 2次    索引2和1 索引2和0比较

要点：
    1. 比较的总轮数：列表长度-1  range(n)
    2. 每轮比较的次数：range(i,0,-1)
    3. 谁和谁比较：索引j 和 j-1 位置的元素比

时间复杂度：
    最优 o(n)
    最差 o(n2)

扩展：稳定排序
扩展：
"""


def insert_sort(list):
    # 1.获取长度
    n = len(list)
    # 2.外循环，控制比较的轮数
    for i in range(1, n):
        # 3.内循环，看着每轮的比较次数
        for j in range(i, 0, -1):
            if my_list[j] < my_list[j - 1]:
                my_list[j - 1], my_list[j] = my_list[j], my_list[j - 1]
            else:
                # 5.走到这里，说明元素位置找到了，停止
                break
    return list


if __name__ == "__main__":
    my_list = [5, 3, 6, 7, 2]
    # my_list = [1, 2, 3, 4, 5]
    insert_sort(my_list)
    print(my_list)
