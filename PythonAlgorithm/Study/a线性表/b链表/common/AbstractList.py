from typing import Generic, TypeVar
E = TypeVar('E')

# ABC：定义抽象类  
# abstractmethod：定义抽象方法
from abc import ABC, abstractmethod

class AbstractList(ABC, Generic[E]):
    
    # 清除所有元素
    @abstractmethod
    def clear(self): pass
    
    # 是否为空
    @abstractmethod        
    def isEmpty(self) -> bool: pass  

    # 是否包含某个元素
    @abstractmethod     
    def contains(self, *, element: E) -> bool: pass

    # 获取index位置的元素
    @abstractmethod
    def getElementAtIndex(self, *, index: int) -> E: pass
    
    # 设置index位置的元素
    @abstractmethod
    def setElementAtIndex(self, *, index: int, element: E): pass
    
    # 添加元素到最后
    @abstractmethod
    def addElementToTail(self, *, element: E): pass

    # 在index位置插入一个元素
    @abstractmethod
    def insertElementAtIndex(self, *, index: int, element: E): pass
    
    # 删除index位置的元素
    @abstractmethod
    def removeElementAtIndex(self, *, index: int): pass
    
    # 查看元素的索引
    @abstractmethod
    def indexOfElement(self, *, element: E) -> int: pass
    
