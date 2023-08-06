
# https://leetcode.cn/problems/binary-tree-maximum-path-sum/

""" 
思路：定义一个全局变量maxSum，不停的左右树递归，比较maxSum和当前节点的路径值，递归结束就拿到最大值了
题解：https://leetcode.cn/problems/binary-tree-maximum-path-sum/solutions/293434/124di-gui-de-jing-sui-ji-lu-yi-xia-by-821218213/


输入[1,2,4,5,6,4]
//     ┌──1──┐
//     │     │
//   ┌─2─┐ ┌─3─┐
//   │   │ │   │
//   4   5 6   4

期望输出结果：5+2+1+3+6 = 17

    
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class Solution(object):
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0

        # 初始化最大路径和
        self.maxSum: float = float("-inf")

        # 深度递归
        def dfs(tempNode: TreeNode) -> float:
            if tempNode is None:
                return 0
            
            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain: float = dfs(tempNode.left)
            rightGain: float = dfs(tempNode.right)

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            newPathValue: float = tempNode.val + leftGain + rightGain
            # 更新最大值
            self.maxSum = max(self.maxSum, newPathValue)
            
            # 返回节点的最大贡献值
            return max(0, max(leftGain, rightGain) + tempNode.val)

        dfs(root)

        return self.maxSum





