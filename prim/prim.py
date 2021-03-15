# 无限大
inf = 600

# 邻接矩阵
# graph =[[0,2,4,2],
#         [2,0,3,inf],
#         [4,3,0,3],
#         [2,inf,3,0]]

graph = [[0,6,1,5,inf,inf],
        [6,0,5,inf,3,inf],
        [1,5,0,5,6,4],
        [5,inf,5,0,inf,2],
        [inf,3,6,inf,0,6],
        [inf,inf,4,2,6,0]]

# 储存需要的边
edges = []
# 储存需要的边的相关点
vertexes = []

# 标记
book = [0]*len(graph)

# 给定初始点
vertexes.append(0)
book[0] = 1

while(len(vertexes) < len(graph)):
    bestEdge = (-1,-1,inf)
    # 以已经存储的点为起点，找边
    for vertex in vertexes:

        for i in range(0,len(graph)):
            # 查询还没有添加的点；并且是否比当前最优的还好
            if (book[i] != 1 and bestEdge[2] > graph[vertex][i]) :
                    bestEdge = (vertex,i,graph[vertex][i])
    
    # 找完，标记最优边
    vertexes.append(bestEdge[1])
    book[bestEdge[1]] = 1
    edges.append(bestEdge)

# 输出储存的边
for edge in edges:
    print("%d - %d : %f" % (edge[0],edge[1],edge[2]))