
class CustomQueue:
    def __init__(self):
        # 首
        self.head = 0
        # 尾
        self.tail = 0
        # 数据储存
        self.datas = []

    def push(self,number:float):
        self.datas.append(number)
        self.tail = self.tail + 1

    def pull(self):
        # 空队列检测
        if(self.head == self.tail):
            print("this queue is null")
            return None

        temp = self.datas[self.head]
        self.head = self.head + 1

        return temp

mqueue = CustomQueue()
mqueue.push(1)
mqueue.push(2)
mqueue.push(3)




