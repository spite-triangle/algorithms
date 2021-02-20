import numpy as np
str1 = "abecd"
str2 = "abceabe"

# v(i,j):表述的是str1的第i位置与str2的第j位置时，公共子串长度为v(i,j)
# v(i,j) = v(i - 1,j - 1) + 1，str1(i)与str2(j)相等
# v(i,j) = 0，str1(i)与str2(j)不相等

v = [[ 0 for j in range(len(str2) + 1) ] for i in range(len(str1) + 1)]

for i in range(1,len(str1) + 1):
    for j in range(1,len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            v[i][j] = v[i - 1][j - 1] + 1
        else:
            v[i][j] = 0

print(np.array(v))

# 获取子串：找v中的最大值，然后记录最大值的i或者j，将str1或者str2视作char[]，最后进行遍历就行。