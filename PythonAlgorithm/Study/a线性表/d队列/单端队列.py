from ..b链表.双向链表.LinkList普通双向链表 import LinkList普通双向链表
from typing import Generic, TypeVar
E = TypeVar('E')


class 单端队列(Generic[E]):
    """ 
    单端队列：只能用右侧队尾放入，左侧队首拿出 (看定义队首在左右哪边决定)
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
        
    def enQueue(self, *, element: E):
        # --------入队列(从右侧队尾放入)--------
        self.__linkList.addElementToTail(element=element)
        
    def deQueue(self):
        # --------出队列(从左侧队首拿出)--------
        self.__linkList.removeElementAtIndex(index=0)        

    def front(self) -> E:
        # --------获取当前队列首个元素--------
        return self.__linkList.getElementAtIndex(index=0)

    def __str__(self) -> str:
        # --------打印队列时拼接字符串--------
        tempStr = f"{self.__linkList}"
        return tempStr