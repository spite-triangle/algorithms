class CustomQueue:
    def __init__(self):
        # 首
        self.head = 0
        # 尾
        self.tail = 0
        # 数据储存
        self.datas = []

    def push(self,data):
        self.datas.append(data)
        self.tail = self.tail + 1

    def pull(self):
        # 空队列检测
        if(self.head == self.tail):
            print("this queue is null")
            return None

        temp = self.datas[self.head]
        self.head = self.head + 1

        return temp

class Node:
    def __init__(self,name:str,step:int):
        self.name = name
        self.step = step

graph = {}
graph["you"] = ["bob","claire","alice"]
graph["bob"] = ["anuj","peggy"]
graph["anuj"] = []
graph["peggy"] = []
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["thom"] = []
graph["jonny"] = []

queue = CustomQueue()

# 移动点标记
book = []


def find(name:str,step:int):

    # 四周搜寻
    for item in graph[name]:
        # 找到 目标 就返回步长
        if (item == "anuj"):
            print(step + 1)
            return

        if (item not in book):
            queue.push(Node(item,step + 1))
            book.append(item)
    
    # 弹出第一个，用第二点作为下一次的迭代起点
    queue.pull()

    # 搜寻完毕，没找到
    if (queue.head == queue.tail):
        print("over")
        return

    find(queue.datas[queue.head].name,queue.datas[queue.head].step)

# 起始点
queue.push(Node("you",0))
book.append("you")
find("you",0)