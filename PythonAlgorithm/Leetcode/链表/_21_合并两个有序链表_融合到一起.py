
# https://leetcode.cn/problems/merge-two-sorted-lists/？

""" 
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

题解：https://leetcode.cn/problems/merge-two-sorted-lists/solutions/103891/yi-kan-jiu-hui-yi-xie-jiu-fei-xiang-jie-di-gui-by-/
"""


class ListNode(object):
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val: int = val
        self.next: ListNode = next

class Solution(object):
    
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        pass


def run():
    header1: ListNode = generateLinkList(data=[1, 2, 4])
    header2: ListNode = generateLinkList(data=[1, 3, 4])
    
    result: ListNode = Solution().mergeTwoLists(list1=header1, list2=header2)
    print(f"{printLinkList(result)}")   

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

