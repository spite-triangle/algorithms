#ifndef __CONFIGUREINI_H__
#define __CONFIGUREINI_H__
#include <stdio.h>
#include <string.h>

#include <fstream>
#include <iostream>
#include <map>
#include <regex>
#include <vector>

#define DEBUG

using namespace std;
namespace mini {

// 节点的值与注释
class Node {
   public:
    Node(string value);
    Node(string value, string comment);
    string value;
    string comment;
};

// 一个单元
class Section {
   private:
   public:
    // 单元
    string name;
    // 一个单元下的全部节点
    map<string, Node *> nodes;

    Section(string name);
    ~Section();
    /*
     * 描述: 添加一个节点
     */
    void appendNode(string &key, string &value, string &comment);

    /*
     * 描述:  删除一个节点
     */
    void removeNode(string &key);
};

class OperatorINI {
   private:
    /*
     * 描述: 拆分字符串
     */
    std::vector<std::string> splitComment(const std::string &str,
                                          const std::string &pattern);

   public:
    ~OperatorINI();
    // 存储所有单元的列表
    map<string, Section *> sections;

    /*
     * 描述: 读取ini配置文件
     */
    void readINI(const char *path);

    /*
     * 描述: 写出ini配置文件
     */
    void writeINI(const char *path);

    /*
     * 描述: 获取值
     */
    string getValue(string section, string key);

    void setValue(string section, string key,string value);

    void setValue(string section, string key,float value);
    
    void setValue(string section, string key,int value);
    /*
     * 描述: 获取值
     */
    int getValueInt(string section, string key);

    /*
     * 描述: 获取值
     */
    float getValueFloat(string section, string key);

    /*
     * 描述: 获取注释
     */
    string getComment(string section, string key);

    /*
     * 描述: 获取一个单元
     */
    Section *getSector(string section);

    /*
     * 描述: 删除节点
     */
    void removeNode(string section, string key);

    /*
     * 描述: 添加配置
     */
    void appendNode(string section, string key, string value);

    /*
     * 描述: 添加配置
     */
    void appendNode(string section, string key, string value, string comment);
};

}  // namespace mini

#endif  // __CONFIGUREINI_H__