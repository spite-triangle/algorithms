# 等待排序数组
mArray = [5,12,5,7,2,4,5]


def quickSort(left:int,right:int):
    """
    快速排序法
    
    参数：
        left,right: 数组下标 的 起始 与 终止
        
    """
    # 递归结束标志
    if (left >= right):
        return

    i = 0    
    j = 0
    base = mArray[left]
    
    # 左小，右大
    while (True):
        # 移动j
        for j in range(right,left-1,-1):
            # 当j主动与i相遇。可优化到 while
            if (j == i):
                break
            # 从右向左，找到小于 基
            if (mArray[j] < base):
                break

        # 移动i
        for i in range(left,right + 1):
            # 当i主动与j相遇。可优化到while
            if (i == j):
                break

            # 从左向右，找到大于 基
            if(mArray[i] > base):
                break

        # 交换最大与最小
        if(i == j):
            # 当 i主动遇到 j, j的最后停留的地方，一定 < base
            # 当 j主动遇到 i, i的最后停留的地方，一定 <= base
            mArray[left] = mArray[j]
            mArray[j] = base
            break
        else:
            temp = mArray[i]
            mArray[i] = mArray[j]
            mArray[j] = temp

    # 基础位 左边 排序。递归处理
    quickSort(left,i-1)
    # 基础位 右边 排序。递归处理
    quickSort(i+1,right)

quickSort(0,len(mArray) - 1)
print(mArray)