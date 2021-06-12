class CustomHeap:
    def createHeap(self,datas:list):
        """
        创建堆            
        """
        self.n = len(datas)
        # 0下标不要：0 * any = 0 会导致错误
        self.datas = datas
        self.datas = [0]*(len(datas) + 1)
        for i in range(1,len(self.datas)):
            self.datas[i] = datas[i - 1]
        
        # 从最后一个父节点进行调制
        for i in range(int(self.n / 2),0,-1):
            self.siftDownNode(i)
            
    def swapNode(self,i:int,j:int):
        temp = self.datas[i]
        self.datas[i] = self.datas[j]
        self.datas[j] = temp    

    def addNode(self,data):
        """
        在末尾创建一个节点
        """
        self.datas.append(data)
        self.n = self.n + 1
        self.siftUpNode(self.n)
    
    def removeRoot(self):
        """
        删除根节点，并返回
        """
        temp = self.datas[1]
        # 将最后一个节点移动到第一个
        self.datas[1] = self.datas[self.n]
        self.siftDownNode(1)
        self.datas.pop(self.n)
        self.n = self.n - 1
        return temp


    def siftUpNode(self,i:int):
        """
        向上移动节点
        """
        # 到根节点的时候，停止
        while(i > 1):
            # 子节点小于父节点
            if(self.datas[i] < self.datas[int(i/2)]):
                self.swapNode(i,int(i/2))
                i = int(i / 2)
            else:
                break
            

    def siftDownNode(self,i:int):
        """
        向下移动节点
        """
        while (True):
            # 是否有左节点
            if (i*2 <= self.n):
                # 与子左节点的关系
                if (self.datas[i] > self.datas[2*i]):
                    minum = i * 2
                else:
                    minum = i
            else:
                # 没有子左节点，肯定没有子右节点。到头了
                break

            # 是否有右节点
            if (i*2 + 1 <= self.n):
                if(self.datas[minum] > self.datas[i*2 + 1]):
                    minum = i * 2 + 1

            # 相等说明，i当前就是子树中最小的。
            if(minum != i):
                self.swapNode(minum,i)
                i = minum
            else:
                break

datas = [100,1,6,2,7,9,8]
mheap = CustomHeap()
mheap.createHeap(datas)

print(mheap.datas)

for i in range(3):
    mheap.removeRoot()

print(mheap.datas)
mheap.addNode(5)
mheap.addNode(1)
print(mheap.datas)
