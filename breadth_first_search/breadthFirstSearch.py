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
    def __init__(self,x:int,y:int,step:int):
        self.x = x
        self.y = y
        self.step = step

# 迷宫地图
map = [[0,0,1,0],[0,0,0,0],[0,0,1,0],[0,1,6,0],[0,0,0,1]]
# 位移: 右，下，左，上
move = [[0,1],
        [1,0],
        [0,-1],
        [-1,0]]
# 搜索用的队列
queue = CustomQueue()

# 移动点标记
book = [[0 for i in range(4)] for j in range(5)]


def find(x:int,y:int,step:int):

    # 四周搜寻
    for i in range(4):
        xt = x + move[i][1]
        yt = y + move[i][0]

        # 边界
        if(xt < 0 or yt < 0 or xt >= 4 or yt >= 5):
            continue
        # 障碍
        if(book[yt][xt] == 0 and map[yt][xt] != 1):
            book[yt][xt] = 1
            queue.push(Node(xt,yt,step + 1))

        # 结束条件
        if(map[y][x] == 6):
            print(step)
            return
    
    # 弹出第一个，用第二点作为下一次的迭代起点
    queue.pull()

    # 搜寻完毕，没找到
    if (queue.head == queue.tail):
        print("over")
        return

    find(queue.datas[queue.head].x,queue.datas[queue.head].y,queue.datas[queue.head].step)

# 起始点
queue.push(Node(0,0,0))
book[0][0] = 1
find(0,0,0)