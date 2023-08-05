from abc import ABC, abstractmethod
from .BinaryTree_AbstractInfo import BinaryTree_AbstractInfo


class Printer(ABC):
    """
    抽象打印器类,负责按不同顺序打印二叉树
    """
    def __init__(self, tree: BinaryTree_AbstractInfo):
        self.tree: BinaryTree_AbstractInfo = tree

    @abstractmethod
    def print_string(self) -> str:
        """生成打印字符串"""
        # 抽象方法，没有实现

    def println(self):
        """打印后换行"""
        self.print()
        print()

    def print(self):
        """打印"""
        print(self.print_string())


