# 需要覆盖的所有州
remainStates = set({"mt","wa","or","id","nv","ut","ca","az"})

# 广播电视台
stations = {
    "kone":set(["id","nv","ut"]),
    "ktwo":set(["wa","id","mt"]),
    "kthree":set(["or","nv","ca"]),
    "kfour":set(["nv","ut"]),
    "kfive":set(["ca","az"])
}

# 最终的电视台
finalSet = set()

while(len(remainStates) > 0):
    bestStation = ""
    bestCover = set()
    
    # 当前覆盖最多的
    for item in stations.keys():
        if (item not in finalSet):
            # 覆盖的
            cover =  stations[item] & remainStates
            
            if (bestStation == ""):
                bestStation = item
                bestCover = cover
                continue

            if (len(bestCover) < len(cover)):
                bestStation = item
                bestCover = cover
    
    # 剔除掉已经覆盖的州
    remainStates = remainStates - bestCover
    # 添加最好的
    finalSet.add(bestStation)

print(finalSet)





