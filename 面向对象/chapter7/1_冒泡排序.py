"""

要点：
    1. 比较的总轮数 n-1
    2. 每轮比较的总次数 n-1-i
    3. 谁和谁比较 索引j 和 j+1位置的元素排序
时间复杂度：
    最优：O(n)
    最坏：O(n2)
扩展：
    稳定排序算法
    外循环的-1是什么意思：减少比较的轮数，提高效率
    内循环的-1是什么意思：为了防止索引 越界
    内循环的-i是什么意思：减少每轮比较的次数
"""


def bubble_sort(my_list):

    # 获取列表的长度
    n = len(my_list)
    for i in range(n - 1):
        # 细节1：定义变量，记录具体的交换次数
        count = 0
        for j in range(n - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                count += 1
        # 细节3：打印每轮的交换次数
        print(f"第{i + 1}轮，交换了{count}次。。。")

        # 细节4：判断如果本轮没有发生交换，结束即可
        if count == 0:
            break
    return my_list


if __name__ == "__main__":
    my_list = [5, 3, 6, 7, 2]
    # my_list = [1, 2, 3, 4, 5]
    bubble_sort(my_list)
    print(my_list)
