datas = [1,2,3,4,5,6,7,8,9,10,11]

target = 12

def search(low:int,high:int):

    # 序列中不存在：由于low向左移动，high向右移动。所以找不到的情况就是 low > high
    if (low > high):
        print("not found!!")
        return 

    # 中间位置: 奇数时，向下取整
    mid = int((high + low) / 2)

    # 小于 中间 的值
    if (target < datas[mid]):
        high = mid - 1

    # 大于 中间 的值
    if (target > datas[mid]):
        low = mid + 1

    # 等于 中间 的值
    if (target == datas[mid]):
        print(mid)
        return

    search(low,high)

search(0,len(datas)-1)