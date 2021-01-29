
class CustomStack:
    def __init__(self):
        self.cursor = -1
        self.datas = []
    
    def push(self,value):
        self.datas.append(value)
        self.cursor = self.cursor + 1

    def pull(self):

        if (self.cursor < 0):
            print("this stack is null")
            return None

        temp = self.datas[self.cursor]
        self.datas.pop(self.cursor)
        self.cursor = self.cursor - 1
        return temp

# 测试字符
testStr = "(22(11)())"

mStack = CustomStack()

# 括号计数
count = 0

for i in testStr:
    # 添加 左
    if( i == "("):
        mStack.push(i)
    
    # 检测 右
    if(i == ")"):
        temp = mStack.pull()
        if( temp != "("):
           print("error" )
           break
        else:
            count = count + 1

print(count)