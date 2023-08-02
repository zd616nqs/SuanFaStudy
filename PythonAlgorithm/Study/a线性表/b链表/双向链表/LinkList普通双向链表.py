from ..common.AbstractList import AbstractList
from typing import Generic, TypeVar
E = TypeVar('E')


class Node(Generic[E]):
    def __init__(self, element: E, prev, next):
        self.prev: Node = prev
        self.element = element
        self.next: Node = next

    # 打印当前node的前后关系
    def __str__(self) -> str:
        nodeStr: str = ""
        # 拼接上个node
        if self.prev is None:
            nodeStr = nodeStr + "(null)"
        else:
            nodeStr = nodeStr + f"({self.prev.element})"
        # 拼接当前node
        nodeStr = nodeStr + "_" + f"{self.element}" + "_"
        # 拼接下个node
        if self.next is None:
            nodeStr = nodeStr + "(null)"
        else:
            nodeStr = nodeStr + f"({self.next.element})"
        return nodeStr


class LinkList普通双向链表(AbstractList, Generic[E]):

    def __init__(self) -> None:
        # 元素数量（初始0）
        self.__nodeCount: int = 0
        # 链表首个节点(置空)
        self.__firstNode: Node = None
        # 链表末尾节点(置空)
        self.__lastNode: Node = None
        # 找不到元素
        self.__ELEMENT_NOT_FOUND = -1

    def clear(self):
        # 清除所有元素
        self.__nodeCount = 0
        self.__firstNode = None
        self.__lastNode = None

    def isEmpty(self) -> bool:
        # 是否为空
        return (self.__nodeCount == 0)

    def contains(self, *, element: E) -> bool:
        # 是否包含某个元素
        return self.indexOfElement(element=element) is not self.__ELEMENT_NOT_FOUND

    def getElementAtIndex(self, *, index: int) -> E:
        self.__rangeCheck(index)
        # 获取index位置的元素

        resultNode: Node = self.__getNodeAtIndex(index)
        return resultNode.element
    
    def getNodeAtIndex(self, *, index: int) -> Node:
        self.__rangeCheck(index)
        # 获取index位置的元素

        resultNode: Node = self.__getNodeAtIndex(index)
        return resultNode

    def setElementAtIndex(self, *, index: int, element: E):
        # 设置index位置的元素
        self.__rangeCheck(index)

        resultNode: Node = self.__getNodeAtIndex(index)
        resultNode.element = element

    def addElementToTail(self, *, element: E):
        # 添加元素到最后
        if self.__nodeCount == 0:
            # 创建第一个节点，next指向None
            self.__firstNode = Node(element, self.__firstNode, self.__lastNode)
            self.__lastNode = self.__firstNode
        else:
            # 正常往链表后面加node
            origin_last_node = self.__lastNode
            new_end_node = Node(element, origin_last_node.prev, None)
            origin_last_node.next = new_end_node
            self.__lastNode = new_end_node

        self.__nodeCount += 1

    def insertElementAtIndex(self, *, index: int, element: E):
        # 在index位置插入一个元素
        self.__rangeCheckForAdd(index)

        nextNode: Node = self.__getNodeAtIndex(index)
        prevNode: Node = nextNode.prev
        insertNode: Node = Node(element=element, prev=prevNode, next=nextNode)

        if prevNode is None:
            self.__firstNode = insertNode
        else:
            prevNode.next = insertNode

        if nextNode is None:
            self.__lastNode = insertNode
        else:
            nextNode.prev = insertNode

        self.__nodeCount += 1


    def removeElementAtIndex(self, *, index: int):
        # 删除一个位置的元素
        # 思路：跨过中间的node，头尾的两个node进行引用，中间的node没有引用就销毁了
        self.__rangeCheck(index)

        curNode: Node = self.__getNodeAtIndex(index)
        prevNode: Node = curNode.prev
        nextNode: Node = curNode.next

        # ------处理next节点-----
        if prevNode is None:
            self.__firstNode = nextNode
        else:
            prevNode.next = nextNode

        # -----处理prev节点-----
        if nextNode is None:
            self.__lastNode = prevNode
        else:
            nextNode.prev = prevNode

        self.__nodeCount -= 1

    def indexOfElement(self, *, element: E) -> int:
        # 查看元素的索引
        if (element is None):
            # 匹配element为None的情况
            curNode: Node = self.__firstNode
            for i in range(self.__nodeCount):
                if curNode.element is None:
                    return i
                curNode = curNode.next
        else:
            # 匹配element有值的情况
            curNode: Node = self.__firstNode
            for i in range(self.__nodeCount):
                if (isinstance(element, E)
                        and isinstance(curNode.element, E)
                        and str(element) == str(curNode.element)):
                    return i
                # 没有匹配到，就继续找下个节点
                curNode = curNode.next
        return self.__ELEMENT_NOT_FOUND

    # -----------私有方法-------------

    def __getNodeAtIndex(self, index: int) -> Node:
        # 获取index位置对应的节点对象
        self.__rangeCheck(index)

        if index < self.__nodeCount/2:
            # 从前往后找链表快
            curNode: Node = self.__firstNode
            for temp in range(index):
                curNode = curNode.next
            return curNode
        else:
            # 从后往前找链表快
            curNode: Node = self.__lastNode
            for temp in range(self.__nodeCount-1-index):
                curNode = curNode.prev
        return curNode

    def __outOfBounds(self, index: int):
        # 超出index，抛出错误
        raise IndexError(f"下标越界：Index: {index}, nodeCount: {self.__nodeCount}")

    def __rangeCheck(self, index: int):
        # 检查index是否超出范围
        if index < 0 or index >= self.__nodeCount:
            self.__outOfBounds(index)

    def __rangeCheckForAdd(self, index: int):
        # 监测index是否越界
        if index < 0 or index > self.__nodeCount:
            self.__out_of_bounds(index)

    def __str__(self) -> str:
        # print打印链表结构
        string = ["双向链表汇总：\n\t元素数量:" + str(self.__nodeCount) + ", \n\t"]
        for i in range(self.__nodeCount):
            if i != 0:
                string.append("\n\t")
            string.append(f"index:{i}："+str(self.__getNodeAtIndex(i).element))
        return "".join(string)
