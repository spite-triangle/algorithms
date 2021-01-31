import numpy as np
class fill:
    def __init__(self,book:list,map:list):
        self.color = -1
        # 位移: 右，下，左，上
        self.move = [[0,1],
                [1,0],
                [0,-1],
                [-1,0]]
        self.book = book
        self.map = map

    def search(self,x:int, y:int):
        # 查找四周
        for i in range(4):

            xt = x + self.move[i][1]
            yt = y + self.move[i][0]

            if (xt < 0 or yt < 0 or xt >= 8 or yt >= 6):
                continue

            if (self.book[yt][xt] == 0 and self.map[yt][xt] !=0):

                self.book[yt][xt] = 1
                self.map[yt][xt] = self.color

                self.search(xt,yt)

# 地图
map = [[1,0,2,3,0,1,2,0],
       [0,0,1,2,3,0,0,0],
       [0,0,0,1,2,3,0,0],
       [0,1,0,1,0,0,0,0],
       [0,0,0,1,2,3,0,0],
       [1,2,3,0,0,0,0,0]]

# 标记
book = [[0 for i in range(8)] for j in range(6)]
mfill = fill(book=book,map=map)

for i in range(8):
    for j in range(6):
        if (mfill.book[j][i] == 0 and mfill.map[j][i] != 0):
            mfill.book[j][i] = 1
            mfill.map[j][i] = mfill.color
            mfill.search(i,j)
            mfill.color = mfill.color - 1

print(np.array(mfill.map))
