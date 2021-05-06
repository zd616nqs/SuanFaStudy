package jeason.a线性表.b链表.双向链表;
import jeason.a线性表.b链表.common.AbstractList;


//继承抽象父类，实现声明的方法
public class LinkList普通双向链表<E> extends AbstractList<E> {
	private Node<E> first;
	private Node<E> last;
	
	private static class Node<E> {
		E element;//当前node节点存储的元素
		Node<E> prev;//上一个元素
		Node<E> next;//下一个元素
		//构造方法 
		public Node(Node<E> prev, E element, Node<E> next) {
			this.prev = prev;
			this.element = element;
			this.next = next;
		}
		

		//打印出来，能够直观观察链表的引用
		@Override
		public String toString() {
			StringBuilder sb = new StringBuilder();
			
			if (prev != null) {
				sb.append("("+prev.element+")");
			} else {
				sb.append("(null)");
			}
			sb.append("_").append(element).append("_");
			if (next != null) {
				sb.append("("+next.element+")");
			} else {
				sb.append("(null)");
			}
			return sb.toString();
		}
	}

	
	@Override
	public void clear() {
		//first和last的node节点置null，对应链表的所有引用都会销毁
		size = 0;
		first = null;
		last = null;
	}

	//--------------添加元素----------------
	@Override
	public void add(int index, E element) {
		rangeCheckForAdd(index);

		// size == 0
		// index == 0  
		if (index == size) { 
			//-----------往最后面添加元素----------
			//获取最后一个节点
			Node<E> oldLast = last;
			//创建当前要插入的node节点
			last = new Node<>(oldLast, element, null);
			if (oldLast == null) {
				// 这是链表添加的第一个元素 
				first = last;
			} else {
				// 插入到当前链表的最后
				oldLast.next = last;
			}
		} else {
			//-------往首个或中间添加元素------------
			Node<E> next = node(index); 
			Node<E> prev = next.prev; 
			Node<E> node = new Node<>(prev, element, next);
			next.prev = node;
			
			if (prev == null) { 
				//index == 0 插入到链表的首个位置
				first = node;
			} else {
				// 正常插入链表
				prev.next = node;
			}
		}
		
		size++;
	}


	//------------删除元素------------
	@Override
	public E remove(int index) {
		rangeCheck(index);

		Node<E> node = node(index);
		Node<E> prev = node.prev;
		Node<E> next = node.next;

		//跨过中间的node，头尾的两个node进行引用，中间的node没有引用就销毁了
		
		//------处理next节点------------
		if (prev == null) { 
			// 最开始的节点，index == 0
			first = next;
		} else {
			// 正常引用next节点
			prev.next = next;
		}
		
		//------处理prev节点------------
		if (next == null) { 
			// 最后一个节点，index == size - 1
			last = prev;
		} else {
			// 正常引用prev节点
			next.prev = prev;
		}
		
		size--;
		return node.element;
	}

	@Override
	public int indexOf(E element) {
		if (element == null) {
			Node<E> node = first;
			for (int i = 0; i < size; i++) {
				if (node.element == null) return i;
				
				node = node.next;
			}
		} else {
			Node<E> node = first;
			for (int i = 0; i < size; i++) {
				if (element.equals(node.element)) {
					return i;
				}
				node = node.next;
			}
		}
		return ELEMENT_NOT_FOUND;
	}
	
	/**
	 * 获取index位置对应的节点对象
	 * @param index
	 * @return
	 */
	private Node<E> node(int index) {
		rangeCheck(index);
		
		if (index < (size >> 1)) {
			Node<E> node = first;
			for (int i = 0; i < index; i++) {
				node = node.next;
			}
			return node;
		} else {
			Node<E> node = last;
			for (int i = size - 1; i > index; i--) {
				node = node.prev;
			}
			return node;
		}
	}




	@Override
	public E get(int index) {
		return node(index).element;
	}

	@Override
	public E set(int index, E element) {
		Node<E> node = node(index);
		E old = node.element;
		node.element = element;
		return old;
	}
	
	@Override
	public String toString() {
		StringBuilder string = new StringBuilder();
		string.append("size=").append(size).append(", [");
		Node<E> node = first;
		for (int i = 0; i < size; i++) {
			if (i != 0) {
				string.append(", ");
			}
			
			string.append(node);
			
			node = node.next;
		}
		string.append("]");
		return string.toString();
	}
}
