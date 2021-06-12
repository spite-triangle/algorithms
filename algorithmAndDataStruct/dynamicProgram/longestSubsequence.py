import numpy as np
# 获取最长的公共子序列
str1 = "\0eacsdr"
str2 = "\0abag"

# v(i,j):表述的是str1的第i位置与str2的第j位置时，公共子序列长度为v(i,j)
# v(i,j) = v(i-1,j-1) + 1, str1(i) == str2(j)
# v(i,j) = max(v(i-1,j),v(i,j-1)) ,str1(i) != str2(j)

v = [[0 for j in range(len(str2))] for i in range(len(str1))]

for j in range(1,len(str2)):
    for i in range(1,len(str1)):
        
        if str1[i] == str2[j]:
            v[i][j] = v[i-1][j-1] + 1
        else:
            v[i][j] = max(v[i-1][j],v[i][j-1])

print(np.array(v))