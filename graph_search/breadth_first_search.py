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

# 图的 邻接矩阵 : 表示了图节点之间的连接关系
graph = [[0,1,1,-1,1],
        [1,0,-1,1,-1],
        [1,-1,0,-1,1],
        [-1,1,-1,0,-1],
        [1,-1,1,-1,0]]

# 标记
book = [0]*5

queue = CustomQueue()

def search(num:int):

    # 打印当前节点
    print(num)

    # 搜索 
    for i in range(5):
        if ( graph[num - 1][i] == 1 and book[i] == 0):
            book[i] = 1
            # 储存搜索到的 节点
            queue.push(i + 1)
    
    # 当前节点出队
    queue.pull()
    # 判断是否搜索完毕
    if(queue.head == queue.tail):
        return
    # 搜索下一个起点
    search(queue.datas[queue.head])

book[0] = 1
queue.push(1)

search(1)