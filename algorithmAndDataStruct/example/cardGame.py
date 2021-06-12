# 队列与栈
import random

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

class CustomStack:
    def __init__(self):
        self.cursor = -1
        self.datas = []
    
    def push(self,value):
        self.datas.append(value)
        self.cursor = self.cursor + 1

    def pull(self):

        if (self.cursor < 0):
            print("this stack is null")
            return None

        temp = self.datas[self.cursor]
        self.datas.pop(self.cursor)
        self.cursor = self.cursor - 1
        return temp

hong = CustomQueue()
ming = CustomQueue()
gameTable = CustomStack()
book = [0]*10

hong.push(2)
hong.push(4)
hong.push(1)
hong.push(2)
hong.push(5)
hong.push(6)

ming.push(3)
ming.push(1)
ming.push(3)
ming.push(5)
ming.push(6)
ming.push(4)

# ming.push(2)
# ming.push(4)
# ming.push(1)
# ming.push(2)
# ming.push(5)
# ming.push(6)

# hong.push(3)
# hong.push(1)
# hong.push(3)
# hong.push(5)
# hong.push(6)
# hong.push(4)


while(True):
    if(hong.head == hong.tail):
        print("win ming")
        print(ming.tail - ming.head)
        print(hong.tail - hong.head)
        break

    if(ming.head == ming.tail):
        print("win hong")
        print(hong.tail - hong.head)
        print(ming.tail - ming.head)
        break

    hongCard = hong.pull()
    # 判断Hong是否得牌
    if(book[hongCard] == 1):
        # 刚出的拿回去
        hong.push(hongCard)
        # 拿牌桌上的
        while(True):
            temp = gameTable.pull()

            hong.push(temp)
            book[temp] = 0

            if( temp == hongCard):
                break
        
    else:
        book[hongCard] = 1
        gameTable.push(hongCard)

    mingCard = ming.pull()

    if(book[mingCard] == 1):
        # 刚出的拿回去
        ming.push(mingCard)
        # 拿牌桌上的
        while(True):
            temp = gameTable.pull()
            if (temp == None):
                print(temp)

            ming.push(temp)
            book[temp] = 0
            
            if( temp == mingCard):
                break
    else:
        book[mingCard] = 1
        gameTable.push(mingCard)




