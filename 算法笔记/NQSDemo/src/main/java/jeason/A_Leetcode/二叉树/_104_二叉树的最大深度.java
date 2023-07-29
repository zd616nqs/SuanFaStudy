package jeason.A_Leetcode.二叉树;
import java.util.LinkedList;
import java.util.Queue;


// https://leetcode.cn/problems/maximum-depth-of-binary-tree/



public class _104_二叉树的最大深度 {

    // 方法一：深度优先搜索
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        } else {
            int leftHeight = maxDepth(root.left);
            int rightHeight = maxDepth(root.right);
            return Math.max(leftHeight, rightHeight) + 1;
        }
    }



    // 方法二：广度优先搜索
    public int maxDepth2(TreeNode root) {
        if (root == null) {
            return 0;
        }

        Queue<TreeNode> nodeQueue = new LinkedList<TreeNode>();//新建空队列
        nodeQueue.offer(root);//入队列

        int resultDepth = 0;
        while (!nodeQueue.isEmpty()) {
            int size = nodeQueue.size();
            while (size > 0) {
                TreeNode node = nodeQueue.poll();//取出队头并且删除当前队头
                if (node.left != null) {
                    //将左子节点入队
                    nodeQueue.offer(node.left);
                }
                if (node.right != null) {
                    //将右子节点入队
                    nodeQueue.offer(node.right);
                }
                size--;
            }
    
            resultDepth++;
        }
        return resultDepth;
    }



     //定义TreeNode
    private static class TreeNode {
		TreeNode left;
		TreeNode right;
        // int element;
	}

}
