
# https://leetcode.cn/problems/linked-list-cycle/

""" 
给你一个链表的头节点 head ，判断链表中是否有环。 

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况

如果链表中存在环 ，则返回 true 。 否则，返回 false 。


输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

题解：https://leetcode.cn/problems/linked-list-cycle/solutions/233220/141-linked-list-cycle_li-jie-by-gulugulu_go/
"""


class ListNode(object):
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val: int = val
        self.next: ListNode = next

class Solution(object):
    # 使用快慢指针，如果能够相遇，说明是环形的
    def hasCycle(self, head: ListNode) -> bool:
        if (head is None) or (head.next is None):
            return False
        
        fast: ListNode = head
        slow: ListNode = head
        
        while (fast and fast.next):
            fast = fast.next.next # 快指针每次走2步
            slow = slow.next # 慢指针每次走1步
            if fast == slow:
                return True

        return False




def run():
    # 数据1:有环
    header1: ListNode = generateLinkList(data=[1, 2, 3, 3, 4, 4])
    tempNode: ListNode = header1
    while tempNode:
        if tempNode.next:
            tempNode = tempNode.next
        else:
            # 找到了最后一个节点,人为创建环
            tempNode.next = header1.next.next
            break
        
    result1: bool = Solution().hasCycle(head=header1)
    # 数据2:没环
    header2: ListNode = generateLinkList(data=[3, 3, 3, 3, 3, 3])
    result2: bool = Solution().hasCycle(head=header2)
    
    print(f"result1={result1}， result2={result2}")

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

