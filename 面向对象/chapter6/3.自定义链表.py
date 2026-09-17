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


# SingleNode对象，有元素域 item 和 地址域 next两个属性
# 链表对象，有head属性


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

    # 5. add 链表头部增加节点

    def add(self, item):
        new_node = SingleNode(item)
        new_node.next = self.head
        self.head = new_node
        print(f'新节点"{item}"添加完毕。。。')

    # 6. append
    def append(self, item):
        # 创建一个新的节点
        new_node = SingleNode(item)
        # 判断链表，如果头节点为空，或者链表的isEmpty属性为True，说明链表没有节点，直接加
        if self.head is None:
            self.head = new_node
        # 如果不为空，则通过循环遍历到最后一个节点它的地址域名为None，则给这个节点的地址域替换成新节点
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        print(f"New node {item} has been append")

    # 7. insert
    def insert(self, item, pos):
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            cur = self.head
            count = 0
            # 只要当前节点的位置<pos-1，就一直循环
            while count < pos - 1:
                cur = cur.next
                count += 1
            new_node = SingleNode(item)
            # 设置 新节点的地址域，指向 插入位置前那个节点的的地址域
            new_node.next = cur.next
            # 插入节点的上个节点指向新节点
            cur.next = new_node
        print(f"新节点 {item} 插入完毕！")

    # 8. remove
    def remove(self, item):
        # 创建游标（表示当前节点），默认从头开始
        cur = self.head
        # 定义变量，记录要删除节点的 前驱节点
        pre = None

        # 遍历
        while cur is not None:
            if cur.item == item:
                if cur == self.head:
                    # cur.next = None
                    self.head = cur.next

                else:
                    # 要删除的节点的前置节点指向当前节点的后续节点
                    pre.next = cur.next

                cur.next = None  # 可不写
                print(f'节点 "{item}" 删除成功')
                return  # 删除成功后，跳出循环，函数结束
            else:
                # 游标后移
                pre = cur
                cur = cur.next
        print(f'没有找到该节点"{item}"')

    # 9. search 查找节点是否存在
    def search(self, item):
        cur = self.head

        while cur.next is not None:
            if cur.item == item:
                print(f'节点 "{item}" 存在！')
                break
            else:
                cur = cur.next
        # while循环结束，么有break
        else:
            print(f'节点 "{item}" 不存在！')


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
    print("#" * 34)
    # 6.测试遍历
    ll5.traverse()
    print("#" * 34)
    # 7.测试增加节点
    ll5.add("虚竹")
    ll5.add("鸠摩智")
    ll5.traverse()
    print(ll5.length())
    print("#" * 34)
    # 8.测试尾部增加节点
    ll5.append("萧远山")
    ll5.traverse()
    print(ll5.length())
    print("#" * 34)
    # 9.测试插入位置
    ll5.insert("慕容博", 2)
    ll5.traverse()
    print("#" * 34)
    # 10.测试删除
    ll5.remove("萧远山")
    ll5.traverse()
    print("#" * 34)
    # 11.测试存在
    ll5.search("慕容复")
    ll5.search("慕容博")
