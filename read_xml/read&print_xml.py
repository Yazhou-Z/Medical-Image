# https://blog.csdn.net/hju22/article/details/85111071

from xml.dom import minidom
dom = minidom.parse("catROIs_00014.xml") #打开xml

def getInfo(node):
    names = dom.getElementsByTagName(node)
    data = names[0].firstChild.data
    #l = len(data)
    #print(data, l)
    data = data[1:-2].split(';')    # delete "[" and "]"
    l = len(data)
    print(data, l)
    # for ii in range(l): print(data[ii])

# 打印各脑区id与四个特征
informations = ['ids', 'depth', 'fractaldimension', 'gyrification', 'thickness']
for node in informations:
    print(node, ': ')
    getInfo(node)

# 打印各脑区名称
names = dom.getElementsByTagName('item')
for i in range(len(names)): print(names[i].firstChild.data)