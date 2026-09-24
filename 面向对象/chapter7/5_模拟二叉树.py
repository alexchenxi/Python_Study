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
        # 1.把item封装成节点
        new_node = Node(item)
        # 2.判断根节点是否为空
        if self.root is None:
            self.root = new_node
            return
        # 3.创建队列，添加 根节点到队列中
        queue = []
        queue.append(self.root)
        # 4. 找到空缺的节点位置
        while True:
            # 5. 获取队列的第一个元素
            node = queue.pop(0)
            # 6. 判断当前左子树
            if node.lchild is None:
                node.lchild = new_node
                return
            else:
                # 把当前节点的左子树，添加到队列里
                queue.append(node.lchild)

            # 7. 右子树
            if node.rchild is None:
                node.rchild = new_node
                return
            else:
                # 把当前节点的右子树，添加到队列里
                queue.append(node.rchild)

    def breadth(self):
        # 1. 判断根节点为空
        if self.root is None:
            print("这个二叉树是空的")
            return
        # 2. 创建队列，添加根节点到队列
        queue = []
        queue.append(self.root)
        index = 1
        while len(queue) > 0:
            node = queue.pop(0)
            print(f"{index}. {node.item}", end=" ")
            index += 1
            # 判断当前节点左子树是否为空
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)

    def preorder(self, root):
        if root is not None:
            print(root.item, end=" ")
            self.preorder(root.lchild)
            self.preorder(root.rchild)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.lchild)
            print(root.item, end=" ")
            self.inorder(root.rchild)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.lchild)
            self.postorder(root.rchild)
            print(root.item, end=" ")


def test_dm1():
    # 1. 创建节点
    node1 = Node("A")
    # 2. 打印
    print(node1.item)
    print(node1.lchild)
    print(node1.rchild)
    print("*" * 34)


def test_dm2():
    # 1. 创建队列，先进先出
    queue = []
    # 2. 模拟添加元素
    queue.append("A")
    queue.append("B")
    queue.append("C")
    print(queue.pop(0))  # 删除索引的元素并返回元素
    print(queue.pop(0))
    print(queue.pop(0))
    # 3. 模拟从队列中取出元素

    # 4. 打印
    print(queue)


# 广度优先遍历
def test_breadth_query():
    # 1.创建二叉树
    node = Node("朱元璋")
    bt = BinaryTree(node)

    # 2. 添加元素
    bt.add("朱标")
    bt.add("朱棣")
    bt.add("朱允炆")
    bt.add("朱标儿子2")
    bt.add("朱高炽")
    bt.add("朱高煦")
    # 3. 广度优先遍历
    bt.breadth()


# 深度优先遍历
def test_order_query():
    # 1.创建二叉树
    node = Node("朱元璋")
    bt = BinaryTree(node)

    # 2. 添加元素
    bt.add("朱标")
    bt.add("朱棣")
    bt.add("朱允炆")
    bt.add("朱标儿子2")
    bt.add("朱高炽")
    bt.add("朱高煦")
    # 3. 广度优先遍历
    bt.preorder(node)
    print()
    print("#" * 34)
    bt.inorder(node)
    print()
    print("#" * 34)
    bt.postorder(node)


if __name__ == "__main__":
    # test_dm1()
    # test_dm2()
    test_order_query()
