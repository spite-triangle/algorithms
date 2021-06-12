# 第四章第2节：解救小哈
# 迷宫地图
map = [[0,0,1,0],[0,0,0,0],[0,0,1,0],[0,1,6,0],[0,0,0,1]]
# 位移: 右，下，左，上
move = [[0,1],
        [1,0],
        [0,-1],
        [-1,0]]

# 标记走过的位置
book = [[0 for i in range(4)] for j in range(5)]

minStep = 100

def findPath(x:int,y:int,step:int):
    global minStep 
    # 结束条件
    if (map[y][x] == 6):
        if (step < minStep):
            minStep = step
        return

    # 所有可能性
    for i in range(0,4):
        xt = x + move[i][1]
        yt = y + move[i][0]

        # 边界检测
        if(xt < 0 or yt < 0 or xt >= 4 or yt >= 5):
            continue
        # 障碍检测；是否走过
        # print("%d,%d" % (xt,yt))
        if(book[yt][xt] == 0 and map[yt][xt] != 1):
            # 进入下一步
            book[yt][xt] = 1
            findPath(xt,yt,step + 1)
            
            # 从后面回退，回复状态
            book[yt][xt] = 0


book[0][0] = 1
findPath(0,0,0)
print(minStep)





