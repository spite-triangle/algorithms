# 实现四则运算计算器

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkStack:
    def __init__(self):
        self.head = None
        self.len = 0

    def push(self,data):
        # 上一个头节点
        lastNode = self.head
        # 新建一个节点
        self.head = Node(data)
        self.head.next = lastNode
        self.len = self.len + 1

    def pull(self):
        if (self.len <= 0):
            return None

        # 要弹出的首节点
        head = self.head
        # 弹出第一个
        self.head = self.head.next
        self.len = self.len - 1
        return head.data

    def display(self):
        
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

# 定义优先等级
order = {'+':1,'-':1,'*':2,'/':2}
# 运算符号
flags = ['+','-','*','/','(',')']

def suffixExpression(expression:list):
    """
    将表达式转为 后缀表达式
    """
    flagStack = LinkStack()
    out = []

    for item in expression:
        # 是否为数字
        isNumber = True
        # 是否为运算符号
        isOparetor = True

        # 符号
        for flag in flags:
            if (item == flag):
                # 括号处理
                if(item == '('):
                    flagStack.push(item)
                    isOparetor = False
                # 括号处理
                if(item == ')'):
                    temp = flagStack.pull()
                    while(temp != '('):
                        out.append(temp)
                        temp = flagStack.pull()

                    isOparetor = False

                # 符号优先等级处理
                while(isOparetor):
                    if (flagStack.len == 0 or flagStack.head.data == '('):
                        flagStack.push(item)
                        break

                    elif (order[item] > order[flagStack.head.data]):
                        flagStack.push(item)
                        break

                    else:
                        out.append(flagStack.pull())

                isNumber = False
                break
        # 数字
        if(isNumber):
            out.append(item)

    temp = flagStack.pull()
    while(temp):
        out.append(temp)
        temp = flagStack.pull()

    return out

def calculation(suffix:list):
    """
    后缀表达式运算
    """
    numberStack = LinkStack()
    for item in suffix:
        isFlag = False
        # 搜寻符号
        if(item == '+'):
            res = numberStack.pull() + numberStack.pull()
            numberStack.push(res)
            isFlag = True
        if(item == '-'):
            res = -(numberStack.pull() - numberStack.pull())
            numberStack.push(res)
            isFlag = True
        if(item == '*'):
            res = numberStack.pull() * numberStack.pull()
            numberStack.push(res)
            isFlag = True
        if(item == '/'):
            res = 1 / (numberStack.pull() / numberStack.pull())
            numberStack.push(res)
            isFlag = True
        if(not isFlag):
            numberStack.push(float(item))
    return numberStack.pull()



stack = LinkStack()

# 后缀表达式
# mstr = "9+(3-1)*3+10/2"
mstr = ['9','+','(','3','-','1',')','*','3','+','10','/','2']

out = suffixExpression(mstr)
print(calculation(out))