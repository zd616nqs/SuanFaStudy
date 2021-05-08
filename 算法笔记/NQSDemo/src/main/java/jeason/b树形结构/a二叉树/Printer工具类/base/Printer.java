package jeason.b树形结构.a二叉树.Printer工具类.base;

public abstract class Printer {	
	/**
	 * 二叉树的基本信息
	 */
	protected BinaryTreeInfoProtocol tree;
	
	public Printer(BinaryTreeInfoProtocol tree) {
		this.tree = tree;
	}
	
	/**
	 * 生成打印的字符串
	 */
	public abstract String printString();
	
	/**
	 * 打印后换行
	 */
	public void println() {
		print();
		System.out.println();
	}
	
	/**
	 * 打印
	 */
	public void print() {
		System.out.print(printString());
	}
}
