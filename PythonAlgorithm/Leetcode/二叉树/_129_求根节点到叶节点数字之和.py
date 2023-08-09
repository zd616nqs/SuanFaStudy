
# https://leetcode.cn/problems/sum-root-to-leaf-numbers/

""" 
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点


输入：root = [1,2,3]
输出：25
解释：
从根到叶子节点路径 1->2 代表数字 12
从根到叶子节点路径 1->3 代表数字 13
因此，数字总和 = 12 + 13 = 25

输入：root = [4,9,0,5,1]
输出：1026
解释：
从根到叶子节点路径 4->9->5 代表数字 495
从根到叶子节点路径 4->9->1 代表数字 491
从根到叶子节点路径 4->0 代表数字 40
因此，数字总和 = 495 + 491 + 40 = 1026


题解：

"""
from collections import deque


class TreeNode(object):
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class Solution(object):
    # 方法一：dfs深度优先搜索
    def sumNumbers1(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, prevSum: int):
            if not root:
                return 0
            sum: int = prevSum * 10 + root.val
            if (not root.left) and (not root.right):
                return sum
            else:
                return dfs(root.left, sum) + dfs(root.right, sum)
        
        return dfs(root, 0)
    
    # 方法二：bfs广度优先搜索
    def sumNumbers2(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue: deque = deque([root, root.val])
        sumResult: int = 0
        while (queue):
            node: TreeNode
            num: int
            node, num = queue.popleft() # 取出队头并且删除当前队头
            if not node.left and not node.right:
                # 当前节点没有子节点，sum增加，知道所有子节点遍历完，就是最终的值
                sumResult += num
            if node.left:
                # 将左子节点入队+左子节点的值入队
                queue.append([node.left, num * 10 + node.left.val])
            if node.right:
                # 将右子节点入队+右子节点的值入队
                queue.append([node.right, num * 10 + node.right.val])
        return sumResult