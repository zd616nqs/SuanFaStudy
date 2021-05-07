package jeason.a线性表.d队列;



@SuppressWarnings("unchecked")
public class CircleQueue循环单端队列<E> {
	private int front;
	private int size;
	private E[] elements;
	private static final int DEFAULT_CAPACITY = 10;
	
	//便利构造
	public CircleQueue循环单端队列() {
		elements = (E[]) new Object[DEFAULT_CAPACITY];
	}
	

	//-------入队列-----------
	public void enQueue(E element) {
		//容量不足动态扩容
		ensureCapacity(size + 1);
		
		elements[index(size)] = element;
		size++;
	}

	//-------出队列------------
	public E deQueue() {
		//获取队头指向的元素
		E frontElement = elements[front];
		//删除队头指向的元素
		elements[front] = null;
		//队头向后移动1位
		front = index(1);


		size--;
		return frontElement;
	}

	//----指定队头移动的步数(到达最大值后归零继续)--------
	private int index(int index) {
		index += front;
		int temp = (index >= elements.length ? elements.length : 0);
		return index - temp;
	}

	//-------获取队头指向的元素------
	public E front() {
		return elements[front];
	}
	



	//-------容量-----------
	public int size() {
		return size;
	}
	//-------是否为空-----------
	public boolean isEmpty() {
		return size == 0;
	}
	//-------清空重置-----------
	public void clear() {
		for (int i = 0; i < size; i++) {
			elements[index(i)] = null;
		}
		//队头和size归零
		front = 0;
		size = 0;
	}

	@Override
	public String toString() {
		StringBuilder string = new StringBuilder();
		string.append("总容量=").append(elements.length)
		.append(" 占用容量=").append(size)
		.append(" 队头front指向=").append(front)
		.append(", [");
		for (int i = 0; i < elements.length; i++) {
			if (i != 0) {
				string.append(", ");
			}
			
			string.append(elements[i]);
		}
		string.append("]");
		return string.toString();
	}
	
	
	
	/**
	 * 保证要有capacity的容量
	 * @param capacity
	 */
	private void ensureCapacity(int capacity) {
		int oldCapacity = elements.length;
		if (oldCapacity >= capacity) return;
		
		// 新容量为旧容量的1.5倍
		int newCapacity = oldCapacity + (oldCapacity >> 1);
		E[] newElements = (E[]) new Object[newCapacity];
		//扩容时，会按照队首->队尾的顺序重新排列整个队列
		for (int i = 0; i < size; i++) {
			newElements[i] = elements[index(i)];
		}
		elements = newElements;
		
		// 重置front
		front = 0;
	}
}