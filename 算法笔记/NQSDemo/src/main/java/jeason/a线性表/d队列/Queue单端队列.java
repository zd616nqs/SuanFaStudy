package jeason.a线性表.d队列;
import jeason.a线性表.b链表.双向链表.LinkList普通双向链表;


//单端队列：头部移除、尾部添加
public class Queue单端队列<E> {

	LinkList普通双向链表<E> list = new LinkList普通双向链表<E>();

	//----获取队列长度--------
	public int size() {
		return list.size();
	}

	//----队列是否为空--------
	public boolean isEmpty() {
		return list.isEmpty();
	}

	//----清空队列--------
	public void clear() {
		list.clear();
	}
	//----入队列：将元素添加到队列尾部--------
	public void enQueue(E element) {
		list.add(element);
	}

	//----出队列：删除队列首部元素--------
	public E deQueue() {
		return list.remove(0);
	}

	//----获取队列首个元素--------
	public E front() {
		return list.get(0);
	}


}
