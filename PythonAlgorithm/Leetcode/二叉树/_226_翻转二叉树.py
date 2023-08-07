
from collections import deque
# https://leetcode.cn/problems/binary-tree-maximum-path-sum/

""" 
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。


    
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right


class Solution(object):
    
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        result: TreeNode = None
        # 前序遍历
        result = self.invertTreeWithPreorder(root)
        # 中序遍历
        result = self.invertTreeWithInorder(root)
        # 后序遍历
        result = self.invertTreeWithPostorder(root)
        # 层序遍历
        result = self.invertTreeWithLevelorder(root)
        return result
    
    # -----------前序遍历---------
    # 前序遍历二叉树
    def preorder(self, root: TreeNode) -> None:
        if root is None:
            return None

        print(f"{root.val}")
        self.preorder(root.left)
        self.preorder(root.right)

    # 使用前序遍历的方式 翻转二叉树
    def invertTreeWithPreorder(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        # 保存右子树,然后交换左右子树的位置
        rightTree: TreeNode = root.right
        root.right = self.invertTreeWithPreorder(root.left)
        root.left = self.invertTreeWithPreorder(rightTree)
        return root

    # -----------中序遍历---------
    # 中序遍历二叉树
    def inorder(self, root: TreeNode) -> None:
        if root is None:
            return None

        self.inorder(root.left)
        print(f"{root.val}")
        self.inorder(root.right)

    # 使用中序遍历的方式 翻转二叉树
    def invertTreeWithInorder(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        # 1.递归找到左侧的所有节点
        self.invertTreeWithInorder(root.left)
        # 2.每层递归时将左右节点互换位置
        rightNode: TreeNode = root.right
        root.right = root.left
        root.left = rightNode
        # 3.上一层的右节点都被换到左边了，继续向下递归查找
        self.invertTreeWithInorder(root.left)
        return root

    # -----------后序遍历---------
    # 后序遍历二叉树
    def postorder(self, root: TreeNode) -> None:
        if root is None:
            return None

        self.postorder(root.left)
        self.postorder(root.right)
        print(f"{root.val}")

    # 使用后序遍历的方式 翻转二叉树
    def invertTreeWithPostorder(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        # 1.后序遍历-- 从下向上交换
        leftNode: TreeNode = self.invertTreeWithPostorder(root.left)
        rightNode: TreeNode = self.invertTreeWithPostorder(root.right)
        # 2. 左右互换位置
        root.right = leftNode
        root.left = rightNode
        return root

    # -----------层序遍历---------
    # 后序遍历二叉树
    def levelorder(self, root: TreeNode) -> None:
        if root is None:
            return None

        queue: deque = deque([root])
        while (len(queue)):
            tempNode: TreeNode = queue.popleft()
            print(f"{tempNode.val}")

            if tempNode.left is not None:
                # 左节点 入队列
                queue.append(tempNode.left)

            if tempNode.right is not None:
                # 右节点 入队列
                queue.append(tempNode.right)

        print(f"{queue}")

    # 使用层序遍历的方式 翻转二叉树
    def invertTreeWithLevelorder(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        queue: deque = deque([root])
        while (len(queue)):
            tempNode: TreeNode = queue.popleft()

            # 此处操作交换
            rightNode = tempNode.right
            tempNode.right = tempNode.left
            tempNode.left = rightNode

            if tempNode.left is not None:
                # 左节点 入队列
                queue.append(tempNode.left)

            if tempNode.right is not None:
                # 右节点 入队列
                queue.append(tempNode.right)

        print(f"{queue}")
        return root
