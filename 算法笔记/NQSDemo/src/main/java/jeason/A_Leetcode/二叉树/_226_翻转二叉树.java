package jeason.A_Leetcode.二叉树;


// https://leetcode-cn.com/problems/invert-binary-tree/


import java.util.LinkedList;
import java.util.Queue;
public class _226_翻转二叉树 {


    //*******************************************************
    //前序遍历
    private void preorder(TreeNode node) {
		if (node == null) return;
		
        System.out.println(node.element);//在前面打印节点
		preorder(node.left);
		preorder(node.right);
	}

    //使用 前序遍历 翻转二叉树
    public TreeNode invertTree1(TreeNode root){
        if (root == null) return null;
        // 保存右子树,然后交换左右子树的位置
        TreeNode rightTree = root.right;
        root.right = invertTree1(root.left);
        root.left = invertTree1(rightTree);
        return root;
    }


    //*******************************************************
    //中序遍历
    private void inorder(TreeNode node) {
		if (node == null) return;
		
		inorder(node.left);
        System.out.println(node.element);//在中间打印节点
		inorder(node.right);
	}


    //使用 中序遍历 翻转
    public TreeNode invertTree2(TreeNode root){
        if (root == null) return null;
        // 递归找到左节点
        invertTree2(root.left); 
        // 保存右节点
        TreeNode rightNode= root.right; 
        root.right = root.left;
        root.left = rightNode;
        // 递归找到右节点 继续交换 : 因为此时左右节点已经交换了,所以此时的右节点为root.left
        invertTree2(root.left); 
        return root;
    }
    //*******************************************************
    //后序遍历
    private void postorder(TreeNode node) {
		if (node == null) return;
		
		postorder(node.left);
		postorder(node.right);
		System.out.println(node.element);//在后面打印节点
	}
    
    //使用 后序遍历 翻转
    public TreeNode invertTree3(TreeNode root){
        // 后序遍历-- 从下向上交换
        if (root == null) return null;
        TreeNode leftNode = invertTree3(root.left);
        TreeNode rightNode = invertTree3(root.right);
        root.right = leftNode;
        root.left = rightNode;
        return root;
    }
    //*******************************************************

    //层序遍历
    public void levelOrder(TreeNode root) {
		if (root == null) return;
		
		Queue<TreeNode> queue = new LinkedList<>();
		//根节点 入队列
		queue.offer(root);
		
		while (!queue.isEmpty()) {
			//取出队头后，删除该元素，队头向后移1位
			TreeNode node = queue.poll();

			System.out.println(node.element);//在此处打印节点

			if (node.left != null) {
				//左节点 入队列
				queue.offer(node.left);
			}
			
			if (node.right != null) {
				//右节点 入队列
				queue.offer(node.right);
			}
		}
	}

    //使用 层序遍历 翻转
    public TreeNode invertTree4(TreeNode root){
        // 层次遍历--直接左右交换即可
        if (root == null) return null;
        Queue<TreeNode> queue = new LinkedList<>();

        queue.offer(root);//取出队头后，删除该元素，队头向后移1位

        while (!queue.isEmpty()){
            TreeNode node = queue.poll();//入队

            //此处操作交换
            TreeNode rightTree = node.right;
            node.right = node.left;
            node.left = rightTree;


            if (node.left != null){
                //左节点 入队列
                queue.offer(node.left);
            }
            if (node.right != null){
                //右节点 入队列
                queue.offer(node.right);
            }
        }
        return root;
    }






    //定义TreeNode
    private static class TreeNode {
		int element;
		TreeNode left;
		TreeNode right;
		TreeNode parent;
		public TreeNode(int element, TreeNode parent) {
			this.element = element;
			this.parent = parent;
		}

	}


}
