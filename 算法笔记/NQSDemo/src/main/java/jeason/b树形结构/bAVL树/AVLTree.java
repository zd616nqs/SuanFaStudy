package jeason.b树形结构.bAVL树;
import jeason.b树形结构.bAVL树.tree.*;

import java.util.Comparator;


//AVL树继承自二叉搜素树BST
public class AVLTree<E> extends BST<E> {
	public AVLTree() {
		this(null);
	}
	
	public AVLTree(Comparator<E> comparator) {
		super(comparator);
	}
	
	//--------添加某个节点后:1.更新高度2.平衡二叉树-------------
	@Override
	public void afterAdd(Node<E> node) {
		while ((node = node.parent) != null) {
			if (isBalanced(node)) {
				//新添加进来的叶子节点的父节点,平衡因子是平衡的---->直接更新高度
				updateHeight(node);
			} else {
				//新添加进来的叶子节点的父节点,平衡因子为不是平衡的---->去恢复平衡
				//入参的node是不平衡的父子节点
				rebalance(node);
				// 整棵树恢复平衡
				break;
			}
		}
	}
	
	//--------删除某个节点后:1.更新高度2.平衡二叉树-------------
	@Override
	public void afterRemove(Node<E> node) {
		while ((node = node.parent) != null) {
			if (isBalanced(node)) {
				// 删除节点后,整个二叉树是平衡的---->直接更新高度
				updateHeight(node);
			} else {
				// 删除节点后,整个二叉树是不平衡的---->去恢复平衡
				rebalance(node);
			}
		}
	}
	
	//--------重写父类BST的创建节点方法,返回AVLNode节点------------
	@Override
	
	public Node<E> createNode(E element, Node<E> parent) {
		return new AVLNode<>(element, parent);
	}
	
	//--------------恢复平衡(左旋转和右旋转组合使用)---------
	//grand:平衡因子不平衡的-->对应的根子节点
	@SuppressWarnings("unused")
	private void rebalance2(Node<E> grand) {
		//获取不平衡节点的--->高度比较高的一个子节点
		Node<E> parent = ((AVLNode<E>)grand).tallerChild();
		//获取不平衡节点的--->高度比较高的一个子节点的--->高度比较高的一个子节点的
		Node<E> node = ((AVLNode<E>)parent).tallerChild();
		if (parent.isLeftChild()) { 
			// L
			if (node.isLeftChild()) { 
				// LL
				rotateRight(grand);
			} else { 
				// LR
				rotateLeft(parent);
				rotateRight(grand);
			}
		} else { 
			// R
			if (node.isLeftChild()) { 
				// RL
				rotateRight(parent);
				rotateLeft(grand);
			} else { 
				// RR
				rotateLeft(grand);
			}
		}
	}

	private void rotateLeft(Node<E> grand) {
		Node<E> parent = grand.right;
		Node<E> child = parent.left;
		grand.right = child;
		parent.left = grand;
		afterRotate(grand, parent, child);
	}
	
	private void rotateRight(Node<E> grand) {
		Node<E> parent = grand.left;
		Node<E> child = parent.right;
		grand.left = child;
		parent.right = grand;
		afterRotate(grand, parent, child);
	}
	private void afterRotate(Node<E> grand, Node<E> parent, Node<E> child) {
		// 让parent称为子树的根节点
		parent.parent = grand.parent;
		if (grand.isLeftChild()) {
			grand.parent.left = parent;
		} else if (grand.isRightChild()) {
			grand.parent.right = parent;
		} else { // grand是root节点
			root = parent;
		}
		
		// 更新child的parent
		if (child != null) {
			child.parent = grand;
		}
		
		// 更新grand的parent
		grand.parent = parent;
		
		// 更新高度
		updateHeight(grand);
		updateHeight(parent);
	}
	







	//--------------恢复平衡(统一所有旋转)---------
	//grand:平衡因子不平衡的-->对应的根子节点
	private void rebalance(Node<E> grand) {
		Node<E> parent = ((AVLNode<E>)grand).tallerChild();
		Node<E> node = ((AVLNode<E>)parent).tallerChild();
		if (parent.isLeftChild()) { 
			// L
			if (node.isLeftChild()) { 
				// LL   根节点   b        c         d          e          f
				rotate(grand, node, node.right, parent, parent.right, grand);
			} else { 
				// LR   根节点   b        c         d       e          f
				rotate(grand, parent, node.left, node, node.right, grand);
			}
		} else { 
			// R
			if (node.isLeftChild()) { 
				// RL   根节点   b        c       d       e          f
				rotate(grand, grand, node.left, node, node.right, parent);
			} else { 
				// RR   根节点   b        c         d         e        f
				rotate(grand, grand, parent.left, parent, node.left, node);
			}
		}
	}
	
	//统一所有旋转:所有旋转方案
	// 1.最后d都会成为根节点,a和g的父节点都没发生变化
	// 2.变化的只有bdf的父/子关系 和 b-c的父/子关系 和 e-f的父/子关系
	//          LL            RR                LR             RL
	//        ┌──f──┐     ┌──b──┐           ┌────f──┐      ┌──b────┐ 
	//        │     │     │     │           │       │      a       │
	//     ┌──d──┐	g     a  ┌──d──┐      ┌─b───┐   g           ┌──f──┐
	//     │     │           │     │      │     │               │     │
	//   ┌─b─┐   e           c   ┌─f─┐    a   ┌─d─┐           ┌─d─┐   g
	//   │   │                   │   │        │   │           │   │
	//   a   c                   e   g        c   e           c   e
	//
	// 旋转平衡后都会变成下面的样子:
	//     ┌──d──┐
	//     │     │
	//   ┌─b─┐ ┌─e─┐
	//   │   │ │   │
	//   a   c f   g
	private void rotate(
			Node<E> r, // 子树的根节点
			Node<E> b, Node<E> c,
			Node<E> d,
			Node<E> e, Node<E> f) {
		// 让d成为这棵子树的根节点
		d.parent = r.parent;
		if (r.isLeftChild()) {
			r.parent.left = d;
		} else if (r.isRightChild()) {
			r.parent.right = d;
		} else {
			root = d;
		}
		
		//b-c
		b.right = c;
		if (c != null) {
			c.parent = b;
		}
		updateHeight(b);
		
		// e-f
		f.left = e;
		if (e != null) {
			e.parent = f;
		}
		updateHeight(f);
		
		// b-d-f
		d.left = b;
		d.right = f;
		b.parent = d;
		f.parent = d;
		updateHeight(d);
	}
	
	
	
	




	//--------判断节点是否是平衡(平衡因子为-1/0/1时就是平衡)----------
	private boolean isBalanced(Node<E> node) {
		return Math.abs(((AVLNode<E>)node).balanceFactor()) <= 1;
	}
	//--------更新节点高度-------------
	private void updateHeight(Node<E> node) {
		((AVLNode<E>)node).updateHeight();
	}
	









	//--------创建Node子类AVLNode,添加了height属性来判断平衡因子---------
	private static class AVLNode<E> extends Node<E> {
		int height = 1;
		
		public AVLNode(E element, Node<E> parent) {
			super(element, parent);
		}
		
		//-----计算平衡因子
		public int balanceFactor() {
			int leftHeight = left == null ? 0 : ((AVLNode<E>)left).height;
			int rightHeight = right == null ? 0 : ((AVLNode<E>)right).height;
			return leftHeight - rightHeight;
		}
		
		//-----更新当前节点的高度
		public void  updateHeight() {
			int leftHeight = left == null ? 0 : ((AVLNode<E>)left).height;
			int rightHeight = right == null ? 0 : ((AVLNode<E>)right).height;
			height = 1 + Math.max(leftHeight, rightHeight);
		}
		
		//-----获取左右子节点,高度更高的一个
		public Node<E> tallerChild() {
			int leftHeight = left == null ? 0 : ((AVLNode<E>)left).height;
			int rightHeight = right == null ? 0 : ((AVLNode<E>)right).height;
			if (leftHeight > rightHeight) return left;
			if (leftHeight < rightHeight) return right;
			//如果左右子节点一样高,默认返回左子节点
			return isLeftChild() ? left : right;
		}
		
		@Override
		public String toString() {
			String parentString = "null";
			if (parent != null) {
				parentString = parent.element.toString();
			}
			return element + "_p(" + parentString + ")_h(" + height + ")";
		}
	}
}
