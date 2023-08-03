from typing import Generic, TypeVar, List
E = TypeVar('E')


class 循环单端队列(Generic[E]):

    def __init__(self, *, capacity: int) -> None:

        DEFAULT_CAPACITY: int = 10  # 默认数组分配内存空间

        # 容量不能小于默认容量(10)
        self.capacity = capacity if (
            capacity >= DEFAULT_CAPACITY) else DEFAULT_CAPACITY
        # 动态数组
        self.__elements: List[E] = ["null"] * capacity

        # 元素数量
        self.__eleCount: int = 0
        # 队头指针的下标
        self.frontPos: int = 0

    def size(self) -> int:
        # --------队列的长度--------
        return self.__eleCount

    def isEmpty(self) -> bool:
        # --------队列是否为空--------
        return self.size() == 0

    def clear(self):
        # --------清空队列--------
        for temp in range(self.__eleCount):
            self.__elements[self.caculateFrontIndex(temp)] = "null"
        # 队头和size归零
        self.frontPos = 0
        self.__eleCount = 0

    def enQueue(self, element: E):
        # front指针出入队列
        self.__ensure_capacity(self.__eleCount + 1)

        enQueuePos: int = self.caculateFrontIndex(self.__eleCount)
        self.__elements[enQueuePos] = element
        self.__eleCount += 1

    def deQueue(self):
        # 获取队头指向的元素
        # frontEle: E = self.__elements[self.frontPos]
        # 删除队头指向的元素
        self.__elements[self.frontPos] = "null"
        # 队头向后移动1位
        self.frontPos = self.caculateFrontIndex(1)
        self.__eleCount -= 1

    def front(self) -> E:
        # --------获取当前队列首个元素--------
        return self.__elements[self.frontPos]

    def caculateFrontIndex(self, step: int) -> int:
        # step:1 front指针向右走一步
        # step:-1 front指针向左走一步
        newFrontPos = self.frontPos + step
        
        if newFrontPos >= len(self.__elements):
            # 到达右边界，移动到左边界,继续把步数走完
            return newFrontPos - len(self.__elements)
        else:
            # 正常左右移动
            return newFrontPos
            
    # def caculateExcutePos(self, eleCounts: int) -> int:
    #     tempTailIndex: int = self.frontPos + eleCounts
    #     temp: int = 0
    #     if tempTailIndex > len(self.__elements):
    #         temp = len(self.__elements)
    #     else:
    #         temp = 0
    #     return tempTailIndex - temp

    def __ensure_capacity(self, tempCapacity: int):
        # 保证要有capacity的容量
        if self.capacity >= tempCapacity:
            return

        old_capacity = self.capacity
        new_capacity = 0
        # 新容量为旧容量的1.5倍
        if old_capacity == 0:
            new_capacity = 10
        else:
            new_capacity = int(self.capacity * 1.5)

        new_elements = ["null"] * new_capacity
        self.capacity = new_capacity
        
        # 扩容时，会按照队首->队尾的顺序重新排列整个队列
        for i in range(self.__eleCount):
            new_elements[i] = self.__elements[self.caculateFrontIndex(i)]
        self.__elements = new_elements
        # 队首归零
        self.frontPos = 0
        print(f"***队列扩容：{old_capacity} - {new_capacity}")
        

    def __str__(self) -> str:
        resultStr = f"总容量={len(self.__elements)} 占用容量={self.__eleCount} "
        resultStr = resultStr + f"队头front下标={self.frontPos}  头["
        for temp in range(len(self.__elements)):
            if temp != 0:
                resultStr = resultStr + " ,"
            currentEle = f"{self.__elements[temp]}"
            resultStr = resultStr + currentEle
        resultStr = resultStr + "]尾"
        return resultStr
