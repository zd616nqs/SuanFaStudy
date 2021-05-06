package jeason.a线性表.b链表;


import jeason.a线性表.b链表.common.ListProtocol;
import jeason.a线性表.b链表.单向链表.LinkList普通链表;
import jeason.a线性表.b链表.单向链表.LinkList动态扩容缩容链表;
import jeason.a线性表.b链表.双向链表.LinkList普通双向链表;

public class Main002 {

	public static void run(boolean execute) {

		if (!execute) {
			return;
		}


		//---------------单向链表----------
		//普通单向链表的实现
		// test1();
		//动态扩容缩容单向链表
		// test2();

		//---------------双向链表----------
		//普通双向链表
		test3();
	}

	//普通单向链表的实现
	private static void test1() {
		ListProtocol<Object> list1 =  new LinkList普通链表<>();
		list1.add(10);
		list1.add(20);
		list1.add(30);
		list1.add(40);
		list1.add(50);
		list1.remove(2);//删除下标2的node节点
		System.out.println(list1);//[10, 20, 40, 50]
	}


	//动态扩容缩容单向链表
	private static void test2() {
		ListProtocol<Object> list2 =  new LinkList动态扩容缩容链表<>();
		for (int i = 0; i < 30; i++) {
			//每次扩容*1.5
			list2.add(i);
		}
		for (int i = 0; i < 30; i++) {
			//每次缩容/2
			list2.remove(0);
		}
		System.out.println(list2);
		/**
		 * 10扩容为15
		 * 15扩容为22
		 * 22扩容为33
         * 33缩容为16
	     * 16缩容为8
         * size=0, []
		 */
	}

	//普通双向链表
	private static void test3() {
		ListProtocol<Object> list3 =  new LinkList普通双向链表<>();
		list3.add(11);
		list3.add(22);
		list3.add(33);
		list3.add(44);
		list3.add(55);
		list3.add(66);
		list3.add(77);
		System.out.println(list3);
		list3.remove(list3.indexOf(22));
		System.out.println(list3);
		// size=7, [(null)_11_(22), (11)_22_(33), (22)_33_(44), (33)_44_(55), (44)_55_(66), (55)_66_(77), (66)_77_(null)]
		// size=6, [(null)_11_(33), (11)_33_(44), (33)_44_(55), (44)_55_(66), (55)_66_(77), (66)_77_(null)]
	}
	
}
