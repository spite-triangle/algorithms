class EdgeNode:
    """
    边节点
    """

    def __init__(self,ivex:int,ilink:EdgeNode,jvex:int,jlink:EdgeNode,weight:float):
        self.ivex = ivex
        self.ilink = ilink
        self.jvex = jvex
        self.jlink = jlink
        self.weight = weight
        # 标记：方便遍历
        self.mark = False

class VertexNode:
    """
    顶点节点
    """
    def __init__(self,ID:str,firstEdge:EdgeNode):
        self.ID = ID
        self.firstEdge = firstEdge

class GraphAgjacencyMulti:
    def __init__(self):
        self.vertexs = list()
        self.vertexCount = 0
        self.edgeCount = 0

    def getVertexIndex(self,vex:VertexNode):
        """
        通过顶点，获取顶点在数组中的的位置
        """
        for i in range(self.vertexCount):
            if(self.vertexs[i].ID == vex.ID):
                return i

        return -1
    
    def drawVertex(self,ID:str):
        """
        绘制图的点
        """
        self.vertexs.append(VertexNode(ID,None))
        self.vertexCount = self.vertexCount + 1

    def drawEdge(self,ivex:int,jvex:int,weight:float):
        """
        绘制图的边
        """

        # 创建边
        edge = EdgeNode(ivex,None,jvex,None,weight)

        # @note - i链表和j链表的实现
        # 1）firstEdge是头节点；
        # 2）新增节点是从链表头插入的。 

        # 关于 i 的链表：
        edge.ilink = self.vertexs[ivex].firstEdge
        self.vertexs[ivex].firstEdge = edge

        # 关于 j 的链表
        edge.jlink = self.vertexs[jvex].firstEdge
        self.vertexs[jvex].firstEdge = edge
        
        self.edgeCount = self.edgeCount + 1



if __name__ == "__main__":
    # 创建图
    graph = GraphAgjacencyMulti()

    # 画点
    graph.drawVertex("A")
    graph.drawVertex("B")
    graph.drawVertex("C")
    graph.drawVertex("E")
    graph.drawVertex("F")

    # 画边
    graph.drawEdge(0,1,1)
    graph.drawEdge(0,3,4)
    graph.drawEdge(0,5,3)
    graph.drawEdge(1,4,4)
    graph.drawEdge(5,4,5)
    graph.drawEdge(5,3,2)
    graph.drawEdge(4,2,1)

    print(graph.vertexs[0])