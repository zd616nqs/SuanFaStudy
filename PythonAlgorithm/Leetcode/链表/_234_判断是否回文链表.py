
# https://leetcode.cn/problems/palindrome-linked-list/

""" 
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 

输入：head = [1,2,3,3,2,1]
输出：true

输入：head = [1,2,3,2,1]
输出：true

输入：head = [1,2]
输出：false


题解：https://leetcode.cn/problems/palindrome-linked-list/solutions/457059/hui-wen-lian-biao-by-leetcode-solution/
"""


class ListNode(object):
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val: int = val
        self.next: ListNode = next

class Solution(object):
    # 方法一：思路：将链表的值赋值到数组后，对比数组正序和倒序是否一样
    # 时间复杂度O(n) 空间复杂度O(n)
    def isPalindrome1(self, head: ListNode) -> bool:
        currentNode: ListNode = head
        tempList: list = []
        # 将链表的所有的val放入数组中
        while currentNode is not None:
            tempList.append(currentNode.val)
            currentNode = currentNode.next
        # 数组正序和倒序进行对比是否一致
        result: bool = (tempList == tempList[::-1])
        return result
        
    # 方法二：递归 
    # 思路：front指针指向head，currentNode递归指向到尾部，两个指针前后一步一步移动进行对比
    # 时间复杂度O(n) 空间复杂度O(n)
    def isPalindrome2(self, head: ListNode) -> bool:
        
        self.front = head
        
        def recursiveCheck(currentNode: ListNode):
            
            if currentNode is not None: # 2.递归直到最后一个节点
                if not recursiveCheck(currentNode.next):# 1.将currentNode节点一层层next递归
                    return False # 6.左右节点有一次对不上，直接返回false
                
                # 4.currentNode指向尾部之后，进行front和currentNode的双向比较，然后各自移动1步
                if self.front.val != currentNode.val:
                    return False # 5.匹配不上，将失败结果返回
                self.front = self.front.next
            
            # 3.currentNode递归到尾部后，每次都返回True,保证尾节点能反向向前移动
            return True
        
        # 返回最终结果
        return recursiveCheck(currentNode=head)
        



def run():
    header: ListNode = generateLinkList(data=[1, 2, 3, 2, 1])
    result: bool = Solution().isPalindrome2(head=header)
    print(f"result1={result}")
    

# 生成单向链表
def generateLinkList(data: list) -> ListNode:
    header: ListNode = ListNode(666, None)
    lastNode: ListNode = header
    for i, ele in enumerate(data):
        tempNode: ListNode = ListNode(ele, None)
        lastNode.next = tempNode
        lastNode = tempNode
    return header.next


run()

