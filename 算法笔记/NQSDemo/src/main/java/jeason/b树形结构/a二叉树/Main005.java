package jeason.b树形结构.a二叉树;
import java.util.Comparator;

import jeason.b树形结构.a二叉树.Printer工具类.*;
// import jeason.b树形结构.a二叉树.Files工具类.Files;
import jeason.b树形结构.a二叉树.BinarySearchTree二叉搜索树.Visitor;;

public class Main005 {

	public static void run(boolean execute) {

		if (!execute) {
			return;
		}
		
		//----简单的添加数字到二叉树中------
		test1(false);

		//----从小到大、从大到小放入二叉树------
		test2(false);

		//----数据源随机，观察生成的二叉树-------
		test3(false);

		//-------将自定义Person进行二叉树比较--------
		test4(false);

		//--------各种遍历方式----------
		//-----------前序遍历：根节点--->前序遍历左子树--->前序遍历右子树
		//-----------中序遍历：遍历左子树--->根节点--->中遍历右子树
		//-----------后序遍历：遍历左子树--->遍历右子树--->根节点
		//-----------层序遍历：从上到下、从左到右依次访问每一个节点
		test5(false);

		//-----获取二叉树的高度(根节点开始、指定节点开始)------
		test6(false);

		//------判断是否是完全二叉树-----------
		test7(true);


	}

	

	//----简单的添加数字到二叉树中------
    static void test1(boolean isWork) {
		if(!isWork) return;

		Integer data[] = new Integer[] {
			7, 4, 9, 2, 5, 8, 11, 3, 12, 1
		};
	
		BinarySearchTree二叉搜索树<Integer> bst = new BinarySearchTree二叉搜索树<>();
		for (int i = 0; i < data.length; i++) {
			bst.add(data[i]);
		}
		BinaryTrees.println(bst);
		/** 
             ┌───7_p(null)───┐
             │               │
        ┌─4_p(7)─┐       ┌─9_p(7)─┐
        │        │       │        │
   ┌─2_p(4)─┐  5_p(4) 8_p(9)   11_p(9)─┐
   │        │                          │
1_p(2)    3_p(2)                    12_p(11)
		*/
	}








	//----从小到大、从大到小放入二叉树------
	static void test2(boolean isWork) {
		if(!isWork) return;

		//---情况1：默认数字小的放在二叉树前面
		Integer data[] = new Integer[] {
			7, 4, 9, 2, 5, 8, 11, 3, 12, 1
		};
	
		BinarySearchTree二叉搜索树<Person> bst1 = new BinarySearchTree二叉搜索树<>();
		for (int i = 0; i < data.length; i++) {
			bst1.add(new Person(data[i]));
		}
		
		BinaryTrees.println(bst1);
		
		//---情况2：定义数字大的放在二叉树前面
		BinarySearchTree二叉搜索树<Person> bst2 = new BinarySearchTree二叉搜索树<>(new Comparator<Person>() {
			public int compare(Person o1, Person o2) {
				return o2.getAge() - o1.getAge();
			}
		});
		for (int i = 0; i < data.length; i++) {
			bst2.add(new Person(data[i]));
		}
		BinaryTrees.println(bst2);

/*
                            ┌───────────7_null_p(null)──────────┐
                            │                                   │
                  ┌─4_null_p(7_null)─┐                 ┌─9_null_p(7_null)─┐
                  │                  │                 │                  │
        ┌─2_null_p(4_null)─┐  5_null_p(4_null) 8_null_p(9_null)   11_null_p(9_null)─┐
        │                  │                                                        │
1_null_p(2_null)    3_null_p(2_null)                                        12_null_p(11_null)
                             ┌───────────7_null_p(null)──────────┐
                             │                                   │
                   ┌─9_null_p(7_null)─┐                 ┌─4_null_p(7_null)─┐
                   │                  │                 │                  │
         ┌─11_null_p(9_null)   8_null_p(9_null) 5_null_p(4_null)  ┌─2_null_p(4_null)─┐
         │                                                        │                  │
12_null_p(11_null)                                        3_null_p(2_null)    1_null_p(2_null) 
*/
	}


	//----数据源随机，观察生成的二叉树-------
	static void test3(boolean isWork) {
		if(!isWork) return;
		BinarySearchTree二叉搜索树<Integer> bst = new BinarySearchTree二叉搜索树<>();
		for (int i = 0; i < 40; i++) {
			bst.add((int)(Math.random() * 100));
		}
		
		// String str = BinaryTrees.printString(bst);
		// str += "\n";

		BinaryTrees.println(bst);

		// Files.writeToFile("F:/1.txt", str, true);
		
	}


	//-------将自定义Person进行二叉树比较--------
	static void test4(boolean isWork) {
		if(!isWork) return;
		BinarySearchTree二叉搜索树<Person> bst = new BinarySearchTree二叉搜索树<>();
		bst.add(new Person(10, "jack"));
		bst.add(new Person(12, "rose"));
		bst.add(new Person(6, "jim"));
		bst.add(new Person(10, "michael"));
		
		BinaryTrees.println(bst);
/*
         ┌─10_michael_p(null)─┐
         │                    │
6_jim_p(10_michael) 12_rose_p(10_michael)

*/
	}


	//--------各种遍历方式----------
	//-----------前序遍历：根节点--->前序遍历左子树--->前序遍历右子树
	//-----------中序遍历：遍历左子树--->根节点--->中遍历右子树
	//-----------后序遍历：遍历左子树--->遍历右子树--->根节点
	//-----------层序遍历：从上到下、从左到右依次访问每一个节点
	static void test5(boolean isWork) {

		if(!isWork) return;
		Integer data[] = new Integer[] {
			7,4,2,1,3,5,9,8,11,10,12
		};
	
		BinarySearchTree二叉搜索树<Integer> bst = new BinarySearchTree二叉搜索树<>();
		for (int i = 0; i < data.length; i++) {
			bst.add(data[i]);
		}
		BinaryTrees.println(bst);
		
		//-----------前序遍历Preorder Traversal----------
		//根节点--->前序遍历左子树--->前序遍历右子树
		System.out.print("前序遍历:开始 ");
		bst.preorder(new Visitor<Integer>() {
			public boolean visit(Integer element) {
				System.out.print(element + " ");
				// return element == 2 ? true : false;
				return false;
			}
		});
		System.out.println("结束\n");
		
		//----------中序遍历Inorder Traversal---------------
		//中序遍历左子树--->根节点--->中序遍历右子树
		System.out.print("中序遍历:开始 ");
		bst.inorder(new Visitor<Integer>() {
			public boolean visit(Integer element) {
				System.out.print(element + " ");
				// return element == 4 ? true : false;
				return false;
			}
		});
		System.out.println("结束\n");
		
		//----------后序遍历Postorder Traversal---------------
		//后序遍历左子树--->后序遍历右子树--->根节点
		System.out.print("后序遍历:开始 ");
		bst.postorder(new Visitor<Integer>() {
			public boolean visit(Integer element) {
				System.out.print(element + " ");
				// return element == 4 ? true : false;
				return false;
			}
		});
		System.out.println("结束\n");
		
		//---------层序遍历LevelOrder Traversal-------
		// 从上到下、从左到右依次访问每一个节点
		System.out.print("层序遍历:开始 ");
		bst.levelOrder(new Visitor<Integer>() {
			public boolean visit(Integer element) {
				System.out.print(element + " ");
				// return element == 9 ? true : false;
				return false;
			}
		});
		System.out.println("结束\n");
//     ┌──7──┐
//     │     │
//   ┌─4─┐ ┌─9─┐
//   │   │ │   │
// ┌─2─┐ 5 8 ┌─11─┐
// │   │     │    │
// 1   3    10    12
// 前序遍历:开始 7 4 2 1 3 5 9 8 11 10 12 结束
// 中序遍历:开始 1 2 3 4 5 7 8 9 10 11 12 结束
// 后序遍历:开始 1 3 2 5 4 8 10 12 11 9 7 结束
// 层序遍历:开始 7 4 9 2 5 8 11 1 3 10 12 结束

	}






	static void test6(boolean isWork) {
		if(!isWork) return;
		Integer data[] = new Integer[] {
			7,4,2,1,3,5,9,8,11,10,12
		};
	
		BinarySearchTree二叉搜索树<Integer> bst = new BinarySearchTree二叉搜索树<>();
		for (int i = 0; i < data.length; i++) {
			bst.add(data[i]);
		}
		BinaryTrees.println(bst);
		System.out.println("二叉树的高度："+bst.height());
		System.out.println("节点2的高度："+bst.SpecialHeight(2));

//     ┌──7──┐
//     │     │
//   ┌─4─┐ ┌─9─┐
//   │   │ │   │
// ┌─2─┐ 5 8 ┌─11─┐
// │   │     │    │
// 1   3    10    12
// 二叉树的高度：4
// 节点2的高度：2

	}


	static void test7(boolean isWork) {
		if(!isWork) return;
		Integer data[] = new Integer[] {
			7,4,2,1,3,5,9,8,11,10,12
		};
	
		BinarySearchTree二叉搜索树<Integer> bst = new BinarySearchTree二叉搜索树<>();
		for (int i = 0; i < data.length; i++) {
			bst.add(data[i]);
		}
		BinaryTrees.println(bst);
		System.out.println("是否是完整二叉树："+bst.isComplete());
	}


	
	
}
