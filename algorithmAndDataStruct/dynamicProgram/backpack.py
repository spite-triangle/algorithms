import numpy as np 
# 物品
goods = {
    "lagtop":[3,2000],
    "noiser":[4,3000],
    "getar":[1,1500],
    "phone":[1,2000]
}

# 二维的问题描述式v(i,r)：到第i个物品，在重量为r的背包时，能装入的最高价值为v(i,r)
# 初始值都是 0
grid = [[ 0 for i in range(5)] for j in range(5)]

# 递推式求解
i = 1
for item,content in goods.items():
    weight = content[0]
    value = content[1]

    # 递推表达式
    for r in range(5):
        # 放不下,v(i,r) = v(i - 1,r)
        if(weight > r):
            grid[i][r] = grid[i - 1][r]
        # 能放下,v(i,r) = max(v(i-1,r),v(i-1,r-w[i]) + v[i])
        else:
            grid[i][r] = max(grid[i - 1][r],grid[i - 1][r - weight] + value)
    
    i = i + 1

print(np.array(grid))

goodsNames = []
for item in goods.keys():
    goodsNames.append(item)

tempValue = grid[4][4]
r = 4
# 反解最优路径
for index in range(len(goodsNames),0,-1):
    weight = goods[goodsNames[index - 1]][0]
    value = goods[goodsNames[index - 1]][1]

    # 从后向前遍历物品
    if((tempValue - value) == grid[index - 1][r - weight]):
        print(goodsNames[index - 1])
        r = r - weight
        tempValue = tempValue - value




    

    



