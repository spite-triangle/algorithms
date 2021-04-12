# 通过二分法，从一个有序序列中找到最靠近的指定数的区间

# 有序序列
datas = [0,1.2,3,3.5,5,6,9]

# 指定值
value = 4
# 指定数的左右值
left = 0
right = len(datas) - 1

while(True):
    if((right - left) == 1):
        print("left: %d, right: %d"%(left,right))
        break
    mid = int((left + right)/2)

    # 大于等于中间
    if(value >= datas[mid]):
        left = mid

    # 小于中间
    if(value < datas[mid]):
        right = mid
