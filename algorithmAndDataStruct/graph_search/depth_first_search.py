
# 图的 邻接矩阵 : 表示了图节点之间的连接关系
graph = [[0,1,1,-1,1],
        [1,0,-1,1,-1],
        [1,-1,0,-1,1],
        [-1,1,-1,0,-1],
        [1,-1,1,-1,0]]

# 标记
book = [0]*5

def search(num:int):
    # 打印当前节点
    print(str(num))

    # 遍历所有可能性
    for i in range(5):
        # 查找当前节点的下一节点
        if ( graph[num - 1][i] == 1 and book[i] == 0 ):
            book[i] = 1
            search(i + 1)

book[0] = 1
search(1)