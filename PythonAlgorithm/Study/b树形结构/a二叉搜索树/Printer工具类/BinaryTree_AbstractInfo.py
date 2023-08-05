from abc import ABC, abstractmethod
from typing import Generic, TypeVar
E = TypeVar('E')

# ABC：定义抽象类
# abstractmethod：定义抽象方法
class BinaryTreeInfoProtocol(ABC, Generic[E]):

    # 获取根节点
    @abstractmethod
    def root(self, node: E) -> E: pass

    # 获取左节点
    @abstractmethod
    def left(self, node: E) -> E: pass

    # 获取右节点
    @abstractmethod
    def right(self, node: E) -> E: pass

    # 打印当前节点信息
    @abstractmethod
    def printStr(self, node: E) -> E: pass
