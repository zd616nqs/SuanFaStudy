
# https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/description/

""" 
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：
    5
   /  \
   2   6
 /  \
1    3

输入: [1,6,3,2,5]
输出: false

输入: [1,3,2,6,5]
输出: true

输入: [5,7,6,9,11,10,8]
输出: true

题解1：https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solutions/824014/bsthou-xu-jian-cha-di-gui-he-die-dai-jie-x1yo/

题解2：https://blog.csdn.net/Oblak_ZY/article/details/124655213
"""

# Definition for a binary tree node.
from ast import List


class TreeNode(object):
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class Solution(object):
    
    # 递归的方法
    ''' 
    思路：
    1.以根节点(即数组最后一个值)为分界线，划分出两部分(根节点左边、根节点右边)
    2.左半部分都比根节点小，右半部分都比根节点大(如果划分出来不止2部分，这个二叉树就不是二叉搜索树BST)
    3.
    '''
    def verifyPostorder(self, dataList: List[int]) -> bool:
        # 如果数据为空，返回true
        if not dataList:
            return True
        
        # 后序遍历的情况下，最后一个元素，就是整个二叉树的根节点
        root = dataList[-1]
        
        # 左半结点都比根结点小，右半部分都比根结点大
        eleCount = len(dataList) # 二叉树所有节点数量
        segmentIndex = 0 # 自增找到左右子树的分割点下标
        
        # while循环结束后，segmentIndex的值就是后序遍历中，根节点的右子树中第一个元素的下标
        while (segmentIndex < eleCount) and (dataList[segmentIndex] < root):
            segmentIndex += 1
        
        # 确定了根节点右子树的所有节点的index范围
        for tempIndex in range(segmentIndex, eleCount - 1):
            # 根节点右子树的所有节点，都要比root大，如果不匹配，就返回false
            if not dataList[tempIndex] > root:
                return False
        
        # 以segmentIndex为分界点，向二叉树下一层继续匹配下一层的左右子树是否匹配
        return self.verifyPostorder(dataList[:segmentIndex]) and self.verifyPostorder(dataList[segmentIndex:-1])