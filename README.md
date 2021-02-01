## 《阿哈！算法》
* 快速排序： [quick sort](quicksort/quicksort.py)
* 队列: [queue](queue/queue.py)
* 栈：[stack](stack/stack.py)

    可以用来处理**对称问题**

* 链表：[link](link/link.py), [simulation link](link/simLink.py)
* 深度搜索：[depth first search](depthfFirstSearch/depthFirstSearch.py)
```c++
    void search(location){
        // 期望的结束条件
        if(){
            return;
        }

        // 尝试所有可能性，向后移动
        for(){

            // 移动到下一步
            loctation = location + 1;
            search(location);

            // 从 后面 回退回来，复原状态
            location = location - 1;
        }

        // 隐含的结束条件：**不能向后移动时，回退**
        return ;
    }
```

* 广度搜索：[breadth first search](breadth_first_search/breadthFirstSearch.py)
```c++
    void search(location){

        // 尝试**当前点**对应的所有可能性；
        for(){
            // 将移动的一步入对
            queue.push(location + 1);

            // 找到目的时，就结束递归
            if(){
                return;
            }
        }

        // 将**当前点**出队
        queue.pull();

        // 队列为空。没有找到目标，结束递归
        if(queue.head == queue.tail){
            return;
        }

        // 以队首为**起始点**继续处理
        search(queue.head)
    }
```
* 漫水填充：[floodfill](floodFill/floodFill.py)

    基于 *深度搜索*  或者 *广度搜索*

* 图 的遍历：[depth first search](graph_search/depth_first_search.py); [breadth first search](graph_search/breadth_first_search.py)