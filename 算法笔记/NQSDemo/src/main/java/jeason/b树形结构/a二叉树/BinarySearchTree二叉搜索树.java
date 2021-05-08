package jeason.b树形结构.a二叉树;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;


import jeason.b树形结构.a二叉树.Printer工具类.base.BinaryTreeInfoProtocol;

// import com.mj.printer.BinaryTreeInfo;

@SuppressWarnings("unchecked")
public class BinarySearchTree二叉搜索树 <E> implements BinaryTreeInfoProtocol {
	private int size;
	private Node<E> root;
	private Comparator<E> comparator;
	
	public BinarySearchTree二叉搜索树() {
		this(null);
	}
	
	public BinarySearchTree二叉搜索树(Comparator<E> comparator) {
		this.comparator = comparator;
	}
	
	//-----------------判断大小-----------------------
	public int size() {
		return size;
	}

	//-----------------判断是否为空-----------------------
	public boolean isEmpty() {
		return size == 0;
	}

	//-----------------清空元素-----------------------
	public void clear() {
		root = null;
		size = 0;
	}

	//-----------------添加元素-----------------------
	public void add(E element) {
		elementNotNullCheck(element);
		
		// ********添加第一个节点*********
		if (root == null) {
			root = new Node<>(element, null);
			size++;
			return;
		}
		
		// *******添加的不是第一个节点*********
		// ——————1.找到父节点--------
		Node<E> parent = root;
		Node<E> node = root;
		int cmp = 0;
		do {
			cmp = compare(element, node.element);
			//循环查找，最终找到需要插入的父节点
			parent = node;

			if (cmp > 0) {
				//从父节点的右边寻找下去
				node = node.right;
			} else if (cmp < 0) {
				//情况1：从父节点的左边寻找下去
				//情况2：插入完毕后，又一次循环到此处置null，跳出循环
				node = node.left;
			} else { // 相等
				node.element = element;
				return;
			}
		} while (node != null);


		// --------2.找到父节点后，判断插入到父节点的哪个位置-------
		Node<E> newNode = new Node<>(element, parent);
		if (cmp > 0) {
			parent.right = newNode;
		} else {
			parent.left = newNode;
		}
		size++;
	}



	public boolean contains(E element) {
		//遍历查找node，看是否能找到
		return node(element) != null;
	}


	public void remove(E element) {
		remove(node(element));
	}
	
	private void remove(Node<E> node) {
		if (node == null) return;
		
		size--;
		
		if (node.hasTwoChildren()) { // 度为2的节点
			// 找到后继节点
			Node<E> s = successor(node);
			// 用后继节点的值覆盖度为2的节点的值
			node.element = s.element;
			// 删除后继节点
			node = s;
		}
		
		// 删除node节点（node的度必然是1或者0）
		Node<E> replacement = node.left != null ? node.left : node.right;
		
		if (replacement != null) { // node是度为1的节点
			// 更改parent
			replacement.parent = node.parent;
			// 更改parent的left、right的指向
			if (node.parent == null) { // node是度为1的节点并且是根节点
				root = replacement;
			} else if (node == node.parent.left) {
				node.parent.left = replacement;
			} else { // node == node.parent.right
				node.parent.right = replacement;
			}
		} else if (node.parent == null) { // node是叶子节点并且是根节点
			root = null;
		} else { // node是叶子节点，但不是根节点
			if (node == node.parent.left) {
				node.parent.left = null;
			} else { // node == node.parent.right
				node.parent.right = null;
			}
		}
	}
	
	//--------根据传入的节点值，遍历查找出对应的node--------
	private Node<E> node(E element) {
		Node<E> node = root;
		while (node != null) {
			int cmp = compare(element, node.element);
			if (cmp == 0) return node;
			if (cmp > 0) {
				node = node.right;
			} else { // cmp < 0
				node = node.left;
			}
		}
		return null;
	}


	//-----------前序遍历Preorder Traversal----------
	//根节点--->前序遍历左子树--->前序遍历右子树
	public void preorder(Visitor<E> visitor) {
		if (visitor == null) return;
		preorder(root, visitor);
	}
	private void preorder(Node<E> node, Visitor<E> visitor) {
		if (node == null || visitor.stop) return;
		
		visitor.stop = visitor.visit(node.element);
		preorder(node.left, visitor);
		preorder(node.right, visitor);
	}
	

	//----------中序遍历Inorder Traversal---------------
	//中序遍历左子树--->根节点--->中序遍历右子树
	public void inorder(Visitor<E> visitor) {
		if (visitor == null) return;
		inorder(root, visitor);
	}
	private void inorder(Node<E> node, Visitor<E> visitor) {
		if (node == null || visitor.stop) return;
		
		inorder(node.left, visitor);
		if (visitor.stop) return;
		visitor.stop = visitor.visit(node.element);
		inorder(node.right, visitor);
	}
	

	//----------后序遍历Postorder Traversal---------------
	//后序遍历左子树--->后序遍历右子树--->根节点
	public void postorder(Visitor<E> visitor) {
		if (visitor == null) return;
		postorder(root, visitor);
	}
	private void postorder(Node<E> node, Visitor<E> visitor) {
		if (node == null || visitor.stop) return;
		
		postorder(node.left, visitor);
		postorder(node.right, visitor);
		if (visitor.stop) return;
		visitor.stop = visitor.visit(node.element);
	}
	

	//---------层序遍历LevelOrder Traversal-------
	// 从上到下、从左到右依次访问每一个节点
	// 规律就是循环进行下面3个操作:1.取出队头 2.左节点入队 3.右节点入队
	public void levelOrder(Visitor<E> visitor) {
		if (root == null || visitor == null) return;
		
		Queue<Node<E>> queue = new LinkedList<>();
		//根节点 入队列
		queue.offer(root);
		
		while (!queue.isEmpty()) {
			//取出队头后，删除该元素，队头向后移1位
			Node<E> node = queue.poll();
			if (visitor.visit(node.element)) return;
			
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
	


	//-----判断是否是完全二叉树----------
	//使用层序遍历 来判断
	public boolean isComplete() {
		if (root == null) return false;
		
		Queue<Node<E>> queue = new LinkedList<>();
		queue.offer(root);

		boolean leaf = false;
		while (!queue.isEmpty()) {
			Node<E> node = queue.poll();
			if (leaf && !node.isLeaf()) return false;
			
			if (node.left != null) {
				queue.offer(node.left);
			} else if (node.right != null) { // node.left == null && node.right != null
				return false;
			}
			
			if (node.right != null) {
				queue.offer(node.right);
			} else { // node.right == null
				leaf = true;
			}
		}
		
		return true;
	}

	
	//-------------计算二叉树的高度(从根节点到最远节点的层数)-------------
	//使用层序遍历的方法，一层一层向下遍历
	public int height() {
		if (root == null) return 0;
		
		// 树的高度
		int height = 0;
		// 存储着每一层的元素数量
		int levelSize = 1;
		Queue<Node<E>> queue = new LinkedList<>();
		queue.offer(root);//根节点入队
		
		while (!queue.isEmpty()) {
			Node<E> node = queue.poll();//出队 取出队头后删除，队头向后移动1位
			levelSize--;//当前层的数量减1，直到0，接着访问下一层，继续递减
			
			//左子节点入队
			if (node.left != null) {
				queue.offer(node.left);
			}
			//右子节点入队
			if (node.right != null) {
				queue.offer(node.right);
			}

			// 意味着即将要访问下一层
			if (levelSize == 0) { 
				levelSize = queue.size();//获得下一层的元素数量
				height++;//每走一层 高度+1
			}
		}
		
		return height;
	}

	//------计算指定节点的高度（指定节点到最远子节点的层次）---------------
	public int SpecialHeight(E element) {
		Node<E> node = node(element);
		return tempHeight(node);
	} 
	private int tempHeight(Node<E> node) {
		if (node == null) return 0;
		return 1 + Math.max(tempHeight(node.left), tempHeight(node.right));
	}
	

	
	@SuppressWarnings("unused")
	private Node<E> predecessor(Node<E> node) {
		if (node == null) return null;
		
		// 前驱节点在左子树当中（left.right.right.right....）
		Node<E> p = node.left;
		if (p != null) {
			while (p.right != null) {
				p = p.right;
			}
			return p;
		}
		
		// 从父节点、祖父节点中寻找前驱节点
		while (node.parent != null && node == node.parent.left) {
			node = node.parent;
		}

		// node.parent == null
		// node == node.parent.right
		return node.parent;
	}
	
	private Node<E> successor(Node<E> node) {
		if (node == null) return null;
		
		// 前驱节点在左子树当中（right.left.left.left....）
		Node<E> p = node.right;
		if (p != null) {
			while (p.left != null) {
				p = p.left;
			}
			return p;
		}
		
		// 从父节点、祖父节点中寻找前驱节点
		while (node.parent != null && node == node.parent.right) {
			node = node.parent;
		}

		return node.parent;
	}
	
	//---------定义一个对外的接口，使外部能在遍历的过程中自定义操作，并且控制便利是否结束---------
	public static abstract class Visitor<E> {
		boolean stop;
		/**
		 * @return 如果返回true，就代表停止遍历
		 */
		public abstract boolean visit(E element);
	}


	//---------定义node节点-----------
	private static class Node<E> {
		E element;
		Node<E> left;
		Node<E> right;
		Node<E> parent;
		public Node(E element, Node<E> parent) {
			this.element = element;
			this.parent = parent;
		}
		
		public boolean isLeaf() {
			return left == null && right == null;
		}
		
		public boolean hasTwoChildren() {
			return left != null && right != null;
		}
	}




	
	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		toString(root, sb, "");
		return sb.toString();
	}
	
	private void toString(Node<E> node, StringBuilder sb, String prefix) {
		if (node == null) return;

		toString(node.left, sb, prefix + "L---");
		sb.append(prefix).append(node.element).append("\n");
		toString(node.right, sb, prefix + "R---");
	}
	

	//--------判断两个节点的大小---------
	// 返回值等于0，代表e1和e2相等；
	// 返回值大于0，代表e1大于e2；
	// 返回值小于于0，代表e1小于e2

	private int compare(E e1, E e2) {
		if (comparator != null) {
			return comparator.compare(e1, e2);
		}
		return ((Comparable<E>)e1).compareTo(e2);
	}
	
	
	private void elementNotNullCheck(E element) {
		if (element == null) {
			throw new IllegalArgumentException("element must not be null");
		}
	}





	@Override
	public Object root() {
		return root;
	}

	@Override
	public Object left(Object node) {
		return ((Node<E>)node).left;
	}

	@Override
	public Object right(Object node) {
		return ((Node<E>)node).right;
	}

	@Override
	public Object string(Object node) {
		Node<E> myNode = (Node<E>)node;
		String parentString = "null";
		if (myNode.parent != null) {
			parentString = myNode.parent.element.toString();
		}
		return myNode.element + "_p(" + parentString + ")";
	}
}
