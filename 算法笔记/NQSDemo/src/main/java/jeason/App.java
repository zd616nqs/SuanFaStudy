package jeason;

import jeason.TimeTool.Task;
import jeason.a线性表.a动态数组.*;
import jeason.a线性表.b链表.*;

public class App 
{
    public static void main( String[] args ) {
        
        TimeTool.check("测试", new Task() {
			public void execute() {
                System.out.println( "哈哈哈");
			}
		});


        //************************线性表*******************
        //----动态数组---------
        // Main001.run();

        //-----链表----------
        Main002.run();

    }
}
