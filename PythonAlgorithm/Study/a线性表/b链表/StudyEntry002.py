from Utils.NQS_Utils import Utils
from .单向链表.LinkList普通链表 import LinkList普通链表


class StudyEntry002(object):

    def __init__(self) -> None:
        pass

    @staticmethod
    def run(*, execute: bool):
        if (not execute):
            return
        # ---------------单向链表----------
        obj = StudyEntry002()

        # ---------------单向链表----------
        # 普通单向链表的实现
        obj.example1(isWork=False)
        # 动态扩容缩容单向链表
        obj.example2(isWork=True)

        # ---------------双向链表----------
        # 普通双向链表
        # example3(false)

        # ----------循环链表(单向+双向)------------
        # 单向循环链表
        # example4(false)
        # 双向循环链表
        # example5(false)

        # 解决约瑟夫问题:使用循环链表就能实现(单向和双向都可以)
        # example6(false)

    # --------------普通单向链表的实现---------------
    @Utils.func_cal_time
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
    
    # --------------动态扩容缩容单向链表---------------
    @Utils.func_cal_time
    def example2(self, *, isWork: bool):
        if (not isWork):
            return
        
        # # 强制校验子类是否实现抽象类定义的所有方法
        # Utils.check_implement(LinkList动态扩容缩容链表)
        # linkList = LinkList动态扩容缩容链表[int]()
        
        # for i in range(30):
        #     linkList.addElementToTail(element=i)
        #     print(f"{linkList.__eleCount}")
            
        # for i in range(20):
        #     linkList.removeElementAtIndex(index=0)
        #     print(f"{linkList.__eleCount}")
        