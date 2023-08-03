import copy
from .单端队列 import 单端队列
from .双端队列 import 双端队列
from .循环单端队列 import 循环单端队列
from .循环双端队列 import 循环双端队列


class StudyEntry004(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def run(*, execute: bool):
        if (not execute):
            return

        # ---------------队列----------
        obj = StudyEntry004()

        obj.example1(isWork=False)
        
        obj.example2(isWork=False)
        
        obj.example3(isWork=False)
        
        obj.example4(isWork=True)

    def example1(self, *, isWork: bool):
        if (not isWork):
            return

        queue1: 单端队列 = 单端队列[str]()
        queue1.enQueue(element="111")
        queue1.enQueue(element="222")
        queue1.enQueue(element="333")
        queue1.enQueue(element="444")
        queue1.enQueue(element="555")
        print(f"{queue1}")
        

        while (not queue1.isEmpty()):
            print(f'准备deQueue，队首元素：{queue1.front()}')
            queue1.deQueue()
            
        """ 
        双向链表汇总：
                元素数量:5, 
                index:0：111
                index:1：222
                index:2：333
                index:3：444
                index:4：555
        准备deQueue，队首元素：111
        准备deQueue，队首元素：222
        准备deQueue，队首元素：333
        准备deQueue，队首元素：444
        准备deQueue，队首元素：555
        """

    def example2(self, *, isWork: bool):
        if (not isWork):
            return

        queue2: 双端队列 = 双端队列[str]()
        queue2.enQueueWithFront(element="11")
        queue2.enQueueWithRear(element="1111")
        queue2.enQueueWithFront(element="22")
        queue2.enQueueWithRear(element="2222")
        queue2.enQueueWithFront(element="33")
        queue2.enQueueWithRear(element="3333")
        queue2.enQueueWithFront(element="44")
        queue2.enQueueWithRear(element="4444")
        print(f"{queue2}\n")
        
        queue2222: 双端队列 = copy.deepcopy(queue2)
        print("----从队首出列")
        while (not queue2.isEmpty()):
            print(f'准备从队首deQueue，队首：{queue2.front()} ,队尾:{queue2.rear()}')
            queue2.deQueueWithFront()
        
        print("----从队尾出列")
        while (not queue2222.isEmpty()):
            print(f'准备从队尾deQueue，队首：{queue2222.front()} ,队尾:{queue2222.rear()}')
            queue2222.deQueueWithRear()
        
        """ 
        双向链表汇总：
                元素数量:8, 
                index:0：44
                index:1：33
                index:2：22
                index:3：11
                index:4：1111
                index:5：2222
                index:6：3333
                index:7：4444

        ----从队首出列
        准备从队首deQueue，队首：44 ,队尾:4444
        准备从队首deQueue，队首：33 ,队尾:4444
        准备从队首deQueue，队首：22 ,队尾:4444
        准备从队首deQueue，队首：11 ,队尾:4444
        准备从队首deQueue，队首：1111 ,队尾:4444
        准备从队首deQueue，队首：2222 ,队尾:4444
        准备从队首deQueue，队首：3333 ,队尾:4444
        准备从队首deQueue，队首：4444 ,队尾:4444
        ----从队尾出列
        准备从队尾deQueue，队首：44 ,队尾:4444
        准备从队尾deQueue，队首：44 ,队尾:3333
        准备从队尾deQueue，队首：44 ,队尾:2222
        准备从队尾deQueue，队首：44 ,队尾:1111
        准备从队尾deQueue，队首：44 ,队尾:11
        准备从队尾deQueue，队首：44 ,队尾:22
        准备从队尾deQueue，队首：44 ,队尾:33
        准备从队尾deQueue，队首：44 ,队尾:44
        """
        
    def example3(self, *, isWork: bool):
        if (not isWork):
            return
    
        
        # ------初始容量10-------
        queue3: 循环单端队列 = 循环单端队列[str](capacity=10)
        print(f"{queue3}")
        # 总容量=10 占用容量=0 队头front下标=0  
        # 头[null ,null ,null ,null ,null ,null ,null ,null ,null ,null]尾
        
        # -------初始入队操作-------
        for a in range(10):
            queue3.enQueueWithTail(element=f"{a}")
        print(f"{queue3}")
        # 总容量=10 占用容量=10 队头front下标=0  
        # 头[0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]尾
        
        # -------——扩容操作---------
        for b in range(90, 93):
            queue3.enQueueWithTail(element=f"{b}")
        print(f"{queue3}")
        # ***队列扩容：10 - 15
        # 总容量=15 占用容量=13 队头front下标=0  
        # 头[0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,90 ,91 ,92 ,null ,null]尾
        
        # --------出队操作，队头发生移动--------
        for c in range(3):
            queue3.deQueueWithFront()
        print(f"{queue3}")
        # 总容量=15 占用容量=10 队头front下标=3  
        # 头[null ,null ,null ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,90 ,91 ,92 ,null ,null]尾
        
        # ------再次入队操作-------
        for d in range(673, 677):
            queue3.enQueueWithTail(element=f"{d}")
        print(f"{queue3}")
        # 总容量=15 占用容量=14 队头front下标=3  
        # 头[675 ,676 ,null ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,90 ,91 ,92 ,673 ,674]尾
        
        # ----接着入队，会进行扩容
        # ----扩容时会重新排序队列，把真正的front放到队首
        # ----先扩容，再执行入队，新入队的数据接着在队尾添加
        for e in range(880, 885):
            queue3.enQueueWithTail(element=f"{e}")
        print(f"{queue3}")
        # ***队列扩容：15 - 22
        # 总容量=22 占用容量=19 队头front下标=0  
        # 头[3 ,4 ,5 ,6 ,7 ,8 ,9 ,90 ,91 ,92 ,673 ,674 ,675 ,676 ,880 ,881 ,882 ,883 ,884 ,null ,null ,null]尾

    def example4(self, *, isWork: bool):
        if (not isWork):
            return
    
        
        # ------初始容量10-------
        queue4: 循环双端队列 = 循环双端队列[str](capacity=10)
        print(f"{queue4}")
        # 总容量=10 占用容量=0 队头front下标=0  
        # 头[null ,null ,null ,null ,null ,null ,null ,null ,null ,null]尾
        
        # 初始值88
        queue4.enQueueWithFront(element="88")
        print(f"{queue4}")
        # 总容量=10 占用容量=1 队头front下标=9  
        # 头[null ,null ,null ,null ,null ,null ,null ,null ,null ,88]尾
        
        for a in range(1, 6):
            # 增加队列元素，动态扩容
            queue4.enQueueWithFront(element=f"{a}") # 头部入队
            queue4.enQueueWithTail(element=f"{100+a}") # 尾部入队
        print(f"{queue4}")
        # ***队列扩容：10 - 15
        # 总容量=15 占用容量=11 队头front下标=0  
        # 头[5 ,4 ,3 ,2 ,1 ,88 ,101 ,102 ,103 ,104 ,105 ,null ,null ,null ,null]尾
        
        # -------头部入队，循环队列会把添加的数据放到扩容后的队尾的index位置
        # -------尾部入队，接着上次尾部的index往后添加数据
        queue4.enQueueWithFront(element="666") # 头部入队
        queue4.enQueueWithTail(element="888") # 尾部入队
        print(f"{queue4}")
        # 总容量=15 占用容量=13 队头front下标=14  
        # 头[5 ,4 ,3 ,2 ,1 ,88 ,101 ,102 ,103 ,104 ,105 ,888 ,null ,null ,666]尾
        
        # ---接着入队，放满队列
        queue4.enQueueWithFront(element="1992") # 头部入队
        queue4.enQueueWithFront(element="1993") # 头部入队
        print(f"{queue4}")
        # 总容量=15 占用容量=15 队头front下标=12  
        # 头[5 ,4 ,3 ,2 ,1 ,88 ,101 ,102 ,103 ,104 ,105 ,888 ,1993 ,1992 ,666]尾
        
        # ----接着入队，会进行扩容
        # ----扩容时会重新排序队列，把真正的front放到队首
        # ----先扩容，再执行入队，所以新入队的数据又被放到扩容后的队列的最后index位置了
        queue4.enQueueWithFront(element="1994")
        print(f"{queue4}")
        # ***队列扩容：15 - 22
        # 总容量=22 占用容量=16 队头front下标=21  
        # 头[1993 ,1992 ,666 ,5 ,4 ,3 ,2 ,1 ,88 ,101 ,102 ,103 ,104 ,105 ,888 ,null ,null ,null ,null ,null ,null ,1994]尾