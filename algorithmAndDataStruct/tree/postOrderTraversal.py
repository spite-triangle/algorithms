# 链表二叉树
class Node:
    def __init__(self,leftChild = None,rightChild = None,data = None):
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.data = data

a = Node(data='A')
b = Node(data='B')
c = Node(data='C')
d = Node(data='D')
e = Node(data='E')
f = Node(data='F')
g = Node(data='G')
h = Node(data='H')

# 搭建一个二叉树
a.leftChild = b
a.rightChild = e
b.leftChild = c
c.rightChild = d
e.leftChild = f
f.leftChild = h
f.rightChild = g

# 遍历二叉树
def traversal(T:Node):
    # 条件
    if (T == None):
        return
    # 搜索所有可能性
    traversal(T.leftChild)
    traversal(T.rightChild)
    print(T.data)

traversal(a)