package jeason.b树形结构.a二叉树.Printer工具类.base;

public interface BinaryTreeInfoProtocol {
	/**
	 * 获取根节点
	 */
	Object root();
	/**
	 * 获取左子节点
	 */
	Object left(Object node);
	/**
	 * 获取右子节点
	 */
	Object right(Object node);
	/**
	 * 打印当前节点信息
	 */
	Object string(Object node);
}