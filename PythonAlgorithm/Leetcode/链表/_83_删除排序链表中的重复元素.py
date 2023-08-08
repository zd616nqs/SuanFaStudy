
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/

""" 
给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 

输入：head = [1,1,2]
输出：[1,2]

输入：head = [1,1,2,3,3]
输出：[1,2,3]

题解：
"""


class ListNode(object):
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val: int = val
        self.next: ListNode = next

class Solution(object):

    # 思路一次遍历   连续两个元素相同就删除一个
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        curNode: ListNode = head
        while (curNode.next):
            if curNode.val == curNode.next.val:
                curNode.next = curNode.next.next
            else:
                curNode = curNode.next
        
        return head



def run():
    header1: ListNode = generateLinkList(data=[1, 2, 3, 3, 4, 4])
    result: ListNode = Solution().deleteDuplicates(head=header1)
    print(f"{printLinkList(result)}")   # 1, 2, 3, 4

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

