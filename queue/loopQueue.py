class CustomQueue:
    def __init__(self,n:int):
        self.head = 0
        self.tail = 0
        self.datas = [0] * n
        self.dataSize = n

    def push(self,data):
        
        # self.tail + 1 : 预留一个位置出来，让头尾不重合
        if ((self.tail + 1)% self.dataSize == self.head):
            print("dont push")
            return None
        
        self.datas[self.tail] = data
        # 使用 % 运算让标签循环
        self.tail = (self.tail + 1) % self.dataSize


    def pull(self):

        # 空 判断
        if (self.head == self.tail):
            return None

        temp = self.datas[self.head]
        # 使用 % 运算让标签循环
        self.head = (self.head + 1) % self.dataSize

        return temp

    def getLen(self):
        return (self.tail - self.head + self.dataSize) % self.dataSize

    def display(self):
        for i in range(self.getLen()):
            print(self.datas[(self.head + i) % self.dataSize])

queue = CustomQueue(4)

queue.push(1)
queue.push(2)
queue.push(3)
queue.display()

queue.pull()
queue.push(4)
queue.pull()
queue.push(5)
print("  ")
queue.display()
print(queue.getLen())