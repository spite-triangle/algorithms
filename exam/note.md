<h1>刷题笔记</h1>

---
[toc]

---
# 一、字符串

## 1.1 [字符串最后一个单词的长度](https://www.nowcoder.com/practice/8c949ea5f36f422594b306a2300315da?tpId=37&&tqId=21224&rp=1&ru=/ta/huawei&qru=/ta/huawei/question-ranking)

- 输入一行字符串
    ```c++
        // 声明字符串的大小
        char buffer[512];
        // ^ : 表示输入到 ^ 之后的字符终止。
        scanf("%[^\n]",buffer);
        // 读取一行字符串；最多只读取 sizeof(buffer) - 1个字符，最后一个放 '\0'
        fgets(buffer, sizeof(buffer), stdin);
        // c++输入
        string str;
        cin >> str;
    ```
- 字符数组，字符串转换
    ```c++
        // 字符数组转string
        string str(char*);
        string a = string(char *); 
        // string 转字符数组
        char * b = a.c_str();
    ```
- 分割字符串
    &emsp;`char* str` **会被修改**。
    ```c++
        #include <string.h>

        vector<string> split(char * str,const char * sep){
            vector<string> strs;
        
            char * buffer;
        
            buffer = strtok(str,sep);
        
            while(buffer){
                strs.push_back(string(buffer));
                buffer = strtok(NULL,sep);
            }
            return strs;
        } 
    ```
- `string` 的长度 **不包括 `\0`**

    ```c++
        // 对象函数，读取 string 的长度
        str.length(); 
        // 读取 char * 字符串的长度
        strlen(str.c_str());
    ```

## 1.2 [计算某字母出现次数](https://www.nowcoder.com/practice/a35ce98431874e3a820dbe4b2d0508b1?tpId=37&tags=&title=&difficulty=0&judgeStatus=0&rp=1)

- 获取一个字符：
    ```c++
        // c++ 标准输入
        char ch;
        cin >> ch;
        // 从标准流读取: 以无符号 char 强制转换为 int 的形式返回，并把位置标识符往前移动。
        ch = fgetc(stdin);
    ```
- `char` 可以通过ASCII码进行数学运算，大小比较

    ```c++
        if(letter <= 'Z' && letter >= 'A' ){
            return letter + 'a' - 'A';
        }
    ```
- 典型ASCII顺序：**数字 < 大写字母 < 下划线 < 小写字母**
- `char* a; char b[];`: **a可以被二次修改，b不能。**

## 1.3 [明明的随机数](https://www.nowcoder.com/practice/3245215fffb84b7b81285493eae92ff0?tpId=37&tags=&title=&difficulty=0&judgeStatus=0&rp=0)

- 循环读取数字，回车退出：
    ```c++
        int a;
        while (cin >> a) {

        } 
    ```
- 字符转数字：
    ```c++
        #include <stdlib.h>
        int atoi(const char *);
        double atof(const char *);
    ```
- 数字转字符串：
    ```c++
        int sprintf(char *str, const char *format, ...); 
    ```