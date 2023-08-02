from Utils.NQS_Utils import Utils
from .单向链表.LinkList普通链表 import LinkList普通链表
from .双向链表.LinkList普通双向链表 import LinkList普通双向链表
from .循环链表.LinkList单向循环链表 import LinkList单向循环链表
from .循环链表.LinkList双向循环链表 import LinkList双向循环链表


class StudyEntry002(object):

    def __init__(self) -> None:
        pass

    @staticmethod
    @Utils.func_cal_time
    def run(*, execute: bool):
        if (not execute):
            return
        # ---------------单向链表----------
        obj = StudyEntry002()

        # ---------------单向链表----------
        # 普通单向链表的实现
        obj.example1(isWork=False)

        # ---------------双向链表----------
        obj.example2(isWork=False)

        # ----------循环链表(单向+双向)------------
        # 单向循环链表
        obj.example3(isWork=True)
        # 双向循环链表
        # 解决约瑟夫问题:使用循环链表就能实现(单向和双向都可以)
        obj.example4(isWork=True)
        
        
        
        
        
        print("")

    # --------------普通单向链表的实现---------------
    def example1(self, *, isWork: bool):
        if (not isWork):
            return

        # 强制校验子类是否实现抽象类定义的所有方法
        Utils.check_implement(LinkList普通链表)

        linkList = LinkList普通链表[int]()
        print(f"11111 {linkList}")
        linkList.addElementToTail(element=11)
        print(f"22222 {linkList}")
        linkList.addElementToTail(element=22)
        print(f"33333 {linkList}")
        linkList.insertElementAtIndex(index=0, element=33)
        print(f"44444 {linkList}")
        resultEle = linkList.getElementAtIndex(index=0)
        print(f"55555 {resultEle}")
        linkList.setElementAtIndex(index=0, element=66)
        print(f"66666 {linkList}")
        print(f"77777 {linkList.isEmpty()}")
        linkList.clear()
        print(f"88888 {linkList}")
        """ 
        11111 单向链表汇总：
                元素数量:0, 

        22222 单向链表汇总：
                元素数量:1, 
                index:0：11
        33333 单向链表汇总：
                元素数量:2, 
                index:0：11
                index:1：22
        44444 单向链表汇总：
                元素数量:3, 
                index:0：33
                index:1：11
                index:2：22
        55555 33
        66666 单向链表汇总：
                元素数量:3, 
                index:0：66
                index:1：11
                index:2：22
        77777 False
        88888 单向链表汇总：
                元素数量:0, 
                
                
                
                
        """

    # --------------普通双向链表的实现---------------
    def example2(self, *, isWork: bool):
        if (not isWork):
            return

        # 强制校验子类是否实现抽象类定义的所有方法
        Utils.check_implement(LinkList普通双向链表)

        linkList2 = LinkList普通双向链表[str]()
        print(f"11111 {linkList2}")
        linkList2.addElementToTail(element="牛")
        print(f"22222 {linkList2}")
        linkList2.addElementToTail(element="青")
        print(f"33333 {linkList2}")
        linkList2.insertElementAtIndex(index=0, element="山")
        print(f"44444 {linkList2}")
        resultEle = linkList2.getElementAtIndex(index=1)
        print(f"55511 {resultEle}")
        resultNode = linkList2.getNodeAtIndex(index=1)
        print(f"55522 {resultNode}")
        linkList2.setElementAtIndex(index=2, element="荔枝")
        print(f"66666 {linkList2}")
        print(f"77777 {linkList2.isEmpty()}")
        linkList2.clear()
        print(f"88888 {linkList2}")

        ''' 
        11111 双向链表汇总：
                元素数量:0, 

        22222 双向链表汇总：
                元素数量:1, 
                index:0：牛
        33333 双向链表汇总：
                元素数量:2, 
                index:0：牛
                index:1：青
        44444 双向链表汇总：
                元素数量:3, 
                index:0：山
                index:1：牛
                index:2：青
        55511 牛
        55522 (山)_牛_(青)
        66666 双向链表汇总：
                元素数量:3, 
                index:0：山
                index:1：牛
                index:2：荔枝
        77777 False
        88888 双向链表汇总：
                元素数量:0, 
                
                
                
        '''
    # --------------单向循环链表的实现---------------

    def example3(self, *, isWork: bool):
        if (not isWork):
            return

        # 强制校验子类是否实现抽象类定义的所有方法
        Utils.check_implement(LinkList单向循环链表)

        linkList3 = LinkList单向循环链表[str]()
        print(f"11111 {linkList3}")
        linkList3.insertElementAtIndex(index=0, element="牛")
        print(f"22222 {linkList3}")
        linkList3.insertElementAtIndex(index=1, element="青")
        print(f"33333 {linkList3}")
        linkList3.insertElementAtIndex(index=2, element="山")
        print(f"44444 {linkList3}")
        resultEle = linkList3.getElementAtIndex(index=1)
        print(f"55555 {resultEle}")
        linkList3.setElementAtIndex(index=2, element="哈")
        print(f"66666 {linkList3}")
        print(f"77777 {linkList3.isEmpty()}")

        print(f"{linkList3._LinkList单向循环链表__getNodeAtIndex(0)}")
        print(f"{linkList3._LinkList单向循环链表__getNodeAtIndex(1)}")
        print(f"{linkList3._LinkList单向循环链表__getNodeAtIndex(2)}")

        linkList3.clear()
        print(f"88888 {linkList3}")
        """ 
        11111 单向循环链表汇总：
        元素数量:0, 

        22222 单向循环链表汇总：
                元素数量:1, 
                index:0：牛
        33333 单向循环链表汇总：
                元素数量:2, 
                index:0：牛
                index:1：青
        44444 单向循环链表汇总：
                元素数量:3, 
                index:0：牛
                index:1：青
                index:2：山
        55555 青
        66666 单向循环链表汇总：
                元素数量:3, 
                index:0：牛
                index:1：青
                index:2：哈
        77777 False
        牛_(青)
        青_(哈)
        哈_(牛)
        88888 单向循环链表汇总：
                元素数量:0, 
                
                
        """

    # --------------双向循环链表的实现---------------
    def example4(self, *, isWork: bool):
        if (not isWork):
            return

        # 强制校验子类是否实现抽象类定义的所有方法
        Utils.check_implement(LinkList双向循环链表)

        linkList4 = LinkList双向循环链表[str]()
        linkList4.addElementToTail(element=11)
        linkList4.addElementToTail(element=22)
        linkList4.addElementToTail(element=33)
        linkList4.addElementToTail(element=44)
        linkList4.addElementToTail(element=55)
        linkList4.addElementToTail(element=66)
        linkList4.addElementToTail(element=77)
        linkList4.addElementToTail(element=88)
        linkList4.addElementToTail(element=99)
        print(f"{linkList4}\n\n")

        linkList4.reset()  # 指针复位到起始位置
        while (linkList4.isEmpty() is False):
            linkList4.next()
            linkList4.next()
            linkList4.remove()
            print(f"{linkList4}")
        '''
        节点数量:9,  [(99)_11_(22)(11)_22_(33),(22)_33_(44),(33)_44_(55),(44)_55_(66),(55)_66_(77),(66)_77_(88),(77)_88_(99),(88)_99_(11),]


        节点数量:8,  [(99)_11_(22)(11)_22_(44),(22)_44_(55),(44)_55_(66),(55)_66_(77),(66)_77_(88),(77)_88_(99),(88)_99_(11),]
        节点数量:7,  [(99)_11_(22)(11)_22_(44),(22)_44_(55),(44)_55_(77),(55)_77_(88),(77)_88_(99),(88)_99_(11),]
        节点数量:6,  [(88)_11_(22)(11)_22_(44),(22)_44_(55),(44)_55_(77),(55)_77_(88),(77)_88_(11),]
        节点数量:5,  [(88)_11_(22)(11)_22_(55),(22)_55_(77),(55)_77_(88),(77)_88_(11),]
        节点数量:4,  [(77)_11_(22)(11)_22_(55),(22)_55_(77),(55)_77_(11),]
        节点数量:3,  [(77)_11_(22)(11)_22_(77),(22)_77_(11),]
        节点数量:2,  [(77)_11_(77)(11)_77_(11),]
        节点数量:1,  [(11)_11_(11)]
        节点数量:0,  []
        '''
