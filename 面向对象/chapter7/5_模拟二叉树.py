"""
树结构解释：
  概述：
    它属于数据结构的一种，属于非线性结构
  特点：
    1. 又只有一个根节点
    2. 每个节点可以有任意个子节点
    3. 没有子节点的节点，称之为 叶子节点
"""


class Node:
    def __init__(self, item):
        # 元素域
        self.item = item
        self.lchild = None
        self.rchild = None


class BinaryTree:
    def __init__(self, node=None):
        # 根节点
        self.root = node

    def add(self, item):
        pass

    def breadth(self):
        pass

    def preorder(self):
        pass

    def inorder(self):
        pass

    def postorder(self):
        pass


def test_dm1():
    # 1. 创建节点
    node1 = Node("A")
    # 2. 打印
    print(node1.item)
    print(node1.lchild)
    print(node1.rchild)
    print("*" * 34)


if __name__ == "__main__":
    test_dm1()

    # 1. 创建队列，先进先出
    queue = []
    # 2. 模拟添加元素
    queue.append("A")
    queue.append("B")
    queue.append("C")

    # 3. 模拟从队列中取出元素

    # 4. 打印
    print(queue)
