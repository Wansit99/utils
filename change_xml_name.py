import os.path
import xml.dom.minidom

xmlFilePath = r"J:\BaiduNetdiskDownload\安全帽_有_无(1)"# 首先将xml文件放到指定的（模型训练时代码读取的地方）文件夹内
xmlFileNames = os.listdir(xmlFilePath)

def change1(joinXmlFilePath):
    # # xml文件读取操作
    dom = xml.dom.minidom.parse(joinXmlFilePath)
    root = dom.documentElement  # 获取xml文件文本，即根目录
    # getElementsByTagName:返回带有指定标签名的对象的集合。
    oriFileName = root.getElementsByTagName("name")
    for ofn in iter(oriFileName):
        fileName = ofn.firstChild.data

        print("原始class名:", fileName)
        # 修改后文件名
        newFileName = fileName.lower()
        ofn.firstChild.data = newFileName
        print("修改后class名:", newFileName)
    with open(joinXmlFilePath, "w") as pn:
        dom.writexml(pn)  # 打开拼接的目录下的文件夹，修改xml的文本文件内容
        print("finish")
def updatexmldxx():
    for xmlFileName in xmlFileNames:  # find xml
        if not os.path.isdir(xmlFileName):
            print(xmlFileName)  # 判断一下是否读取正确
            # xml文件读取操作
            joinXmlFilePath = os.path.join(xmlFilePath,xmlFileName)
            change1(joinXmlFilePath)


def change2(joinXmlFilePath):
    # # xml文件读取操作
    dom = xml.dom.minidom.parse(joinXmlFilePath)
    root = dom.documentElement  # 获取xml文件文本，即根目录
    # getElementsByTagName:返回带有指定标签名的对象的集合。
    oriFileName = root.getElementsByTagName("name")
    for ofn in iter(oriFileName):
        fileName = ofn.firstChild.data
        if fileName == "['Wear_helmet']":
            print("原始class名:", fileName)
            # 修改后文件名
            newFileName = "hat"
            ofn.firstChild.data = newFileName
            print("修改后class名:", newFileName)
        else:
            print("原始class名:", fileName)
            # 修改后文件名
            newFileName = "person"
            ofn.firstChild.data = newFileName
            print("修改后class名:", newFileName)
    with open(joinXmlFilePath, "w") as pn:
        dom.writexml(pn)  # 打开拼接的目录下的文件夹，修改xml的文本文件内容
        print("finish")

# 更新xml中某个类别
def updatexmlpeople2person():
    for xmlFileName in xmlFileNames:  # find xml
        if not os.path.isdir(xmlFileName):
            print(xmlFileName)  # 判断一下是否读取正确
            # xml文件读取操作
            joinXmlFilePath = os.path.join(xmlFilePath, xmlFileName)
            change2(joinXmlFilePath)


if __name__ == '__main__':
    updatexmlpeople2person()  # 将name为people的节点改为person
    # updatexmldxx()  # 统一xml中name的大小写
