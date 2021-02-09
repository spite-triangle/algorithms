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

## 《图解算法》
* 二分法查找：只能用于查找有序的数据 [dichotomizing search](dichotomizing_search/dichotomizingSearch.py)
```c++
    search(int low,int high){
        // 序列中不存在：由于low向左移动，high向右移动。所以找不到的情况就是 low > high
        if(low > high){
            return "not found";
        }
        // 中间位置: 奇数时，向下取整
        int mid = (low + high) / 2;
        // 小于 中间 的值
        if(target < datas[mid]){
            high = high - 1;
        }
        // 大于 中间 的值
        if(target > datas[mid]){
            low = low + 1;
        }
        // 等于 中间 的值
        if(target == datas[mid]){
            return mid;
        }

        // 下一次查找
        search(low,high);
    }

```

* 大O表示法：描述的是运算时间的增量，而非运算时间
    ![bigO](image/bigO.png)
> 1. 对一些算法的运算速度比较时，大O表示法中的省略项，例如(c * n)中的c，将起到主导作用。
> 2. 对于递归的表示：O(调用栈的高度 * 一层中的O())

* 递归的一般形式
```c++
    T function(T input){
        // 基线条件
        if(){
            return ;
        }

        // 递归条件
        ...
        function(nextInput);
        ...
        return;
    }
```

* D&C 分而治之 的思路：
> 1. 找到问题最简单的形式，作为**基线条件**
> 2. 找到实现问题能重复最简化的过程

* 图的储存方式：
> 1. [邻近矩阵](graph_search/breadth_first_search.py)
> 2. [键值对](graph_search/breadthFirstSearchMap.py)

## 《大话数据结构》
* 链表栈：[link stack](stack/LinkStack.py)
* 四则表达式运算：[四则表达式运算](example/calculator.py)

    1. 中缀表达式转后缀表达式
        ![suffix](image/suffixExpression.png)
    2. 后缀表达式运算
* 循环队列：[loop queue](queue/loopQueue.py)