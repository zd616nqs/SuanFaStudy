package jeason.a线性表.d队列;

public class Main004 {

	public static void run(boolean execute) {

		if (!execute) {
			return;
		}
		//-----------非循环队列(线性增加和删除)------------
		//1.单端队列：头部移除、尾部添加（使用普通双向链表实现）
		test1(false);
		
		//2.双端队列：头尾都能添加和删除元素
		test2(false);


		//------------循环队列(front指针会循环绕回去)----------
		//3.循环单端队列：只能队头添加、队尾删除
		//添加后 动态扩容但队头不变
		//删除后 容量变小，并且队头指向向后走1位，到最大容量处返回零重新循环
		test3(false);

		//4.循环双端队列：队头和队尾都能 添加和删除
		test4(true);
	
	}

	
	//单端队列：头部移除、尾部添加（使用普通双向链表实现）
	private static void test1(boolean isWork) {
		if(!isWork) return;

		Queue单端队列<Integer> queue1 = new Queue单端队列<Integer>();
		queue1.enQueue(11);
		queue1.enQueue(22);
		queue1.enQueue(33);
		queue1.enQueue(44);
		queue1.enQueue(55);

		//出队列是先入先出的原则
		while(!queue1.isEmpty()){
			Integer temp =  queue1.deQueue();
			System.out.println(temp);
		}
		/**
		 * 11
		 * 22
		 * 33
		 * 44
		 * 55
		 */

	}





	//双端队列：头尾都能添加和删除元素
	private static void test2(boolean isWork) {
		if(!isWork) return;
		DeQueue双端队列<Integer> queue2 = new DeQueue双端队列<Integer>();

		queue2.enQueueFront(11);
		queue2.enQueueFront(22);
		queue2.enQueueRear(55);
		queue2.enQueueRear(66);
		System.out.println(queue2); 
		/* 尾部 66 55  11 22 头部 */


		while(!queue2.isEmpty()){
			Integer temp =  queue2.deQueueRear();
			System.out.println(temp);
		}
		// 66 55 11 22
	}


	//循环单端队列：只能队头添加、队尾删除
	//添加后 动态扩容但队头不变
	//删除后 容量变小，并且队头指向向后走1位，到最大容量处返回零重新循环
	private static void test3(boolean isWork) {
		if(!isWork) return;

		//------初始容量10-------
		CircleQueue循环单端队列<Integer> queue3 = new CircleQueue循环单端队列<Integer>();


		//-------初始入队操作-------
		for (int a = 0; a < 10; a++) {
			queue3.enQueue(a);
		}
		System.out.println(queue3);
		// 总容量=10 占用容量=10 队头front指向=0, 
		// 头[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]尾

		//-------——扩容操作---------
		for (int b = 90; b < 93; b++) {
			queue3.enQueue(b);
		}
		System.out.println(queue3);
		// 总容量=15 占用容量=10 队头front指向=3, 
		// 头[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 90, 91, 92, null, null]尾


		//--------出队操作，队头发生移动--------
		for (int c = 0; c < 3; c++) {
			queue3.deQueue();
		}
		System.out.println(queue3);
		// 总容量=15 占用容量=10 队头front指向=3, 
		// 头[null, null, null, 3, 4, 5, 6, 7, 8, 9, 90, 91, 92, null, null]尾
		
		//------再次入队操作-------
		for (int d = 673; d < 677; d++) {
			queue3.enQueue(d);
		}
		System.out.println(queue3);
		// 总容量=15 占用容量=14 队头front指向=3, 
		// 头[675, 676, null, 3, 4, 5, 6, 7, 8, 9, 90, 91, 92, 673, 674]尾

		//----接着入队，会进行扩容
		//----扩容时会重新排序队列，把真正的front放到队首
		//----先扩容，再执行入队，新入队的数据接着在队尾添加
		for (int e = 880; e < 885; e++) {
			queue3.enQueue(e);
		}
		System.out.println(queue3);
		// 总容量=22 占用容量=19 队头front指向=0, 
		// 头[3, 4, 5, 6, 7, 8, 9, 90, 91, 92, 673, 674, 675, 676, 880, 881, 882, 883, 884, null, null, null]尾
	}



	//4.循环双端队列：队头和队尾都能 添加和删除
	private static void test4(boolean isWork) {
		if(!isWork) return;

		//------初始容量10-------
		CircleQueue循环双端队列<Integer> queue4 = new CircleQueue循环双端队列<Integer>();

		//初始值88
		queue4.enQueueFront(88);

		for (int a = 1; a <= 5; a++) {
			queue4.enQueueFront(a);//头部入队
			queue4.enQueueRear(100+a);//尾部入队 动态扩容
			System.out.println(queue4.front());
		}
		System.out.println(queue4);
		// 总容量=15 占用容量=11 队头front指向=0, 
		// 头[5, 4, 3, 2, 1, 88, 101, 102, 103, 104, 105, null, null, null, null]尾

		//-------头部入队，循环队列会把添加的数据放到扩容后的队尾的index位置
		//-------尾部入队，接着上次尾部的index往后添加数据
		queue4.enQueueFront(666);//头部入队
		queue4.enQueueRear(888);//尾部入队
		System.out.println(queue4);
		// 总容量=15 占用容量=13 队头front指向=14, 
		// 头[5, 4, 3, 2, 1, 88, 101, 102, 103, 104, 105, 888, null, null, 666]尾

		//---接着入队，放满队列
		queue4.enQueueFront(1992);
		queue4.enQueueFront(1993);
		System.out.println(queue4);
		// 总容量=15 占用容量=15 队头front指向=12, 
		// 头[5, 4, 3, 2, 1, 88, 101, 102, 103, 104, 105, 888, 1993, 1992, 666]尾



		//----接着入队，会进行扩容
		//----扩容时会重新排序队列，把真正的front放到队首
		//----先扩容，再执行入队，所以新入队的数据又被放到扩容后的队列的最后index位置了
		queue4.enQueueFront(1994);
		System.out.println(queue4);
		// 总容量=22 占用容量=16 队头front指向=21, 
		// 头[1993, 1992, 666, 5, 4, 3, 2, 1, 88, 101, 102, 103, 104, 105, 888, null, null, null, null, null, null, 1994]尾


	}
	
}
