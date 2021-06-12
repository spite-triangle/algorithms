class Node:
    def __init__(self):
        self.data = 0
        self.next = None


class CustomLink:
    def __init__(self):
        self.lens = 0
        self.head = None

    # 生成节点
    def append(self,data):
        newNode = Node()
        newNode.data = data
        # 第一个节点
        if (self.head == None):
            self.head = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode

        self.lens = self.lens + 1

    # 显示信息
    def display(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
            

link = CustomLink()
link.append(1)
link.append(2)
link.append(3)

link.display()

