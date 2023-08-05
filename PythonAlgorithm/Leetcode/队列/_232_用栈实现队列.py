
# https://leetcode-cn.com/problems/implement-queue-using-stacks/

"""
题解：https://leetcode.cn/problems/implement-queue-using-stacks/solutions/635805/dong-hua-jiang-jie-ru-he-shi-yong-liang-6g7ub/
思路：
特性:  栈=>后进先出  队列=>先进先出
使用两个栈，push时放入栈1，pop/peek操作时，先把栈1的放入栈2，再正常执行栈2的出栈操作
"""

class MyQueue:

    def __init__(self):
        self.stack1: list = []
        self.stack2: list = []

    def push(self, element: int) -> None:
        """将元素 x 推到队列的末尾"""
        self.stack1.append(element)

    def pop(self) -> int:
        """从队列的开头移除并返回元素"""
        if len(self.stack2) <= 0:
            while (len(self.stack1)):
                self.stack2.append(self.stack1.pop()) 
        return self.stack2.pop()
        

    def peek(self) -> int:
        """返回队列开头的元素"""
        if len(self.stack2) <= 0:
            while (len(self.stack1)):
                self.stack2.append(self.stack1.pop()) 
        return self.stack2[-1]

    def empty(self) -> bool:
        """如果队列为空"""
        return not len(self.stack1) and not len(self.stack2)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


class _232_用栈实现队列(object):
    @staticmethod
    def run(self):
        
        queue: MyQueue = MyQueue()
        queue.push(element=1)
        queue.push(element=2)
        queue.push(element=3)
        print(f"{queue.peek()}")
        print(f"{queue.pop()}")
        print(f"{queue.empty()}")