class SimulateLink:
    def __init__(self):
        # 用于数据储存
        self.datas = []
        # 储存 next
        self.nexts = []
        # 表头
        self.head = 0

    def append(self,data):
        self.datas.append(data)
        self.nexts.append(len(self.datas))

    def display(self):
        cursor = self.head
        while(cursor < len(self.datas)):
            print(self.datas[cursor])
            cursor = self.nexts[cursor]

link = SimulateLink()
link.append(1)
link.append(2)
link.append(3)

link.display()