
# from ....NQS_Utils import func_cal_time
# from typing import Generic, TypeVar, List

# E = TypeVar('E')


# @func_cal_time
def exampleFun22(para1: str, para2: int):
    print(f"para1:{para1}, para2:{para2}")
    
# exampleFun("牛牛", 222)

# class ArrayList(Generic[E]):

#     # 元素的数量
#     size: int  
#     # 所有的元素
#     elements: List[E]
    
#     # 默认数组分配内存空间
#     DEFAULT_CAPACITY: int = 10  
#     # 未找到元素的下标 
#     ELEMENT_NOT_FOUND: int = -1

#     def __init__(self, capacity: int = DEFAULT_CAPACITY) -> None:
#         # 容量不能小于默认容量
#         self.capacity = capacity if capacity >= DEFAULT_CAPACITY else DEFAULT_CAPACITY
#         self.elements = [None] * self.capacity 
#         self.size = 0

#     def clear(self) -> None:
#         # 清除所有元素
#         for i in range(self.size):
#             self.elements[i] = None
#         self.size = 0

#     def size(self) -> int:
#         # 元素的数量
#         return self.size

#     def is_empty(self) -> bool:
#         # 是否为空
#         return self.size == 0

#     def contains(self, element: E) -> bool:
#         # 是否包含某个元素
#         return self.index_of(element) != ELEMENT_NOT_FOUND

#     def add(self, element: E) -> None:
#         # 添加元素到尾部
#         self.add(self.size, element)

#     def get(self, index: int) -> E:
#         # 获取index位置的元素
#         self._range_check(index)
#         return self.elements[index]

#     def set(self, index: int, element: E) -> E:
#         # 设置index位置的元素
#         self._range_check(index)
#         old = self.elements[index]
#         self.elements[index] = element
#         return old

#     def add(self, index: int, element: E) -> None:
#         # 在index位置插入一个元素
#         self._range_check_for_add(index)
#         self._ensure_capacity(self.size + 1)
        
#         for i in range(self.size, index, -1):
#             self.elements[i] = self.elements[i - 1]
        
#         self.elements[index] = element
#         self.size += 1

#     def remove(self, index: int) -> E:
#         # 删除index位置的元素
#         self._range_check(index)
#         old = self.elements[index]
        
#         for i in range(index + 1, self.size):
#             self.elements[i - 1] = self.elements[i]
        
#         self.elements[self.size - 1] = None
#         self.size -= 1
#         return old

#     def index_of(self, element: E) -> int:
#         # 查看元素的索引
#         if element is None:
#             for i in range(self.size):
#                 if self.elements[i] is None:
#                     return i
#         else:
#             for i in range(self.size):
#                 if element == self.elements[i]:
#                     return i
#         return ELEMENT_NOT_FOUND

#     def _ensure_capacity(self, capacity: int) -> None:
#         # 保证要有capacity的容量
#         if self.capacity >= capacity:
#             return
        
#         new_capacity = self.capacity + (self.capacity >> 1)
#         new_elements = [None] * new_capacity
#         for i in range(self.size):
#             new_elements[i] = self.elements[i]
        
#         self.elements = new_elements
#         self.capacity = new_capacity
#         print(f"{self.capacity} expanded to {new_capacity}")

#     def _out_of_bounds(self, index: int) -> None:
#         # 打印抛出异常
#         raise IndexError(f"Index: {index}, Size: {self.size}")

#     def _range_check(self, index: int) -> None:
#         # 监测index是否越界
#         if index < 0 or index >= self.size:
#             self._out_of_bounds(index)

#     def _range_check_for_add(self, index: int) -> None:
#         # 监测index是否越界 
#         if index < 0 or index > self.size:
#             self._out_of_bounds(index)

#     def __str__(self) -> str:
#         # size=3, [99, 88, 77]
#         string = ["size=" + str(self.size) + ", ["]
#         for i in range(self.size):
#             if i != 0:
#                 string.append(", ")
#             string.append(str(self.elements[i]))
#         string.append("]")
#         return "".join(string)
    