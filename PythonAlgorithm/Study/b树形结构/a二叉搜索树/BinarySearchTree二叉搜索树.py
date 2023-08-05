
from ..a二叉搜索树.Printer工具类.BinaryTree_AbstractInfo import BinaryTree_AbstractInfo

from typing import Generic, TypeVar
E = TypeVar('E')


# ---------定义node节点-----------
class Node(Generic[E]):

    def __init__(self, element, parent, left, right) -> None:
        self.element: E = element
        self.parent: Node = parent
        self.left: Node = left
        self.right: Node = right
        return self

    def isLeaf(self) -> bool:
        return (self.left is None) and (self.right is None)

    def hasTwoChild(self) -> bool:
        return (self.left is not None) and (self.right is not None)


class BinarySearchTree二叉搜索树(BinaryTree_AbstractInfo, Generic(E)):
    def __init__(self, comparator: callable) -> None:
        self.size = 0
        self.rootNode: Node = None
        if comparator is not None:
            self.comparator = comparator

    def nodeSize(self) -> int:
        """判断大小"""
        return self.size

    def isEmpty(self) -> bool:
        """判断是否为空"""
        return self.size == 0

    def clear(self):
        """清空元素"""
        self.root = None
        self.size = 0

    def addElement(self, ele: E):
        self.elementNotNullCheck(ele)
        # todo:niu 写不下去了。。先这样把。。
        pass
    

    def removeElement(self, ele: E):
        # todo:niu 写不下去了。。先这样把。。
        pass

    def removeNode(self, node: Node):
        if node is None:
            return
        self.size -= 1

        if node.hasTwoChild():
            # todo:niu 写不下去了。。先这样把。。
            pass

    # --------遍历查找node，看是否能找到--------

    def contains(self, element: E) -> bool:
        return self.getNodeWithEle(element) is not None

    # --------根据传入的节点值，遍历查找出对应的node--------
    def getNodeWithEle(self, element: E) -> Node:
        tempNode: Node = self.rootNode
        while (tempNode is not None):
            cmp: int = self.compareTwoElement(element, tempNode.element)
            if cmp > 0:
                tempNode = tempNode.right
            elif cmp == 0:
                return tempNode
            else:
                tempNode = tempNode.left
        return None

    def __str__(self) -> str:
        tempStr: str = ""
        self.printTree(node=self.rootNode, treeStr=tempStr, prefix="")
        return tempStr

    def printTree(self, node: Node, treeStr: str, prefix: str):
        if self.rootNode is None:
            return
        leftPrefix: str = prefix + "L---"
        rightPrefix: str = prefix + "R---"
        self.printTree(node=node.left, treeStr=treeStr, prefix=leftPrefix)
        treeStr += f"{prefix}{node.element}\n"
        self.printTree(node=node.right, treeStr=treeStr, prefix=rightPrefix)

    """ 
    --------判断两个节点的大小---------
    返回值等于0，代表e1和e2相等；
    返回值大于0，代表e1大于e2；
    返回值小于于0，代表e1小于e2
    """

    def compareTwoElement(self, e1: E, e2: E) -> int:
        if self.comparator is not None:
            return self.comparator(e1, e2)

        if e1 > e2:
            return 1
        elif e1 == e2:
            return 0
        else:
            return -1

    def elementNotNullCheck(cls, element: E):
        if element is None:
            raise ValueError("元素为空，请检查")

    # ------------重写抽象类方法-------
    # def root(self) -> Node:
    #    return self.root

    def right(self, node: Node) -> Node:
        return node.right

    def left(self, node: Node) -> Node:
        return node.left

    def printStr(self, node: Node) -> int:
        tempNode: Node = node
        parentStr: str = None
        if tempNode.parent is not None:
            parentStr += f"{tempNode.parent.element}"
        print(f"{tempNode.element}_p{parentStr})")
