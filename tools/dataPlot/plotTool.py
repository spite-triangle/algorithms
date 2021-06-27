import tkinter as tk
from tkinter import font
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import pandas as pd
import os
import sys
import json
import re
import matplotlib.pyplot as plt

class Application(tk.Frame):
    """
    应用GUI程序
    """
    def __init__(self,master:tk.Misc,blockSize: int,configFilePath:str,configs:dict):
        super().__init__(master)
        master.update()
        self.master = master
        self.blockSize = blockSize
        self.pack()
        self.figures = []
        self.isSaveFig = False
        self.baseDir = os.path.dirname(__file__)
        # 配置文件
        self.configFilePath = self.baseDir + configFilePath
        self.fileConfigs = configs

        # 背景颜色
        self.fileFramebg = '#009688'
        self.plotFramebg = '#FFFFFF'
        self.btnbg = '#00BCD4'
        self.btnfg = '#FFFFFF'
        self.fileLabfg = '#FFFFFF'
        self.plotLabfg = '#000000'
        self.plotEntrybg = '#BDBDBD'
        self.btnActivebg = '#00796B'

        self.btnFont = ('微软雅黑',11,'bold')
        self.labFont = ('微软雅黑',11,'bold')
        self.entryFont = ('微软雅黑',10,'bold')
        # 生成控件
        self.creatWidgets()
        self.initWidget()

        pass
    
    def __del__(self):
        # # ensure_ascii：是否只使用ascii编码；indent：指定值后，输出文本更容易读
        # json.dump(self.fileConfigs,self.configFile,ensure_ascii=False,indent=4)
        # self.configFile.close()
        pass

    def creatWidgets(self):
        """
        定义控件
        """
        # 读取文件区域
        self.fileFrame = tk.Frame(self,background=self.fileFramebg,width=self.getPix(17),height=self.getPix(9)).pack()

        # 文件列表区
        self.fileList = tk.Listbox(self.fileFrame,font=self.entryFont,fg="#757575")
        self.setPosScale(self.fileList,1,1,4,6)
        self.removeFileBtn = tk.Button(self.fileFrame,text="删除",command=self.removeFile,background=self.btnbg,bd=0,fg=self.btnfg,font=self.btnFont,activebackground=self.btnActivebg)
        self.setPosScale(self.removeFileBtn,1,7,2,1)
        self.addFileBtn = tk.Button(self.fileFrame,text="添加",command=self.addFile,background="#05d4ef",bd=0,fg=self.btnfg,font=self.btnFont,activebackground=self.btnActivebg)
        self.setPosScale(self.addFileBtn,3,7,2,1)

        # 文件读取设置区
        self.filePathLab = tk.Label(self.fileFrame,text="文件路径:",background=self.fileFramebg,font=self.labFont,fg=self.fileLabfg)
        self.setPosScale(self.filePathLab,6,1,2,1)
        self.fileColumnsLab = tk.Label(self.fileFrame,text="数据名称:",background=self.fileFramebg,font=self.labFont,fg=self.fileLabfg)
        self.setPosScale(self.fileColumnsLab,6,6,2,1)
        self.fileSepLab = tk.Label(self.fileFrame,text="分割符号:",background=self.fileFramebg,font=self.labFont,fg=self.fileLabfg)
        self.setPosScale(self.fileSepLab,14,6,2,1)
        self.filePathEntry = tk.Entry(self.fileFrame,font=self.entryFont)
        self.setPosScale(self.filePathEntry,6,2,7,1)
        self.fileColumnsEntry = tk.Entry(self.fileFrame,font=self.entryFont)
        self.setPosScale(self.fileColumnsEntry,6,7,7,1)
        self.fileSepEntry = tk.Entry(self.fileFrame,font=self.entryFont)
        self.setPosScale(self.fileSepEntry,14,7,2,1)
        self.filePathBtn = tk.Button(self.fileFrame,text="浏览",command=self.getFilePath,background=self.btnbg,bd=0,fg=self.btnfg,font=self.btnFont,activebackground=self.btnActivebg)
        self.setPosScale(self.filePathBtn,14,2,2,1)
        self.dataIsShow = tk.BooleanVar()
        self.dataShow = tk.Radiobutton(self.fileFrame,text="显示",variable=self.dataIsShow,value=True,background=self.fileFramebg,font=self.labFont,fg=self.fileLabfg,activebackground=self.fileFramebg,selectcolor="#006359")
        self.setPosScale(self.dataShow,6,4,2,2)
        self.dataHidden = tk.Radiobutton(self.fileFrame,text="隐藏",variable=self.dataIsShow,value=False,background=self.fileFramebg,font=self.labFont,fg=self.fileLabfg,activebackground=self.fileFramebg,selectcolor="#006359")
        self.setPosScale(self.dataHidden,11,4,2,2)

        # # 绘图区域
        self.plotFrame = tk.Frame(self,background=self.plotFramebg,height=self.getPix(5),width=self.getPix(17)).pack()
        self.xLab = tk.Label(self.plotFrame,text="x轴:",background=self.plotFramebg,font=self.labFont,fg=self.plotLabfg)
        self.setPosScale(self.xLab,2,12,1,1)
        self.yLab = tk.Label(self.plotFrame,text="y轴:",background=self.plotFramebg,font=self.labFont,fg=self.plotLabfg)
        self.setPosScale(self.yLab,2,10,1,1)
        self.xEntry = tk.Entry(self.plotFrame,bg=self.plotEntrybg,fg='#212121',font=self.entryFont)
        self.setPosScale(self.xEntry,3,12,2,1)
        self.yEntry = tk.Entry(self.fileFrame,bg=self.plotEntrybg,fg='#212121',font=self.entryFont) 
        self.setPosScale(self.yEntry,3,10,12,1)
        self.saveFigBtn = tk.Button(self.plotFrame,text="保存",command=self.saveFigures,background=self.btnbg,bd=0,fg=self.btnfg,font=self.btnFont,activebackground=self.btnActivebg)
        self.setPosScale(self.saveFigBtn,10,12,2,1)
        self.closeFigBtn = tk.Button(self.plotFrame,text="关闭",command=self.closeFigures,background=self.btnbg,bd=0,fg=self.btnfg,font=self.btnFont,activebackground=self.btnActivebg)
        self.setPosScale(self.closeFigBtn,7,12,2,1)
        self.plotBtn = tk.Button(self.plotFrame,text="绘图",command=self.plotFigures,background=self.btnbg,bd=0,fg=self.btnfg,font=self.btnFont,activebackground=self.btnActivebg)
        self.setPosScale(self.plotBtn,13,12,2,1)
        pass

    def initWidget(self):
        """
        初始化控件
        """
        if os.path.getsize(self.configFilePath):
            # 读取配置文件

            # 初始化listbox
            for name in self.fileConfigs.keys():
                if "filePath" in self.fileConfigs[name]:
                    self.addConfig(self.fileConfigs[name])

            # 初始化x,y
            if 'xAxis' in self.fileConfigs or 'yAxis' in self.fileConfigs:
                if not self.fileConfigs['xAxis'] == None:
                    self.xEntry.insert(0,self.fileConfigs['xAxis'])
                if not self.fileConfigs['yAxis'] == []:
                    self.yEntry.insert(0,self.fileConfigs['yAxis'])

        else:
            self.fileConfigs = {}

        # 事件绑定
        self.fileList.bind('<<ListboxSelect>>',self.listBoxSelected)

    def saveFigures(self):
        """
        图像保存
        """
        if self.isSaveFig == True:
            messagebox.showinfo("info","已经关闭图像保存，请 [ 绘图 ]")
            self.plotBtn.config(text="绘图")
            self.isSaveFig = False
        else:
            messagebox.showinfo("info","已经打开图像保存，请 [ 生成 ]")
            self.plotBtn.config(text="生成")
            self.isSaveFig = True

    def closeFigures(self):
        """
        关闭图像
        """
        if self.figures == []:
            return
        for value in self.figures:
            plt.close(value)

            
    def plotFigures(self):
        """
        绘图
        """
        yAxis = re.split('[,， ]',str(self.yEntry.get()).strip())
        xAxis = str(self.xEntry.get()).strip()
        self.figures.clear()

        # 读取数据
        datas = []
        names = []
        for fileName in self.fileConfigs:
            if fileName == 'yAxis' or fileName == 'xAxis':
                continue 

            fileConfig = self.fileConfigs[fileName]

            if(not fileConfig["dataIsShow"]):
                continue

            data = pd.read_csv(fileConfig["filePath"],sep=fileConfig["fileSep"],header=None,engine='python')
            data.columns = fileConfig["fileColumns"]

            names.append(fileName)
            datas.append(data)
        
        # 绘图
        for col in yAxis:
            self.figures.append(plt.figure(col)) 
            plt.title("Fig" + xAxis + "_" + col)
            plt.xlabel(xAxis)
            plt.ylabel(col)
            plt.grid(linestyle='-.')
            for data in datas:
                plt.plot(data[xAxis],data[col])
            plt.legend(names)
            if self.isSaveFig:
                plt.savefig(self.baseDir + "/image/"+"Fig" + xAxis + "_" + col+".jpg")
 
  
        # 存储配置
        self.fileConfigs['yAxis'] = yAxis
        self.fileConfigs['xAxis'] = xAxis

    def listBoxSelected(self,even):
        """
        listbox 选中事件
        """
        if self.fileList.curselection() == ():
            return
        # 获取配置
        fileConfig = self.fileConfigs[self.fileList.get(self.fileList.curselection())]
        # 清空
        self.filePathEntry.delete(0,'end')
        self.fileColumnsEntry.delete(0,'end')
        self.fileSepEntry.delete(0,'end')
        # 填写内容
        self.filePathEntry.insert(0,fileConfig['filePath'])
        self.fileSepEntry.insert(0,fileConfig['fileSep'])
        self.fileColumnsEntry.insert(0,fileConfig['fileColumns'])
        # 选择框
        if(fileConfig["dataIsShow"]):
            self.dataShow.select()
            self.dataIsShow.set(True)
        else:
            self.dataHidden.select()
            self.dataIsShow.set(False)

    def removeFile(self):
        """
        删除配置文件
        """
        # 判断是否有东西被选中
        if not self.fileList.curselection() == ():
            fileName = self.fileList.get(self.fileList.curselection())
            self.fileList.delete('active')
            self.fileConfigs.pop(fileName)


    def addFile(self):
        """
        添加文件配置
        """
        # 一个文件的配置
        fileConfig = {}
        fileConfig["filePath"] = self.filePathEntry.get().strip()
        fileConfig["fileColumns"] = re.split('[,， ]',str(self.fileColumnsEntry.get().strip()))
        fileConfig["fileSep"] = self.fileSepEntry.get().strip()
        fileConfig["dataIsShow"] = self.dataIsShow.get()
        
        self.addConfig(fileConfig)
    
    def getFilePath(self):
        """
        加载文件路径
        """
        filePath = filedialog.askopenfilename(filetypes=(('text','.txt'),('csv','.csv'),('dat','.dat'),("All files", "*.*")))
        self.filePathEntry.delete(0,"end")
        self.filePathEntry.insert(0,filePath)


    def addConfig(self,fileConfig:dict) -> bool:
        """
        监测配置是否正确
        """
        fileName = os.path.split(fileConfig["filePath"])[1]

        if(not fileConfig["dataIsShow"]):
            # 是否已经记录了该文件
            if not fileName in self.fileList.get(0,'end'):
                self.fileList.insert('end',fileName)
            # 储存文件配置
            self.fileConfigs[fileName] = fileConfig
            return True

        # 检验信息是否正确
        try:
            data = pd.read_csv(fileConfig["filePath"],sep=fileConfig["fileSep"],header=None,engine='python')
            data.columns = fileConfig["fileColumns"]
        except IOError as e:
            messagebox.showerror("Error",str(e))
            return False
        except ValueError as e:
            messagebox.showerror("Error",str(e))
            return False
        else:
            # 是否已经记录了该文件
            if not fileName in self.fileList.get(0,'end'):
                self.fileList.insert('end',fileName)
            # 储存文件配置
            self.fileConfigs[fileName] = fileConfig
            return True

    def getPix(self,size:int) -> int:
        return size * self.blockSize

    def setPosScale(self,widget,x:int,y:int,width:int,height:int,anchor:str=None):
        widget.place(x=self.getPix(x),y=self.getPix(y),width=self.getPix(width),height=self.getPix(height),anchor=anchor)


if(__name__ == "__main__"): 
    
    blockSize = 30
    
    plt.ion()

    # 加载配置文件
    configPath = "./config/filesConfig.json"
    configFile = open(os.path.dirname(__file__) + configPath,'r',encoding="utf-8")
    fileConfigs = json.load(configFile)
    configFile.close()

    root = tk.Tk()
    root.title("plot tool")
    print(os.path.dirname(__file__))
    root.geometry(str(blockSize*17) + "x" + str(blockSize*14) + "+512+128")
    app = Application(root,blockSize,configPath,fileConfigs)
    root.mainloop()

    # 配置文件的写出
    configFile = open(os.path.dirname(__file__) + configPath,'w',encoding="utf-8")
    # ensure_ascii：是否只使用ascii编码；indent：指定值后，输出文本更容易读
    json.dump(fileConfigs,configFile,ensure_ascii=False,indent=4)
    configFile.close()
