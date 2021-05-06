package jeason.a线性表.b链表;


import java.util.List;

import jeason.a线性表.b链表.common.ListProtocol;
import jeason.a线性表.b链表.单向链表.LinkList普通链表;
import jeason.a线性表.b链表.单向链表.LinkList动态扩容缩容链表;
import jeason.a线性表.b链表.双向链表.LinkList普通双向链表;
import jeason.a线性表.b链表.循环链表.LinkList单向循环链表;
import jeason.a线性表.b链表.循环链表.LinkList双向循环链表;

public class Main002 {

	public static void run(boolean execute) {

		if (!execute) {
			return;
		}


		//---------------单向链表----------
		//普通单向链表的实现
		test1(true);
		//动态扩容缩容单向链表
		test2(true);

		//---------------双向链表----------
		//普通双向链表
		test3(true);

		//----------循环链表(单向+双向)------------
		//单向循环链表
		test4(true);
		//双向循环链表
		test5(true);
	}

	//普通单向链表的实现
	private static void test1(boolean isWork) {
		if(!isWork) return;

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
	private static void test2(boolean isWork) {
		if(!isWork) return;

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
	private static void test3(boolean isWork) {
		if(!isWork) return;

		ListProtocol<Object> list3 =  new LinkList普通双向链表<>();
		list3.add(11);
		list3.add(22);
		list3.add(33);
		list3.add(44);
		list3.add(55);
		list3.add(66);
		list3.add(77);
		System.out.println(list3);
		list3.remove(list3.indexOf(55));
		System.out.println(list3);
		// size=7, [(null)_11_(22), (11)_22_(33), (22)_33_(44), (33)_44_(55), (44)_55_(66), (55)_66_(77), (66)_77_(null)]
		// size=6, [(null)_11_(22), (11)_22_(33), (22)_33_(44), (33)_44_(66), (44)_66_(77), (66)_77_(null)]
	}
	

	//单向循环链表
	private static void test4(boolean isWork) {
		if(!isWork) return;

		ListProtocol<Object> list4 =  new LinkList单向循环链表<>();
		list4.add(11);//等效list4.add(0, 11)
		list4.add(22);//等效list4.add(1, 22)
		list4.add(33);//等效list4.add(2, 33)
		list4.add(44);//等效list4.add(3, 44)clear
		System.out.println(list4);
		list4.add(0, 673);
		System.out.println(list4);
		// size=4, [11_22, 22_33, 33_44, 44_11]
		// size=5, [673_11, 11_22, 22_33, 33_44, 44_673]
	}



	//双向循环链表
	private static void test5(boolean isWork) {
		if(!isWork) return;

		ListProtocol<Object> list5 =  new LinkList双向循环链表<>();
		System.out.println(list5);
	}
}
