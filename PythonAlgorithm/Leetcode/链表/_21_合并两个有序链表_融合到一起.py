
# https://leetcode.cn/problems/merge-two-sorted-lists

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
        # result: ListNode = self.mergeTwoLists1(list1, list2)
        result: ListNode = self.mergeTwoLists2(list1, list2)
        return result

    # 方法一：递归，各种左右判断大小，递归调用
    def mergeTwoLists1(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists1(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists1(list1, list2.next)
            return list2

    # 方法二：迭代的方式
    def mergeTwoLists2(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 创建一个空节点
        fakeHead: ListNode = ListNode(val=-1)
        tempNode: ListNode = fakeHead

        # 开始循环遍历
        while (list1 and list2):
            if list1.val <= list2.val:
                tempNode.next = list1
                list1 = list1.next
            else:
                tempNode.next = list2
                list2 = list2.next
                
            # 每轮循环完后，自己next到下一个节点
            tempNode = tempNode.next

        # 合并后list1和list2 最多只有一个还未被合并完，直接将链表末尾指向未合并完的链表即可
        tempNode.next = list2 if (list1 is None) else list1
        
        resutlHead: ListNode = fakeHead.next
        return resutlHead


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

