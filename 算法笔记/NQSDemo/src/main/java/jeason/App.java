package jeason;

import jeason.TimeTool.Task;

public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );

        
        TimeTool.check("测试", new Task() {
			public void execute() {
                System.out.println( "哈哈哈");
			}
		});
    }
}
