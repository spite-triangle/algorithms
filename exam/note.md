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
    &emsp;`char* str` **会被修改**。<span style="color:red;font-weight:bold"> 分隔符会被完全屏蔽掉，连续重复的当作一个。 </span>
    ```c++
        #include <string.h>

        vector<string> split(char * str,const char * sep){
            vector<string> strs;
        
            char * buffer;
        
            buffer = strtok(str,sep);

            // 拆分完毕，buffer 就为 NULL
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

        while(scanf("%d %d",&a, &b) != EOF) {//注意while处理多个case
            
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

## 1.4 [进制转换](https://www.nowcoder.com/practice/8f3df50d2b9043208c5eed283d1d4da6?tpId=37&tqId=21227&rp=1&ru=%2Fta%2Fhuawei%2F&qru=%2Fta%2Fhuawei%2Fquestion-ranking)

- `strtol(const char* str,char **,int base);`: 将**二进制，八进制，十六进制格式字符串** 转为 **十进程整数**。
  - `str` : **跳过前面的空白字符，遇上数字或正负符号才开始做转换，再遇到非数字或字符串结束时(’\0’)结束转换。**
  - `endptr`: 可用来循环解析
  - `base` : **解析的进制类型**
  - **循环解析的字符串末尾不能有空白符**，<span style="color:red;font-weight:bold"> 但是靠 `cin >> ` 获取的字符串会过滤掉行首，行尾的空白符。行尾的空白留在缓冲区，行首的被彻底清除掉。 </span>

```c++
    #include <stdlib.h>

    // 字符格式，非字符格式都能解析 
    const char* str = "1723 111 0xff";

    // 用于接收解析一段后的位置
    char* endptr;

    // 解析第一个
    strtol(str,&endptr,16);

    // 循环解析
    while ( strlen(endptr) != 0 )
    {
        cout << "fuck: "<<strtol(endptr,&endptr,16) << endl;
    }
```

- `stoi()` 与 `atoi()`:
  -  `stoi()` 可以识别 `string`
  -  `stoi()` 会做范围检查
  -  `stoi()`也能进行进制转换，**循环解析，不好控制**。
```c++
    #include <string>
    string st = "  ff 0xff1";
    size_t p;
    cout << stoi(st,&p,16) << endl;
    cout << stoi(st.substr(p),&p,16) << endl;
```

## 1.5 [ 句子逆序](https://www.nowcoder.com/practice/48b3cb4e3c694d9da5526e6255bb73c3?tpId=37&tags=&title=&difficulty=0&judgeStatus=0&rp=1)

- `cin >> ` <span style="color:red;font-weight:bold"> 遇到空格，回车，tab就直接停止从缓冲区内读取。 </span>
- **可以利用 `cin >> ` 对 空格、回车、tab 间隔的字符串进行循环读取。**

```c++
    // 输入： ab b c d
    string str;
    while(cin >> str) {
        
    }
```

## 1.6 [密码验证合格程序](https://www.nowcoder.com/practice/184edec193864f0985ad2684fbc86841?tpId=37&&tqId=21243&rp=1&ru=/ta/huawei&qru=/ta/huawei/question-ranking)

- **使用正则查询重复字符**
    - `\\w`: 特殊字符最好写双斜杠
    - `\\1`: 重复1号捕获组捕获到的内容
    
```c++
    #include <regex>

    regex checkPattern("([\\w]{3}).*\\1");
```

--- 
# 二、数学

## 2.1 [ 质数因子](https://www.nowcoder.com/practice/196534628ca6490ebce2e336b47b3607?tpId=37&tags=&title=&difficulty=0&judgeStatus=0&rp=1)

```c++
    // 待分解的数
    int value;
    int temp = value;

    // 需要搜寻的最大质数就到 sqrt(value)
    for(int i=2; i <= temp && i <= sqrt(value);i++){
        // 同一个数，重复拆
        while(temp % i == 0){
            cout << "质因数：" << i;
            temp /= i;
        }
    }

    // 最后一次是否被分解
    if(temp != 1){
        cout << "质因数：" << temp;
    }
```

## 2.2 [近似值](https://www.nowcoder.com/practice/3ab09737afb645cc82c35d56a5ce802a?tpId=37&tags=&title=&difficulty=0&judgeStatus=0&rp=1)

```c++
    #include <math.h>
    // 近似值
    double round(double x);
```