
from .Printer工具类.BinaryTree_AbstractInfo import BinaryTree_AbstractInfo
from .Printer工具类.Printer_Inorder import Printer_Inorder
from .Printer工具类.Printer_Levelorder import Printer_Levelorder
from enum import Enum



class PrintStyle(Enum):
    LEVEL_ORDER = 0
    INORDER = 1

class BinaryTrees(object):
    def __init__(self):
        pass
            
    @staticmethod
    def print(tree, style):
        """单纯打印"""
        if tree is None or (tree.root() is None):
            return
        BinaryTrees.generate_printer(tree, style).print()
    
    @staticmethod
    def println(tree, style):
        """打印后换行"""
        if tree is None or (tree.root() is None):
            return
        BinaryTrees.generate_printer(tree, style).println()
        
    @staticmethod
    def printString(tree, style):
        """生成整个树状图的字符串"""
        if tree is None or tree.root() is None:
            return None
        return BinaryTrees.generate_printer(tree, style).printString()



    @staticmethod
    def generate_printer(tree: BinaryTree_AbstractInfo, style: PrintStyle):
        if style == PrintStyle.INORDER:
            return Printer_Inorder(tree)
        return Printer_Levelorder(tree)