from xml.dom import minidom
from pandas import DataFrame
import os
from openpyxl import Workbook
 
def make_xlsx(path):
    wb = Workbook()
    wb.save(path)


def getInfo(node, dom):
    names = dom.getElementsByTagName(node)
    data = names[0].firstChild.data
    #l = len(data)
    #print(data, l)
    data = data[1:-2].split(';')    # delete "[" and "]"
    # l = len(data)
    # print(l)
    return data
    # for ii in range(l): print(data[ii])


def set_up_excel(filename):
    excel ={}
    dom = minidom.parse("label/" + filename + ".xml") #打开xml

    # 打印各脑区id与四个特征
    informations = ['ids', 
    # 'depth', 'fractaldimension', 'gyrification', 
    'thickness']
    for node in informations:
        print(node, ': ')
        excel[node] = getInfo(node, dom)

    # 打印各脑区名称
    names = dom.getElementsByTagName('item')
    name = []
    for i in range(152): name.append(names[i].firstChild.data)
    # print(name, len(names))

    excel['name'] = name
    print(len(excel['name']))
    df = DataFrame(excel)
    xlsx_path = filename + ".xlsx"
    make_xlsx(xlsx_path)
    df.to_excel(xlsx_path)

    return 0

for i in range(15, 27):
    s = "%05d" % i
    data = "catROIs_" + s
    set_up_excel(data)

