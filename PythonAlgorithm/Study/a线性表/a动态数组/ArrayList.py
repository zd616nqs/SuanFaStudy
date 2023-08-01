from typing import Generic, TypeVar, List
E = TypeVar('E')


class Person(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def toString(self) -> str:
        print(f"Person:[name={self.name} age={self.age}]")
    
    def __eq__(self, __value: object) -> bool:
        if object and (type(__value) == type(self)):
            return (self.name == __value.name) and (self.age == __value.age)



# 定义ArrayListClass为泛型，根据实例化时传入的类型决定
# int_list = ArrayListClass[int]()
# int_list.append(1)
#
# string_list = ArrayListClass[str]()        
# string_list.append("Hello")
class ArrayListClass(Generic[E]):

    
    def __init__(self, *, capacity: int) -> None:
        
        DEFAULT_CAPACITY: int = 10 # 默认数组分配内存空间
        
        # 容量不能小于默认容量(10)
        self.capacity = capacity if (capacity >= DEFAULT_CAPACITY) else DEFAULT_CAPACITY
        # 动态数组
        self.__elements: List[E] = [None] * capacity
        # 元素数量
        self.__eleCount: int = 0

    def clear(self) -> None:
        # 清除所有元素
        for i in range(self.__eleCount):
            self.__elements[i] = None
        self.__eleCount = 0
        self.__elements = None
        self.capacity = 0
    
    def caculateEleCount(self) -> int:
        # 元素的数量
        return self.__eleCount

    def is_empty(self) -> bool:
        # 是否为空
        return self.__eleCount == 0

    def contains(self, element: E) -> bool:
        # 是否包含某个元素
        return self.find(element) != -1

    def addToTail(self, element: E) -> None:
        # 添加元素到尾部
        self.insertObjectAtIndex(self.__eleCount, element)

    def getObjectAtIndex(self, index: int) -> E:
        # 获取index位置的元素
        self.__range_check(index)
        return self.__elements[index]

    def setObjectAtIndex(self, index: int, element: E) -> None:
        # 设置index位置的元素
        self.__range_check(index)
        self.__elements[index] = element
        

    def insertObjectAtIndex(self, index: int, element: E) -> None:
        # 在index位置插入一个元素
        self.__range_check_for_add(index)
        self.__ensure_capacity(self.__eleCount + 1)
        
        for i in range(self.__eleCount, index, -1):
            self.__elements[i] = self.__elements[i - 1]
        
        self.__elements[index] = element
        self.__eleCount += 1

    def removeObjectAtIndex(self, index: int) -> E:
        # 删除index位置的元素
        self.__range_check(index)
        old = self.__elements[index]
        
        for i in range(index + 1, self.__eleCount):
            self.__elements[i - 1] = self.__elements[i]
        
        # 将删除前的最后一个元素置空
        self.__elements[self.__eleCount - 1] = None
        
        self.__eleCount -= 1
        
        # 动态缩容
        self.__trim()
        return old

    def indexOfObject(self, element: E) -> int:
        # 查看元素的索引
        if element is None:
            for i in range(self.__eleCount):
                if self.__elements[i] is None:
                    return i
        else:
            for i in range(self.__eleCount):
                if element == self.__elements[i]:
                    return i
        return -1

    def __ensure_capacity(self, tempCapacity: int) -> None:
        # 保证要有capacity的容量
        if self.capacity > tempCapacity:
            return
        
        old_capacity = self.capacity
        new_capacity = 0
        # 新容量为旧容量的1.5倍
        if old_capacity == 0:
            new_capacity = 10
        else:
            new_capacity = int(self.capacity * 1.5)
        
        new_elements = [None] * new_capacity
        for i in range(self.__eleCount):
            new_elements[i] = self.__elements[i]
        
        self.__elements = new_elements
        self.capacity = new_capacity
        print(f"数组容量从:{old_capacity} 扩容到: {new_capacity}")

    def __trim(self):
        # 30
        oldCapacity: int  = len(self.__elements)
        # 15
        newCapacity: int  = int(oldCapacity / 2)
        if ((self.__eleCount > newCapacity) or (oldCapacity < 10)):
            return

        # 当前可以进行数组缩容
        new_elements = [None] * newCapacity
        for i in range(self.__eleCount):
            new_elements[i] = self.__elements[i]
        self.__elements = new_elements
        print(f"数组容量从:{oldCapacity} 缩容到: {newCapacity}")

    def __out_of_bounds(self, index: int) -> None:
        # 打印抛出异常
        raise IndexError(f"下标越界：Index: {index}, eleCount: {self.__eleCount}")

    def __range_check(self, index: int) -> None:
        # 监测index是否越界
        if index < 0 or index >= self.__eleCount:
            self.__out_of_bounds(index)

    def __range_check_for_add(self, index: int) -> None:
        # 监测index是否越界 
        if index < 0 or index > self.__eleCount:
            self.__out_of_bounds(index)

    def __str__(self) -> str:
        string = ["动态数组汇总：\n\t元素数量:" + str(self.__eleCount) + ", \n\t"]
        for i in range(self.__eleCount):
            if i != 0:
                string.append("\n\t")
            string.append(f"index:{i}："+str(self.__elements[i]))
        return "".join(string)
    


