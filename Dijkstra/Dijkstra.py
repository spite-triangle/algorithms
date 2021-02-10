# 有向图
graph = {
    "A":{
        "B":5,
        "C":2
    },
    "B":{
        "D":4,
        "E":2
    },
    "C":{
        "B":8,
        "E":7,
    },
    "D":{
        "E":6,
        "F":3
    },
    "E":{
        "F":1
    },
    "F":{}
}

graph.clear()

# 无向图
graph = {
    "A":{
        "B":1,
        "C":2
    },
    "B":{
        "A":1,
        "D":3
    },
    "C":{
        "A":2,
        "D":4
    },
    "D":{
        "B":3,
        "C":4
    }
}

# 消费表：记录 从起始点到该节点的 费用
cost = {}
# 父节点表：记录 当前节点的父节点，用于回找路径
parent = {}
# 标记已经搜寻了的点
book = []

def find(begin):

    # 搜索begin节点下的邻居节点
    for item in graph[begin].keys():
        # 计算当前节点的当前cost
        temp = cost[begin] + graph[begin][item]
        # 当前搜寻到的节点是否在cost中，不在则添加，否则就与原来的cost进行比较
        if(item not in cost.keys()):
            cost[item] = temp
            parent[item] = begin
        else:
            if(cost[item] > temp):
                cost[item] = temp
                parent[item] = begin

    # 标记begin节点，不在进行二次寻找
    book.append(begin)

    # 找下一个最低cost的节点
    lowCost = 1000
    lowCostNode = None
    for item in cost.keys():
        if (item not in book and lowCost > cost[item]):
            lowCost = cost[item]
            lowCostNode = item

    # 当 lowCostNode 为 None 表示都搜索完毕
    if(lowCostNode == None):
        return
    else:
        find(lowCostNode)


begin = "A"
final = "D"

cost[begin] = 0
parent[begin] = None

find(begin)
print(cost[final])

# 显示路径
item = final
mstr = ""
while(parent[item] != None):
    mstr = mstr + item + "<===="
    item = parent[item]
mstr = mstr + begin
print(mstr)

    













