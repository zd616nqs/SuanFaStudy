package jeason.a线性表.b链表;


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
		test2(false);

		//---------------双向链表----------
		//普通双向链表
		test3(false);

		//----------循环链表(单向+双向)------------
		//单向循环链表
		test4(false);
		//双向循环链表
		test5(false);

		//解决约瑟夫问题:使用循环链表就能实现(单向和双向都可以)
		test6(false);
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
		// size=4, [11_(next:22), 22_(next:33), 33_(next:44), 44_(next:11)]
		// size=5, [673_(next:11), 11_(next:22), 22_(next:33), 33_(next:44), 44_(next:673)]
	}



	//双向循环链表
	private static void test5(boolean isWork) {
		if(!isWork) return;

		ListProtocol<Object> list5 =  new LinkList双向循环链表<>();
		list5.add(11);//等效list5.add(0, 11)
		list5.add(22);//等效list5.add(1, 22)
		list5.add(33);//等效list5.add(2, 33)
		list5.add(44);//等效list5.add(3, 44)clear
		System.out.println(list5);
		list5.add(0,673);
		System.out.println(list5);
		list5.add(list5.indexOf(33),1992);
		System.out.println(list5);
		// size=4, [(44)_11_(22), (11)_22_(33), (22)_33_(44), (33)_44_(11)]
		// size=5, [(44)_673_(11), (673)_11_(22), (11)_22_(33), (22)_33_(44), (33)_44_(673)]
		// size=6, [(44)_673_(11), (673)_11_(22), (11)_22_(1992), (22)_1992_(33), (1992)_33_(44), (33)_44_(673)]

	}



	// 解决约瑟夫问题:使用循环链表就能实现(单向和双向都可以)
	//问题：约瑟夫问题 8个人每人一个序号站成一圈，从1开始数数，数到3死掉一个人，下一个人接着从1开始数
	//期望：求出最后一个幸存者的序号是多少
	private static void test6(boolean isWork) {
		if(!isWork) return;
		// current: 用于指向某个节点
		// reset:   让current指向头节点first
		// next:    让current往后走一步，也就是current=current.next
		// remove:  删除current指向的节点，删除成功后让current指向下一个节点
		LinkList双向循环链表<Object> list6 =  new LinkList双向循环链表<>();
		list6.add(111);
		list6.add(222);
		list6.add(333);
		list6.add(444);
		list6.add(555);
		list6.add(666);
		list6.add(777);
		list6.add(888);

		list6.reset();
		while (!list6.isEmpty()){
			//remove后会移动一次，所以数三次，移动2次
			list6.next();
			list6.next();
			Object deleteNode = list6.remove();
			System.out.println("delete的元素："+deleteNode);
			System.out.println("剩下的元素："+list6);
			System.out.println("---------------------");
		} 

		/** 
		delete的元素：333
		剩下的元素：size=7, [(888)_111_(222), (111)_222_(444), (222)_444_(555), (444)_555_(666), (555)_666_(777), (666)_777_(888), (777)_888_(111)]
		---------------------
		delete的元素：666
		剩下的元素：size=6, [(888)_111_(222), (111)_222_(444), (222)_444_(555), (444)_555_(777), (555)_777_(888), (777)_888_(111)]
		---------------------
		delete的元素：111
		剩下的元素：size=5, [(888)_222_(444), (222)_444_(555), (444)_555_(777), (555)_777_(888), (777)_888_(222)]
		---------------------
		delete的元素：555
		剩下的元素：size=4, [(888)_222_(444), (222)_444_(777), (444)_777_(888), (777)_888_(222)]
		---------------------
		delete的元素：222
		剩下的元素：size=3, [(888)_444_(777), (444)_777_(888), (777)_888_(444)]
		---------------------
		delete的元素：888
		剩下的元素：size=2, [(777)_444_(777), (444)_777_(444)]
		---------------------
		delete的元素：444
		剩下的元素：size=1, [(777)_777_(777)]
		---------------------
		delete的元素：777
		剩下的元素：size=0, []
		---------------------
		*/


	}
}
