
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
    
    def reverseList(self, head: ListNode) -> ListNode:
        # result: ListNode = self.reverseList1(head)
        result: ListNode = self.reverseList2(head)
        return result
        
    # 方法一：使用递归翻转链表
    def reverseList1(self, head: ListNode) -> ListNode:
        # 递归到最后一个节点后的None节点，返回None
        if not head:
            return head
        # 递归到最后一个节点，返回最后一个节点本身
        if not head.next:
            return head

        newHead: ListNode = self.reverseList1(head.next)
        head.next.next = head
        head.next = None # 此处置None，防止形成环
        return newHead 

    # 方法二： 使用头插法实现
    def reverseList2(self, head: ListNode) -> ListNode:
        pre: ListNode = None
        cur: ListNode = head
        
        while cur.next:
            # 翻转指向，将cur.next指向pre
            tempNextNode: ListNode = cur.next
            cur.next = pre
            
            # pre和cur都向前走一步
            pre = cur
            cur = tempNextNode
        # 结束循环时cur指向链表最后一个元素，pre为倒数第二个元素
        cur.next = pre
        return cur
        



def run():
    header1: ListNode = generateLinkList(data=[1, 2, 3, 4, 5, 6])
    header2: ListNode = generateLinkList(data=[11, 22, 33, 44, 55, 66])
    

    result1: ListNode = Solution().reverseList(head=header1)
    result2: ListNode = Solution().reverseList(head=header2)
    print(f"result1={printLinkList(result1)}， result2={printLinkList(result2)}")

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

