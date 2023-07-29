package jeason.A_Leetcode.二叉树;
import java.util.LinkedList;
import java.util.Queue;

// https://leetcode.cn/problems/sum-root-to-leaf-numbers/



public class _129_求根节点到叶节点数字之和 {

//定义TreeNode
    private static class TreeNode {
        int element;
        TreeNode left;
        TreeNode right;
    }


    // 方法一：深度优先搜索
    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
    }
    
    public int dfs(TreeNode root, int prevSum) {
        if (root == null) {
            return 0;
        }
        int sum = prevSum * 10 + root.element;
        if (root.left == null && root.right == null) {
            return sum;
        } else {
            return dfs(root.left, sum) + dfs(root.right, sum);
        }
    }


// 方法二：广度优先搜索
    public int sumNumbers2(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int sum = 0;
        Queue<TreeNode> nodeQueue = new LinkedList<TreeNode>();
        Queue<Integer> numQueue = new LinkedList<Integer>();
        nodeQueue.offer(root);//入队列
        numQueue.offer(root.element);//入队列

        while (!nodeQueue.isEmpty()) {
            TreeNode node = nodeQueue.poll();//取出队头并且删除当前队头
            int num = numQueue.poll();//取出队头并且删除当前队头

            //取出当前循环的左右子节点
            TreeNode left = node.left;
            TreeNode right = node.right;


            if (left == null && right == null) {
                //当前节点没有子节点，sum增加，知道所有子节点遍历完，就是最终的值
                sum += num;
            } else {
                if (left != null) {
                    nodeQueue.offer(left);//将左子节点入队
                    numQueue.offer(num * 10 + left.element);//左子节点的值入队
                }
                if (right != null) {
                    nodeQueue.offer(right);//将右子节点入队
                    numQueue.offer(num * 10 + right.element);//将右子节点的值入队
                }
            }
        }
        return sum;
    }

}
