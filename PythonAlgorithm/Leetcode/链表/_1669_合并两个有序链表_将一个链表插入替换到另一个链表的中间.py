
# https://leetcode.cn/problems/merge-in-between-linked-lists/

""" 
给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。
请你将 list1 中下标从 a 到 b 的全部节点都删除，并将list2 接在被删除节点的位置。

输入：list1 = [0,1,2,33,444,55,6], a = 33, b = 55, list2 = [1001,1002,1003]
输出：[0,1,2,1001,1002,1003,6]
题解：
"""


class ListNode(object):
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val: int = val
        self.next: ListNode = next

class Solution(object):
    
    def mergeInBetween(self, list1: ListNode, indexOfStart: int, indexOfEnd: int, list2: ListNode) -> ListNode:
        
        # 找到需要替换区间的开头和结尾节点
        insertStartNode = insertEndNode = None
        
        tempNode: ListNode = list1
        i: int = 0
        while list1 and list1.next:
            # 插入的起始、结束点都结束了，中止循环
            if insertStartNode and insertEndNode:
                break
            
            # 找到起始点的前一个节点
            if (i == (indexOfStart - 1)) and (i < indexOfEnd):
                insertStartNode = tempNode
            # 找到结束点
            if (i == indexOfEnd):
                insertEndNode = tempNode
            
            i += 1
            tempNode = tempNode.next
            
        
        if insertEndNode and insertStartNode:
            # 起始点的前一个节点.next指向list2
            insertStartNode.next = list2
            # list2的最后一个节点.next指向->结束点.next
            tempInsertNode: ListNode = list2
            while tempInsertNode.next:
                tempInsertNode = tempInsertNode.next
            tempInsertNode.next = insertEndNode.next
            
        return list1


def run():
    list1: ListNode = generateLinkList(data=[1, 2, 33, 44, 55, 6])
    list2: ListNode = generateLinkList(data=[1000, 1001, 1002])
    
    result: ListNode = Solution().mergeInBetween(list1=list1, indexOfStart=2, indexOfEnd=4, list2=list2)
    print(f"result1={printLinkList(result)}")
    

# 生成单向链表
def generateLinkList(data: list) -> ListNode:
    header: ListNode = ListNode(666, None)
    lastNode: ListNode = header
    for i, ele in enumerate(data):
        tempNode: ListNode = ListNode(ele, None)
        lastNode.next = tempNode
        lastNode = tempNode
    return header.next

# 打印单向链表
def printLinkList(header: ListNode) -> str:
    
    printStr: str = f"{header.val}"
    while header.next is not None:
        header = header.next
        printStr = f"{printStr}, {header.val}"
    return f"{printStr}"

run()

