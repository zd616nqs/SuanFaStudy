package jeason.A_Leetcode.队列;


// https://leetcode-cn.com/problems/implement-queue-using-stacks/


import java.util.Stack;

public class _232_用栈实现队列 {

    //准备两个栈来实现
	private Stack<Integer> inStack;
	private Stack<Integer> outStack;

    public _232_用栈实现队列() {
        inStack = new Stack<>();
        outStack = new Stack<>();
    }
    
    /** 入队 */
    public void push(int x) {
        inStack.push(x);
    }
    
    /** 出队 */
    public int pop() {

        //如果outStack为空：将inStack所有元素逐个弹出，push到outStack中，然后outStack执行pop
        //如果outStack不为空，直接从outStack执行pop
        checkOutStack();
        return outStack.pop();
    }
    
    /** 获取队头元素 */
    public int peek() {
        //如果outStack为空：将inStack所有元素逐个弹出，push到outStack中，然后获取outStack栈顶元素
        //如果outStack不为空，直接获取outStack栈顶元素
        checkOutStack();
        return outStack.peek();
    }
    
    /** 是否为空 */
    public boolean empty() {
        return inStack.isEmpty() && outStack.isEmpty();
    }
    
    private void checkOutStack() {
        if (outStack.isEmpty()) {
            while (!inStack.isEmpty()) {
                //将inStack的所有元素依次pop，再依次push到outStack,实现两个栈的元素顺序颠倒
                outStack.push(inStack.pop());
            }
        }
    }
}
