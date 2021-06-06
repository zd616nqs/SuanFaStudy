package jeason.A_Leetcode.二叉树;
import java.util.LinkedList;
import java.util.Queue;


// https://leetcode-cn.com/problems/subtree-of-another-tree/



public class _572_判断另一个树的子树{


    // 方法：深度优先搜索暴力匹配
    public boolean isSubtree(TreeNode s, TreeNode t) {
        return dfs(s, t);
    }

    public boolean dfs(TreeNode s, TreeNode t) {
        if (s == null) {
            return false;
        }
        //三种都判断，有一个成立就对
        return check(s, t) || dfs(s.left, t) || dfs(s.right, t);
    }

    public boolean check(TreeNode s, TreeNode t) {
        if (s == null && t == null) {
            return true;
        }
        if (s == null || t == null || s.element != t.element) {
            return false;
        }
        return check(s.left, t.left) && check(s.right, t.right);
    }




     //定义TreeNode
    private static class TreeNode {
		TreeNode left;
		TreeNode right;
        int element;
	}


}
