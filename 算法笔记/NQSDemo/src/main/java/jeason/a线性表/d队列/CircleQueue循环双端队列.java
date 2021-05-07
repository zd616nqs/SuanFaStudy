package jeason.a线性表.d队列;



@SuppressWarnings("unchecked")
public class CircleQueue循环双端队列<E> {
	private int front;//
	private int size;
	private E[] elements;
	private static final int DEFAULT_CAPACITY = 10;
	
	public CircleQueue循环双端队列() {
		elements = (E[]) new Object[DEFAULT_CAPACITY];
	}
	
	//----指定队头移动的步数(正数向后移动，负数向前移动，到达边界时切换到另外一个边界)--------
	private int index(int index) {
		index += front;
		if (index < 0) {
			//到达左边界，移动到右边界
			return index + elements.length;
		}else {
			int moveStep = 0;
			if(index >= elements.length){
				//到达右边界，移动到左边界
				moveStep = elements.length;
			}else {
				//正常左右移动，不需要操作边界值
				moveStep = 0;
			}
			
			return index - moveStep;
		}
	}

	/**
	 * 从头部入队
	 * @param element
	 */
	public void enQueueFront(E element) {
		ensureCapacity(size + 1);
		//front指向向左移动1位
		front = index(-1);
		//头部存入数据
		elements[front] = element;
		size++;
	}

	/**
	 * 从头部出队
	 * @param element
	 */
	public E deQueueFront() {
		E frontElement = elements[front];
		elements[front] = null;
		//front指向向右移动1位
		front = index(1);
		size--;
		return frontElement;
	}

	

	/**
	 * 从尾部入队
	 * @param element
	 */
	public void enQueueRear(E element) {
		ensureCapacity(size + 1);
		//向队尾插入数据
		elements[index(size)] = element;
		size++;
	}
	/**
	 * 从尾部出队
	 * @param element
	 */
	public E deQueueRear() {
		//找出真正的队尾的元素
		int rearIndex = index(size - 1);
		E rear = elements[rearIndex];
		//删除队尾的元素
		elements[rearIndex] = null;
		size--;
		return rear;
	}

	public E front() {
		return elements[front];
	}

	public E rear() {
		return elements[index(size - 1)];
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



	public int size() {
		return size;
	}

	public boolean isEmpty() {
		return size == 0;
	}

	public void clear() {
		for (int i = 0; i < size; i++) {
			elements[index(i)] = null;
		}
		front = 0;
		size = 0;
	}
}
