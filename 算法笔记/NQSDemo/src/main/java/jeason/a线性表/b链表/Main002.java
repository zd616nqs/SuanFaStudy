package jeason.a线性表.b链表;

import java.util.LinkedList;
import java.util.List;

public class Main002 {

	public static void run() {

		List<Integer> list1 =  new LinkedList<>();
		list1.add(10);
		list1.add(20);
		list1.add(30);
		list1.add(40);
		list1.add(50);
		list1.remove(2);//删除下标2的node节点
		System.out.println(list1);//[10, 20, 40, 50]
		
		
	}
}
