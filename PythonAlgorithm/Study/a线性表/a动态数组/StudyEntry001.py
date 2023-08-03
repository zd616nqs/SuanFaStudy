from .ArrayList import ArrayListClass, Person


class StudyEntry001(object):

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def run(*, execute: bool):
        if (not execute):
            return
        
        # 创建动态数组
        arrayList: ArrayListClass = ArrayListClass(capacity=10)
        print(arrayList)
        
        # 添加元素，默认添加到最后
        arrayList.addToTail(Person(name="牛牛", age=18))
        arrayList.addToTail("青青")
        arrayList.addToTail(Person(name="山山", age=20))
        arrayList.addToTail(None)
        print(arrayList)
        
        # insert元素
        arrayList.insertObjectAtIndex(1, "琳琳")
        print(arrayList)
        
        # 取下标
        print(arrayList.indexOfObject(None))
        print(arrayList.indexOfObject("青青"))
        
        arrayList.removeObjectAtIndex(0)
        print("元素数量："+str(arrayList.caculateEleCount()))
        
        # 清空
        arrayList.clear()
        print(arrayList)
        
        
        
        for i in range(30):
            arrayList.addToTail(element=i)
            
        for i in range(20):
            arrayList.removeObjectAtIndex(index=0)


