import collections
from typing import Optional

# https://leetcode.cn/problems/maximum-depth-of-binary-tree/
""" 
给定一个二叉树 root ，返回其最大深度
二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

举例1：
输入：root = [3,9,20,null,null,15,7]
输出：3

举例1：
输入：root = [1,null,2]
输出：2
"""
"""
题解：https://leetcode.cn/problems/maximum-depth-of-binary-tree/solutions/602614/104-er-cha-shu-de-zui-da-shen-du-by-edel-pkbp/
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # ---------方法一：深度优先搜索--------------
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            leftHeight: int = self.maxDepth1(root=root.left)
            rightHeight: int = self.maxDepth1(root=root.right)
            result: int = max(leftHeight, rightHeight) + 1
            return result
    
    # ---------方法二：广度优先搜索--------------
    def maxDepth2(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        print(f"{root}\n")
        """
        TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}
        """
        

        # 根据root节点，将整个树的所有节点添加进队列
        nodeQueue = collections.deque([root])
        print(f"{nodeQueue}")
        """
        deque([TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}]) 
        """
        
        resultDepth: int = 0
        while nodeQueue:
            # 获取当前总的节点数
            size: int = len(nodeQueue)
            for i in range(size):
                # 取出当前最新的子节点
                tempNode: TreeNode = nodeQueue.popleft()
                if tempNode.left is not None:
                    nodeQueue.append(tempNode.left)
                if tempNode.right is not None:
                    nodeQueue.append(tempNode.right)
            # 每次for循环都会消耗一层的节点，直到size为0时，就遍历到最深的叶子节点处了
            resultDepth += 1
            print("深度加1 \n")
        return resultDepth




def run():
    print("")

run()



class _104_二叉树的最大深度(object):
    @staticmethod
    def run(self):
        print("")