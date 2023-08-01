from ..common.AbstractList import AbstractList
from typing import Generic, TypeVar
E = TypeVar('E')


class Node(Generic[E]):
    def __init__(self, element: E, next):
        self.element = element
        self.next = next


class LinkList普通链表(AbstractList, Generic[E]):

    def __init__(self) -> None:
        # 元素数量（初始0）
        self.__eleCount: int = 0
        # 链表首个节点(置空)
        self.__firstNode: Node = None
        # 找不到元素
        self.__ELEMENT_NOT_FOUND = -1

    def clear(self):
        # 清除所有元素
        self.__eleCount = 0
        self.__firstNode = None

    def isEmpty(self) -> bool:
        # 是否为空
        return (self.__eleCount == 0)

    def contains(self, *, element: E) -> bool:
        # 是否包含某个元素
        return self.indexOfElement(element=element) is not self.__ELEMENT_NOT_FOUND

    def getElementAtIndex(self, *, index: int) -> E:
        self.__rangeCheck(index)
        # 获取index位置的元素

        resultNode: Node = self.__getNodeAtIndex(index)
        return resultNode.element

    def setElementAtIndex(self, *, index: int, element: E):
        # 设置index位置的元素
        self.__rangeCheck(index)

        resultNode: Node = self.__getNodeAtIndex(index)
        resultNode.element = element

    def addElementToTail(self, *, element: E):
        # 添加元素到最后
        if self.__eleCount == 0:
            # 创建第一个节点，next指向None
            self.__firstNode = Node(element, self.__firstNode)
        else:
            # 1.找到insert的下标的前一个node节点
            endNode: Node = self.__getNodeAtIndex(self.__eleCount - 1)
            # 2.新建插入节点，将其next指向原本在index位置的节点
            new_end_node = Node(element, endNode.next)
            # 3.将原本index前1位节点的next，指向新建节点
            endNode.next = new_end_node
        self.__eleCount += 1

    def insertElementAtIndex(self, *, index: int, element: E):
        # 在index位置插入一个元素
        self.__rangeCheckForAdd(index)

        if index == 0:
            # 创建第一个节点，next指向None
            self.__firstNode = Node(element, self.__firstNode)
        else:
            # 1.找到insert的下标的前一个node节点
            prevNode: Node = self.__getNodeAtIndex(index - 1)
            # 2.新建插入节点，将其next指向原本在index位置的节点
            new_insert_node = Node(element, prevNode.next)
            # 3.将原本index前1位节点的next，指向新建节点
            prevNode.next = new_insert_node
        self.__eleCount += 1

    def removeElementAtIndex(self, *, index: int):
        # 删除一个位置的元素
        self.__rangeCheck(index)

        curNode: Node = self.__firstNode
        if index == 0:
            # 删除首个节点，把原本的第二个节点指向为首节点
            self.__firstNode = self.__firstNode.next
        else:
            # 将prevNode.next指向prevNode.next.next
            prevNode: Node = self.__getNodeAtIndex(index - 1)
            curNode = prevNode.next
            prevNode.next = curNode.next
        self.__eleCount -= 1
        # 返回被删除的节点内容
        return curNode.element

    def indexOfElement(self, *, element: E) -> int:
        # 查看元素的索引
        if (element is None):
            # 匹配element为None的情况
            curNode: Node = self.__firstNode
            for i in range(self.__eleCount):
                if curNode.element is None:
                    return i
        else:
            # 匹配element有值的情况
            curNode: Node = self.__firstNode
            for i in range(self.__eleCount):
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

        curNode: Node = self.__firstNode
        for temp in range(index):
            curNode = curNode.next
        return curNode

    def __outOfBounds(self, index: int):
        # 超出index，抛出错误
        raise IndexError(f"下标越界：Index: {index}, eleCount: {self.__eleCount}")

    def __rangeCheck(self, index: int):
        # 检查index是否超出范围
        if index < 0 or index >= self.__eleCount:
            self.__outOfBounds(index)

    def __rangeCheckForAdd(self, index: int):
        # 监测index是否越界
        if index < 0 or index > self.__eleCount:
            self.__out_of_bounds(index)

    def __str__(self) -> str:
        string = ["普通汇总：\n\t元素数量:" + str(self.__eleCount) + ", \n\t"]
        for i in range(self.__eleCount):
            if i != 0:
                string.append("\n\t")
            string.append(f"index:{i}："+str(self.__getNodeAtIndex(i).element))
        return "".join(string)
