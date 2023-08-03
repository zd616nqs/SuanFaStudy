from ..b链表.双向链表.LinkList普通双向链表 import LinkList普通双向链表
from typing import Generic, TypeVar
E = TypeVar('E')


class 双端队列(Generic[E]):
    """ 
    双端队列：队尾能放入和拿出，队首也能放入和拿出(看定义左右哪边是队首)
    队首：Front
    队尾：Rear
    """

    def __init__(self) -> None:
        self.__linkList = LinkList普通双向链表()

    def size(self) -> int:
        # --------队列的长度--------
        return self.__linkList.nodeCount()

    def isEmpty(self) -> bool:
        # --------队列是否为空--------
        return self.__linkList.isEmpty()

    def clear(self):
        # --------清空队列--------
        self.__linkList.clear()

    # ---------------队首(左侧)出队入队----------------
    def enQueueWithFront(self, *, element: E):
        # 队首：入队列(从左侧队首放入)
        self.__linkList.insertElementAtIndex(index=0, element=element)

    def deQueueWithFront(self):
        # 队首：出队列(从左侧队首拿出)
        self.__linkList.removeElementAtIndex(index=0)

    # ---------------队尾(右侧)出队入队----------------
    def enQueueWithRear(self, *, element: E):
        # 队尾：入队列(从右侧队尾放入)
        self.__linkList.addElementToTail(element=element)

    def deQueueWithRear(self):
        # 队尾：出队列(从右侧队尾拿出)
        self.__linkList.removeElementAtIndex(index=self.size()-1)

    def front(self) -> E:
        # --------获取当前队首元素--------
        return self.__linkList.getElementAtIndex(index=0)

    def rear(self) -> E:
        # --------获取当前队尾元素--------
        rearIndex: int = self.size() - 1
        return self.__linkList.getElementAtIndex(index=rearIndex)

    def __str__(self) -> str:
        # --------打印队列时拼接字符串--------
        tempStr = f"{self.__linkList}"
        return tempStr
