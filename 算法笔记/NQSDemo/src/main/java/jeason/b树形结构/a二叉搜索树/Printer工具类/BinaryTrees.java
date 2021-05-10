
package jeason.b树形结构.a二叉搜索树.Printer工具类;

import jeason.b树形结构.a二叉搜索树.Printer工具类.base.BinaryTreeInfoProtocol;
import jeason.b树形结构.a二叉搜索树.Printer工具类.base.Printer;

public final class BinaryTrees {

	private BinaryTrees() {
	}

	public static void print(BinaryTreeInfoProtocol tree) {
		print(tree, null);
	}

	public static void println(BinaryTreeInfoProtocol tree) {
		println(tree, null);
	}

	public static void print(BinaryTreeInfoProtocol tree, PrintStyle style) {
		if (tree == null || tree.root() == null) return;
		printer(tree, style).print();
	}

	public static void println(BinaryTreeInfoProtocol tree, PrintStyle style) {
		if (tree == null || tree.root() == null) return;
		printer(tree, style).println();
	}

	public static String printString(BinaryTreeInfoProtocol tree) {
		return printString(tree, null);
	}

	public static String printString(BinaryTreeInfoProtocol tree, PrintStyle style) {
		if (tree == null || tree.root() == null) return null;
		return printer(tree, style).printString();
	}

	private static Printer printer(BinaryTreeInfoProtocol tree, PrintStyle style) {
		if (style == PrintStyle.INORDER) return new InorderPrinter(tree);
		return new LevelOrderPrinter(tree);
	}

	public enum PrintStyle {
		LEVEL_ORDER, INORDER
	}
}