package jeason.b树形结构.a二叉搜索树.Printer工具类;

public class Person implements Comparable<Person> {
	private int age;
	private String name;
	
	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public Person(int age) {
		this.age = age;
	}

	public Person(int age, String name) {
		this.age = age;
		this.name = name;
	}

	//自定义比较的规则，外面使用Comparator比较两个Person时，遵守Person内的比较规则
	@Override
	public int compareTo(Person e) {
//		if (age > e.age) return 1;
//		if (age < e.age) return -1;
//		return 0;
		return age - e.age;
	}
	
	@Override
	public String toString() {
		return age + "_" + name;
	}
	
}