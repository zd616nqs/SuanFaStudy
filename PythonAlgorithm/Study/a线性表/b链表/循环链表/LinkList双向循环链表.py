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


class LinkList双向循环链表(AbstractList, Generic[E]):

    def __init__(self) -> None:
        # 元素数量（初始0）
        self.__nodeCount: int = 0
        # 链表首个节点(置空)
        self.__firstNode: Node = None
        # 链表末尾节点(置空)
        self.__lastNode: Node = None
        # 活动指针，解决约瑟夫问题使用
        self.__currentNode: Node = None
        # 找不到元素
        self.__ELEMENT_NOT_FOUND = -1

    def clear(self): pass
    def contains(self, *, element: E) -> bool: pass
    def getElementAtIndex(self, *, index: int) -> E: pass
    def setElementAtIndex(self, *, index: int, element: E): pass
    def removeElementAtIndex(self, index: int): pass
    def indexOfElement(self, element: E) -> int: pass

    def isEmpty(self) -> bool:
        # 是否为空
        return (self.__nodeCount == 0)

    def addElementToTail(self, *, element: E):
        # 添加一个元素到末尾
        self.insertElementAtIndex(element=element, index=self.__nodeCount)

    def insertElementAtIndex(self, *, index: int, element: E):
        # 在index位置插入一个元素
        self.__rangeCheckForAdd(index)

        if self.__nodeCount == 0:
            # 添加链表的第一个元素
            insertNode = Node(element=element, prev=None, next=None)
            self.__firstNode = insertNode
            self.__lastNode = insertNode
        else:
            if index == self.__nodeCount:
                # 往链表的最后添加元素
                insertNode = Node(
                    element=element, prev=self.__lastNode, next=self.__firstNode)
                self.__lastNode.next = insertNode
                self.__firstNode.prev = insertNode
                self.__lastNode = insertNode
            elif index == 0:
                # 往链表的首个位置添加元素
                insertNode: Node = Node(
                    element=element, prev=self.__lastNode, next=self.__firstNode.next)
                self.__lastNode.next = insertNode
                self.__firstNode.next.prev = insertNode
                self.__firstNode = insertNode
            else:
                # 往链表的中间位置添加节点
                prevNode: Node = self.__getNodeAtIndex(index - 1)
                nextNode: Node = prevNode.next
                insertNode: Node = Node(
                    element=element, prev=prevNode, next=nextNode)
                prevNode.next = insertNode
                nextNode.prev = insertNode
        self.__nodeCount += 1

    # -----------约瑟夫问题-------------

    def reset(self):
        self.__currentNode = self.__firstNode

    def next(self) -> E:
        if self.__currentNode is None:
            return None
        else:
            self.__currentNode = self.__currentNode.next
            return self.__currentNode.element

    def remove(self) -> E:
        if self.__currentNode is None:
            return None

        nextNode: Node = self.__currentNode.next

        removeElement = self.__removeNode(self.__currentNode)
        if self.__nodeCount == 0:
            self.__currentNode = None
        else:
            self.__currentNode = nextNode

        return removeElement

    # -----------私有方法-------------

    def __removeNode(self, node: Node) -> E:
        if self.__nodeCount == 1:
            # -------链表只有1个元素------
            self.__firstNode = None
            self.__lastNode = None
        else:
            prevNode: Node = node.prev
            nextNode: Node = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            if (node == self.__firstNode):
                self.__firstNode = nextNode

            if node == self.__lastNode:
                self.__lastNode = prevNode
        self.__nodeCount -= 1
        return node.element

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

        string: str = "节点数量:" + str(self.__nodeCount) + ",  ["
        tempNode: Node = self.__firstNode
        for i in range(self.__nodeCount):
            string = string + f"{tempNode}"
            if i != 0:
                string = string + ","
            tempNode = tempNode.next

        return string + "]"
