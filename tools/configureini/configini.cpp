#include "configini.h"

namespace mini
{

    Node::Node(string value)
    {
        this->value = value;
        this->comment = "";
    }

    Node::Node(string value, string comment)
    {
        this->comment = comment;
        this->value = value;
    }

    Section::Section(string name) { this->name = name; }

    Section::~Section()
    {
        if (nodes.size() > 0)
        {
            for (map<string, Node *>::iterator it = nodes.begin(); it != nodes.end();
                 it++)
            {
                if (it->second)
                {
                    delete it->second;
                }
            }
        }
    }
    OperatorINI::~OperatorINI()
    {
        if (sections.size() > 0)
        {
            for (map<string, Section *>::iterator it = sections.begin();
                 it != sections.end(); it++)
            {
                if (it->second)
                {
                    delete it->second;
                }
            }
        }
    }

    void Section::appendNode(string &key, string &value, string &comment)
    {
        Node *node = new Node(value, comment);
        this->nodes[key] = node;
    }

    void Section::removeNode(string &key)
    {
        delete this->nodes[key];
        this->nodes.erase(key);
    }

    std::vector<std::string> OperatorINI::splitComment(const std::string &str,
                                                       const std::string &pattern)
    {
        char *strc = new char[strlen(str.c_str()) + 1];
        strcpy(strc, str.c_str());
        std::vector<std::string> resultVec;

        // ; 前
        char *tmpStr = strtok(strc, pattern.c_str());
        resultVec.push_back(std::string(tmpStr));

        // ; 后
        tmpStr = strtok(NULL, pattern.c_str());
        resultVec.push_back(std::string(tmpStr));

        delete[] strc;

        return resultVec;
    }

    void OperatorINI::readINI(const char *path)
    {
        unsigned int index = 0;
        ifstream file;
        string line;
        // 当前的单元
        Section *sectionCurr = nullptr;
        smatch result;
        regex sectionPattern("^ *\\[ *(\\S*) *\\] *");
        regex keyValuePattern("^ *(\\S*) *= *(\\S*) *$");
        regex keyValComPattern("^ *(\\S*) *= *(\\S*) *; *(\\S.*) *$");

        // 打开文件
        file.open(path);

        // 解析文件
        while (file)
        {
            // 读取一行
            getline(file, line);
            index++;

            // 解析单元
            if (regex_search(line, result, sectionPattern))
            {
                sectionCurr = new Section(result.str(1));
                this->sections[result.str(1)] = sectionCurr;
                continue;
            }

            if (sectionCurr == nullptr)
            {
                continue;
            }
            
            // 解析key,value
            if (regex_search(line, result, keyValuePattern))
            {
                if (result.str(2).empty() || result.str(1).empty())
                {
#ifdef DEBUG
                    fprintf(stderr,
                            "error: section [%s] on index %d exception !!\n",
                            sectionCurr->name.c_str(), index);
#endif
                    continue;
                }
                sectionCurr->nodes[result.str(1)] = new Node(result.str(2));
            }
            // 解析key,value,comment
            else if (regex_search(line, result, keyValComPattern))
            {
                if (result.str(2).empty() || result.str(1).empty())
                {
#ifdef DEBUG
                    fprintf(stderr,
                            "error: section [%s] on index %d exception !!\n",
                            sectionCurr->name.c_str(), index);
#endif
                    continue;
                }
                sectionCurr->nodes[result.str(1)] =
                    new Node(result.str(2), result.str(3));
            }
        }
        file.close();
    }

    void OperatorINI::writeINI(const char *path)
    {
        Section *section;
        // 打开文件
        ofstream file(path);
        for (map<string, Section *>::iterator itSection = sections.begin();
             itSection != sections.end(); itSection++)
        {
            // 写单元
            file << "[ " << itSection->first << " ]" << endl;
            section = itSection->second;
            for (map<string, Node *>::iterator itNode = section->nodes.begin();
                 itNode != section->nodes.end(); itNode++)
            {
                if (itNode->second->comment.empty())
                {
                    file << itNode->first << " = " << itNode->second->value << endl;
                }
                else
                {
                    file << itNode->first << " = " << itNode->second->value
                         << "    ;" << itNode->second->comment << endl;
                }
            }
            file << endl;
        }
        file.close();
    }

    string OperatorINI::getValue(string section, string key)
    {
#ifdef DEBUG
        if (this->sections.count(section) == 0)
        {
            fprintf(stderr, "get error: not define section [%s]\n",
                    section.c_str());
        }
        if (this->sections.at(section)->nodes.count(key) == 0)
        {
            fprintf(stderr, "get error: not define sejction [%s] node key %s \n",
                    section.c_str(), key.c_str());
        }
#endif

        return this->sections.at(section)->nodes.at(key)->value;
    }
    
    void OperatorINI::setValue(string section, string key,string value) 
    {
        this->sections[section]->nodes[key]->value = value;
    }
    
    void OperatorINI::setValue(string section, string key,float value) 
    {
        this->sections[section]->nodes[key]->value = to_string(value);
    }
    
    void OperatorINI::setValue(string section, string key,int value) 
    {
        this->sections[section]->nodes[key]->value = to_string(value);
    }
    
    int OperatorINI::getValueInt(string section, string key) 
    {
#ifdef DEBUG
        if (this->sections.count(section) == 0)
        {
            fprintf(stderr, "get error: not define section [%s]\n",
                    section.c_str());
        }
        if (this->sections.at(section)->nodes.count(key) == 0)
        {
            fprintf(stderr, "get error: not define sejction [%s] node key %s \n",
                    section.c_str(), key.c_str());
        }
#endif

        return atoi(this->sections.at(section)->nodes.at(key)->value.c_str());
    }
    
    float OperatorINI::getValueFloat(string section, string key) 
    {
#ifdef DEBUG
        if (this->sections.count(section) == 0)
        {
            fprintf(stderr, "get error: not define section [%s]\n",
                    section.c_str());
        }
        if (this->sections.at(section)->nodes.count(key) == 0)
        {
            fprintf(stderr, "get error: not define sejction [%s] node key %s \n",
                    section.c_str(), key.c_str());
        }
#endif

        return atof(this->sections.at(section)->nodes.at(key)->value.c_str());
    }

    string OperatorINI::getComment(string section, string key)
    {
#ifdef DEBUG
        if (this->sections.count(section) == 0)
        {
            fprintf(stderr, "get error: not define section [%s]\n",
                    section.c_str());
        }
        if (this->sections.at(section)->nodes.count(key) == 0)
        {
            fprintf(stderr, "get error: not define section [%s] node key %s \n",
                    section.c_str(), key.c_str());
        }
#endif
        return this->sections.at(section)->nodes.at(key)->comment;
    }

    Section *OperatorINI::getSector(string section)
    {
#ifdef DEBUG
        if (this->sections.count(section) == 0)
        {
            fprintf(stderr, "get error: not define section [%s]\n",
                    section.c_str());
        }
#endif
        return this->sections.at(section);
    }

    void OperatorINI::removeNode(string section, string key)
    {
#ifdef DEBUG
        if (this->sections.count(section) == 0)
        {
            fprintf(stderr, "remove error: not define section [%s]\n",
                    section.c_str());
        }
        if (this->sections.at(section)->nodes.count(key) == 0)
        {
            fprintf(stderr, "remove error: not define section [%s] node key %s \n",
                    section.c_str(), key.c_str());
        }
#endif
        this->sections.at(section)->removeNode(key);
    }

    void OperatorINI::appendNode(string section, string key, string value)
    {
        string comment = "";
        if (this->sections.count(section) == 0)
        {
            this->sections[section] = new Section(section);
        }
        this->sections[section]->appendNode(key, value, comment);
    }

    void OperatorINI::appendNode(string section, string key, string value,
                                 string comment)
    {
        if (this->sections.count(section) == 0)
        {
            this->sections[section] = new Section(section);
        }

        this->sections[section]->appendNode(key, value, comment);
    }

} // namespace mini