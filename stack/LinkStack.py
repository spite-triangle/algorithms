
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkStack:
    def __init__(self):
        self.head = None
        self.len = 0

    def push(self,data):
        # 上一个头节点
        lastNode = self.head
        # 新建一个节点
        self.head = Node(data)
        self.head.next = lastNode
        self.len = self.len + 1

    def pull(self):
        if (self.len <= 0):
            return

        # 要弹出的首节点
        head = self.head
        # 弹出第一个
        self.head = self.head.next
        self.len = self.len - 1
        return head.data

stack = LinkStack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pull())
print(stack.pull())
print(stack.pull())