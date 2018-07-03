#coding:utf-8
import pandas as pd
import os
import matplotlib.pyplot as plt
#当前目录
baseDir = os.path.dirname(os.path.abspath(__file__)).replace('\\','/') + '/'
os.chdir(baseDir)#更改当前工作目录
data = pd.read_table('train.txt',sep=' ',header=None).iloc[:,:-2]
try:
    num1 = raw_input('请输入样例编号(1-25):')
    num2 = raw_input('请输入数据列(3-26):')
except:
    num1 = input('请输入样例编号(1-25):')
    num2 = input('请输入数据列(3-26):')
#归一化类
class normaler():
    def __init__(self,dataInput):
        self.dataMin = dataInput.min()
        self.dataMax = dataInput.max()
    
    #0,1归一化函数
    def normal(self,dataInput):
        return (dataInput-self.dataMin)/(self.dataMax-self.dataMin)
#写入归一化文件
content=normaler(data).normal(data)
content.to_csv('归一化数据.csv',sep=' ')
print('归一化数据已保存...')
#处理样例编号和列索引
num1 = int(num1)
num2 = int(num2)-1
#获得对应数据
data2 = data[data[0]==num1].iloc[:,[1,num2]]
#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei'] 
#用来正常显示负号
plt.rcParams['axes.unicode_minus']=False 
#画板
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
x = data2.iloc[:,[0]]
y = data2.iloc[:,[1]]
ax1.plot(x,y,'ko--')
plt.show()