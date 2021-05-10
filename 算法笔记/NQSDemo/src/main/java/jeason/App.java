package jeason;

import jeason.TimeTool.Task;
import jeason.a线性表.a动态数组.*;
import jeason.a线性表.b链表.*;
import jeason.a线性表.c栈.*;
import jeason.a线性表.d队列.*;
import jeason.b树形结构.a二叉搜索树.Main005;

public class App 
{
    public static void main( String[] args ) {
        
        TimeTool.check("开始执行代码", new Task() {
			public void execute() {
                
                //************************线性表*******************
                //----动态数组---------
                Main001.run(false);

                //-----链表----------
                Main002.run(false);

                //-----栈----------
                Main003.run(false);
                //-----队列----------
                Main004.run(false);

                //***********************树形结构********************
                //----二叉搜索树-------
                Main005.run(true);

			}
		});


    }
}
