# from abc import ABC, abstractmethod
from .Printer import Printer
from .BinaryTree_AbstractInfo import BinaryTree_AbstractInfo
from .StringTool import StringTool



#              ┌──800
#          ┌──760
#          │   └──600
#      ┌──540
#      │   └──476
#      │       └──445
#  ┌──410
#  │   └──394
# 381
#  │     ┌──190
#  │     │   └──146
#  │  ┌──40
#  │  │  └──35
#  └──12
#     └──9


# 实现中序打印器
class Printer_Inorder(Printer):
    """
    按中序遍历顺序打印二叉树
    类属性:
        right_append - 表示节点右边线的字符串
        left_append  - 表示节点左边线的字符串     
        blank_append - 空白字符串     
        line_append  - 节点内线的字符串      
    """
    defaultLength: int = 2
    right_append = "┌" + StringTool.repeat("─", defaultLength)            
    left_append = "└" + StringTool.repeat("─", defaultLength)  
    blank_append = StringTool.blank(defaultLength + 1)     
    line_append = "│" + StringTool.blank(defaultLength)   

    def __init__(self, tree: BinaryTree_AbstractInfo):
        super().__init__(tree)

    def print_string(self) -> str:
        """生成整个树状图的字符串"""
        result: str = self._print_string(self.tree.root(), "", "", "")
        result = result[:-1] # 删除最后一个字符
        return result
    


    def _print_string(self, node: object, node_prefix: str, left_prefix: str, right_prefix: str):
        """ 
        生成node节点的字符串
        参数：
            nodePrefix node那一行的前缀字符串
            leftPrefix node整棵左子树的前缀字符串
            rightPrefix node整棵右子树的前缀字符串
        """
        left: object = self.tree.left(node)  
        right: object = self.tree.right(node)
        string: str = self.tree.string(node) 
        
        length = len(string)
        if length % 2 == 0:  
            length -= 1           
        length >>= 1       
        
        node_string: str = ""  
        if right is not None:  
            right_prefix += StringTool.blank(length) 
            node_string += self._print_string(right, right_prefix + self.right_append, right_prefix + self.line_append, right_prefix + self.blank_append)   
                
        node_string += (node_prefix + string + "\n")
        
        if left is not None:                
            left_prefix += StringTool.blank(length)
            node_string += self._print_string(left, left_prefix + self.left_append, left_prefix + self.blank_append, left_prefix + self.line_append)            
                
        return node_string

