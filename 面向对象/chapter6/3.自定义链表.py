"""
链表介绍：
    概述：
        它属于数据结构之线性结构的一种，每个节点只有一个前驱和一个后继节点
    作用：
        优化顺序表的弊端（扩容失败）
        链表扩容不需要连续的内存空间
    组成：
        由 节点 组成，其中节点由 元素域 和 链接域 组成
    分类：
        单向链表：节点由1个数值域 和 一个地址域组成，前面节点的地址域存储的是后续节点的地址，最后一个节点的地址域为None
        单向循环链表
        双向链表
        双向循环链表

"""


class SingleNode:
    def __init__(self, item):
        self.item = item  # 元素域
        self.next = None  # 地址域


class SingleLinkedList:
    # 1. 初始化属性
    def __init__(self, node=None):
        self.head = node  # 链表的头节点，指向第一个节点

    # 2. isEmpty(self)
    def isEmpty(self):
        # 头节点如果为空说明链表为空
        return self.head is None

    # 3. length
    def length(self):
        count = 0
        cur = self.head

        while cur is not None:
            count += 1
            cur = cur.next
        return count

    # 4. traverse
    def traverse(self):
        cur = self.head
        print("开始遍历。。。")
        while cur is not None:
            print(f"数值域:{cur.item}")
            cur = cur.next

    # 5. add

    # 6. append

    # 7. insert

    # 8. remove

    # 9. search


if __name__ == "__main__":
    # 测试节点
    node1 = SingleNode("萧峰")
    print(f"数值域：{node1.item}")
    print(f"地址域：{node1.next}")
    print(node1)

    print("#" * 34)

    # 测试链表
    my_linkedlist = SingleLinkedList(node1)
    print(f"链表头节点为：{my_linkedlist.head}")
    if my_linkedlist.head:
        print(f"链表头节点的元素域：{my_linkedlist.head.item}")
        print(f"链表头节点的地址域：{my_linkedlist.head.next}")
    print("#" * 34)
    # 4.测试链表是否为空
    ll4 = SingleLinkedList()
    print(f"ll4为空是{'对' if ll4.isEmpty() else '错'}的")
    print("#" * 34)
    # 5.测试链表长度
    ll5 = SingleLinkedList(node1)
    print(f"链表ll5长度为{ll5.length()}")

    ll5.traverse()
