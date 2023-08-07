
# https://leetcode.cn/problems/subtree-of-another-tree/

""" 
给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。

二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。

输入：root = [3,4,5,1,2], subRoot = [4,1,2]
输出：true

题解：https://leetcode.cn/problems/subtree-of-another-tree/solutions/235634/dui-cheng-mei-pan-duan-zi-shu-vs-pan-duan-xiang-de/


判断两个树是否相等的三个条件是与的关系，即：
    1.当前两个树的根节点值相等；
    2.并且，s 的左子树和 t 的左子树相等；
    3.并且，s 的右子树和 t 的右子树相等。

而判断 t 是否为 s 的子树的三个条件是或的关系，即：
    1.当前两棵树相等；
    2.或者，t 是 s 的左子树；
    3.或者，t 是 s 的右子树。

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class Solution(object):
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        # 方法：深度优先搜索暴力匹配    
        # dfs深度搜索能匹配的根节点，然后check往下的一层一层的子节点是否相同
        def dfsSubTree(root: TreeNode, subRoot: TreeNode) -> bool:
            if root is None:
                return False
            
            # 三种情况都进行判断,找到能匹配的更节点
            result: bool = (isSameTree(root, subRoot) or dfsSubTree(root.left, subRoot) or dfsSubTree(root.right, subRoot))
            return result
            
        
        def isSameTree(root: TreeNode, subRoot: TreeNode) -> bool:
            # 都是空的tree，符合条件
            if root is None and subRoot is None:
                return True
            # 节点值不相同，或者其中一个为空，不符合条件
            elif (root is None) or (subRoot is None) or (root.val != subRoot.val):
                return False
            # 比较两个tree的下一层左右节点是否依然相同，一层层往下对比
            nextMatch: bool = isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
            return nextMatch
        
        return dfsSubTree(root=root, subRoot=subRoot)