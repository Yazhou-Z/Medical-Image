from xml.dom import minidom
from pandas import DataFrame
dom = minidom.parse("catROIs_00014.xml") #打开xml

def getInfo(node):
    names = dom.getElementsByTagName(node)
    data = names[0].firstChild.data
    #l = len(data)
    #print(data, l)
    data = data[1:-2].split(';')    # delete "[" and "]"
    l = len(data)
    print(l)
    return data
    # for ii in range(l): print(data[ii])

excel ={}

# 打印各脑区id与四个特征
informations = ['ids', 'depth', 'fractaldimension', 'gyrification', 'thickness']
for node in informations:
    print(node, ': ')
    excel[node] = getInfo(node)

# 打印各脑区名称
names = dom.getElementsByTagName('item')
name = []
for i in range(len(names)-1): name.append(names[i].firstChild.data)
print(name, len(names))

excel['name'] = name
print(excel)
df = DataFrame(excel)
df.to_excel('test.xlsx')