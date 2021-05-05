package jeason.a线性表.b链表.common;


//抽离一个公共父类
//1.abstract抽象类在java是可以不用实现interface(protocol)的所有放啊
//2.implements等同于在ios中实现protocol的delegate一样
public abstract class AbstractList<E> implements ListProtocol<E>  {
	//元素的数量
	protected int size;
	
	//------------------公共方法------------------
	/** 获取元素的数量 */
	public int size() {
		return size;
	}

	/** 是否为空 */
	public boolean isEmpty() {
		return size == 0;
	}

	/** 是否包含某个元素 */
	public boolean contains(E element) {
		return indexOf(element) != ELEMENT_NOT_FOUND;
	}

	/** 添加元素到尾部 */
	public void add(E element) {
		add(size, element);
	}
	

	//------------------同包/子类 能方法------------------
	protected void outOfBounds(int index) {
		throw new IndexOutOfBoundsException("Index:" + index + ", Size:" + size);
	}
	
	protected void rangeCheck(int index) {
		if (index < 0 || index >= size) {
			outOfBounds(index);
		}
	}
	
	protected void rangeCheckForAdd(int index) {
		if (index < 0 || index > size) {
			outOfBounds(index);
		}
	}
}
