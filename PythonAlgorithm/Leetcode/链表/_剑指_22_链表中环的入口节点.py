
# https://leetcode.cn/problems/c32eOV/

""" 
给定一个链表，返回链表开始入环的第一个节点。 从链表的头节点开始沿着 next 指针进入环的第一个节点为环的入口节点。如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。

题解：https://leetcode.cn/problems/c32eOV/solutions/
"""


class ListNode(object):
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val: int = val
        self.next: ListNode = next

class Solution(object):
    # 思路：1.快慢指针开始出发，相遇时，从头节点再出发一个指针，之后新指针和慢指针都步长为1，再次相遇时，即为环的入口
    def detectCycle(self, head: ListNode) -> ListNode:
        slow: ListNode = head
        fast: ListNode = head

        # 找到快慢指针的第一次相遇节点
        while True:
            if not (fast and fast.next): 
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                break
        
        # 从头节点开始出发一个指针
        newHead: ListNode = head
        while newHead != slow:
            newHead = newHead.next
            slow = slow.next
            # 头结点指针和慢指针相遇点，即为环的入点
            if newHead == slow:
                return slow
        return None
        



def run():
    
    header1: ListNode = generateLinkList(data=[5, 3, 2, 7, 1, 6, 8, 9, 4])
    tempNode: ListNode = header1
    while tempNode:
        if tempNode.next:
            tempNode = tempNode.next
        else:
            # 找到了最后一个节点,人为创建环 4->1
            tempNode.next = header1.next.next.next.next
            break
    
    result: ListNode = Solution().detectCycle(head=header1)
    print(f"{result.val}")   # 1

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

