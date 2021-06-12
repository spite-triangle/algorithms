
# 盒子
box = [-1]*3
# 标记card是否放入箱子
book = [0]*4
n = 3

def dfs(loc):

    # 递归终止条件
    sum = 0
    for item in book:
        sum = sum + item

    if (sum >= len(box) ):
        mstr = ""

        for item in box:
            mstr = mstr + str(item)

        print(mstr)
        return

    # 尝试所有可能
    for i in range(1,n+1):
        if (book[i] == 0):
            # 放入
            box[loc] = i
            book[i] = 1

            # 移动一步
            loc = loc + 1
            dfs(loc)

            # 从前面回退；复原状态
            loc = loc - 1
            book[i] = 0

dfs(0)