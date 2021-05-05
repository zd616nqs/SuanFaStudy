package jeason.a线性表.a动态数组;


public class Main001 {

	public static void run() {

		// java.util.ArrayList;


		ArrayList<Object> list  = new ArrayList<>();
		list.add(10);
		list.add(new Person(10, "Jack"));
		list.add(22);
		list.indexOf(new Person(10, "Jack"));
		System.out.println("打印的数组：" + list);


		ArrayList<Object> persons  = new ArrayList<>();
		persons.add(new Person(10, "Jack"));
		persons.add(null);
		persons.add(new Person(15, "Rose"));
		persons.add(null);
		persons.add(new Person(12, "James"));
		persons.add(null);
		System.out.println("找到的下标：" + persons.indexOf(null));
	}

	static void test() {
		// int -> Integer
	
		// 所有的类，最终都继承java.lang.Object

		// new是向堆空间申请内存
		ArrayList<Person> persons  = new ArrayList<>();
		persons.add(new Person(10, "Jack"));
		persons.add(new Person(12, "James"));
		persons.add(new Person(15, "Rose"));
		persons.clear();
		persons.add(new Person(22, "abc"));
		
		System.out.println(persons);
		ArrayList<Integer> ints  = new ArrayList<>();
		ints.add(10);
		ints.add(10);
		ints.add(22);
		ints.add(33);
		System.out.println(ints);
	}
}
