package jeason.a线性表.d队列;
import jeason.a线性表.b链表.双向链表.LinkList普通双向链表;


//单端队列：头部移除、尾部添加
public class DeQueue双端队列<E> {

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

	//----首部入队列：首部添加--------
	public void enQueueFront(E element) {
		list.add(0, element);
	}
	//----首部出队列：首部删除--------
	public E deQueueFront() {
		return list.remove(0);
	}

	//----尾部入队列：尾部添加--------
	public void enQueueRear(E element) {
		list.add(element);
	}
	//----尾部出队列：尾部删除--------
	public E deQueueRear() {
		return list.remove(list.size() - 1);
	}
	

	//----获取队列首个元素--------
	public E front() {
		return list.get(0);
	}

	//----获取队列尾部元素--------
	public E rear() {
		return list.get(list.size() - 1);
	}


}
