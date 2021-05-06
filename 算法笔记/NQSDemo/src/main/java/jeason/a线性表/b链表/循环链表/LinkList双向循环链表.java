package jeason.a线性表.b链表.循环链表;

import jeason.a线性表.b链表.common.AbstractList;


public class LinkList双向循环链表<E> extends AbstractList<E> {
	private Node<E> first;
	private Node<E> last;
	private Node<E> current; 
	
	private static class Node<E> {
		E element;
		Node<E> prev;
		Node<E> next;
		public Node(Node<E> prev, E element, Node<E> next) {
			this.prev = prev;
			this.element = element;
			this.next = next;
		}
		
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

	//---------添加元素-------------
	@Override
	public void add(int index, E element) {
		rangeCheckForAdd(index);

		// size == 0
		// index == 0
		if (index == size) { // 往最后面添加元素
			Node<E> oldLast = last;
			last = new Node<>(oldLast, element, first);
			if (oldLast == null) { 
				//-------这是链表添加的第一个元素--------
				first = last;
				first.next = first;
				first.prev = first;
			} else {
				//-------正常往最后面添加node节点------
				oldLast.next = last;
				first.prev = last;
			}
		} else {
			//------往非结尾的位置添加node节点-------
			Node<E> next = node(index); 
			Node<E> prev = next.prev; 
			Node<E> node = new Node<>(prev, element, next);
			next.prev = node;
			prev.next = node;
			
			if (next == first) { 
				// 往首部插入元素，index == 0
				first = node;
			}
		}
		
		size++;
	}

	//---------删除元素-------------
	private E remove(Node<E> node) {
		if (size == 1) {
			//-------链表只有1个元素------
			first = null;
			last = null;
		} else {
			Node<E> prev = node.prev;
			Node<E> next = node.next;
			prev.next = next;
			next.prev = prev;
			
			//删除首部： index == 0
			if (node == first) { 
				first = next;
			}
			//删除尾部：index == size - 1
			if (node == last) { 
				last = prev;
			}
		}
		
		size--;
		return node.element;
	}




	//约瑟夫问题，循环链表相关方法
	//循环链表：重置	
	public void reset() {
		current = first;
	}
	
	//循环链表：下一步
	public E next() {
		if (current == null) return null;
		
		current = current.next;
		return current.element;
	}
	
	//循环链表：删除current节点
	public E remove() {
		if (current == null) return null;
		
		Node<E> next = current.next; 
		E element = remove(current);
		if (size == 0) {
			current = null;
		} else {
			current = next;
		}
		
		return element;
	}







	@Override
	public void clear() {
		size = 0;
		first = null;
		last = null;
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
	public E remove(int index) {
		rangeCheck(index);
		return remove(node(index));
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
				if (element.equals(node.element)) return i;
				
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
