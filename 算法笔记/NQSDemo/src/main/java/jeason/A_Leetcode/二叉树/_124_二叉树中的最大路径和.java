package jeason.A_Leetcode.二叉树;


// https://leetcode.cn/problems/binary-tree-maximum-path-sum/



public class _124_二叉树中的最大路径和 {


//思路：使用递归，不停的返回当前节点能够贡献的最大数值，然后maxSum一直更新比较得到最大值

    //声明最终返回的变量
    int maxSum = 0;

    public int maxPathSum(TreeNode root) {
        //递归调用
        maxGain(root);
        return maxSum;
    }

    public int maxGain(TreeNode node) {
        if (node == null) {
            return 0;
        }
        
        // 递归计算左右子节点的最大贡献值
        // 只有在最大贡献值大于 0 时，才会选取对应子节点
        int leftGain = Math.max(maxGain(node.left), 0);
        int rightGain = Math.max(maxGain(node.right), 0);

        // 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
        int priceNewpath = node.element + leftGain + rightGain;

        // 更新最大值
        maxSum = Math.max(maxSum, priceNewpath);

        // 返回节点的最大贡献值
        return node.element + Math.max(leftGain, rightGain);
    }


    //定义TreeNode
    private static class TreeNode {
        int element;
        TreeNode left;
        TreeNode right;
    }


}
