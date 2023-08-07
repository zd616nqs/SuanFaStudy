
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

""" 
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

题解：https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solutions/410351/san-chong-fang-fa-shan-chu-dao-shu-di-nge-jie-dian/

"""


class ListNode(object):
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val: int = val
        self.next: ListNode = next

class Solution(object):
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        result: ListNode
        result = self.removeNthFromEnd1(head, n)
        # result = self.removeNthFromEnd1(head, n)
        # result = self.removeNthFromEnd1(head, n)
        return result

    # 方法一：快慢指针 fast指针比slow指针超前N个节点
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        # 在首个节点前面添加虚拟的空节点
        fakeHeader: ListNode = ListNode(0, None)
        fakeHeader.next = head
        
        # 快慢指针都从虚拟空节点出发
        fast: ListNode = fakeHeader
        slow: ListNode = fakeHeader

        # 让快指针领先慢指针N个位置
        for _ in range(n):
            fast = fast.next
            
        # 快慢指针同时往前走，当快指针到达尾部节点时，慢指针到达倒数N+1个节点位置
        # 这里注意一定是fast and fast.next有值
        while (fast and fast.next):
            fast = fast.next
            slow = slow.next
        
        # 将倒数第n+1节点的next指向倒数n-1节点
        slow.next = slow.next.next

        # 虚空头节点的next为真实的头结点
        return fakeHeader.next
    
    # 方法二：遍历搜索法  时间复杂度O(n)，空间复杂度O(1)
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        fakeHeader: ListNode = ListNode(666)
        fakeHeader.next = head
        
        # 计算整个链表的节点数
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        
        # 找到倒数第N+1个节点
        temp = fakeHeader
        for _ in range(length - length):
            temp = temp.next
        
        # 将倒数第n+1节点的next指向倒数n-1节点
        temp.next = temp.next.next
        
        # 虚空头节点的next为真实的头结点
        return temp.next    
        
    # 方法三：递归迭代：回溯时，进行节点计数
    def removeNthFromEnd3(self, head: ListNode, n: int) -> ListNode:
        if not head:
            self.count = 0
            return head
        head.next = self.removeNthFromEnd3(head, n) # 递归调用
        self.count += 1 # 回溯时进行节点计数
        
        return head.next if (self.count == n) else head


def run():
    
    header: ListNode = generateLinkList(data=[1, 2, 3, 4, 5])

    print(f"before:{printLinkList(header)}")    
    result: ListNode = Solution().removeNthFromEnd(header, 2)
    print(f"after:{printLinkList(result)}")   
    
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

