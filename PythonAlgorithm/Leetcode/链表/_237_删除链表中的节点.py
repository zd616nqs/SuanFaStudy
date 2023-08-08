
# https://leetcode.cn/problems/delete-node-in-a-linked-list/

""" 
输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：指定链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9

前提条件： 不能删除最后面的那个节点

题解：https://leetcode.cn/problems/linked-list-cycle/solutions/233220/141-linked-list-cycle_li-jie-by-gulugulu_go/
"""


class ListNode(object):
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val: int = val
        self.next: ListNode = next

class Solution(object):
    
    def deleteNode(self, node: ListNode):
        if node is None:
            return
        
        # 把要删除的node节点的下一个节点值附上，next跨一个
        # 相当于把指定node节点的下一个节点给删除了
        node.val = node.next.val
        node.next = node.next.next
        
        



def run():
    header: ListNode = generateLinkList(data=[1, 2, 3, 4, 5, 6])
    Solution().deleteNode(node=header.next.next)
    print(f"result1={printLinkList(header)}")
    

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

