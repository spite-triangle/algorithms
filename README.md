## 《阿哈！算法》
* 快速排序： [quick sort](quicksort/quicksort.py)
* 队列: [queue](queue/queue.py)
* 栈：[stack](stack/stack.py)

    可以用来处理**对称问题**

* 链表：[link](link/link.py), [simulation link](link/simLink.py)
* 深度搜索：[depth first search](depthfFirstSearch/depthFirstSearch.py)
```c++
    void search(location){
        // 递归结束条件
        if(){
            return;
        }
        // 尝试所有可能性
        for(){
            // 当前操作

            // 移动到下一步
            loctation = location + 1;
            search(location);

            // 从 后面 回退回来，复原状态
            location = location - 1;
        }
    }
```