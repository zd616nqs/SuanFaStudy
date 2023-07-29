package jeason.A_Leetcode.链表;

// https://leetcode.cn/problems/merge-two-sorted-lists/



class _21_合并两个有序链表_融合到一起 {
    // 输入：l1 = [1,2,4], l2 = [1,3,4]
    // 输出：[1,1,2,3,4,4]

    //方法一：递归  各种左右判断大小，递归调用
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        } else if (l2 == null) {
            return l1;
        } else if (l1.val < l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        } else {
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        }
    }

    //方法二：迭代
    public ListNode mergeTwoLists2(ListNode l1, ListNode l2) {
        //初始化一个开始的空节点
        ListNode tempHead = new ListNode(-1);

        //创建一个工具节点，遍历循环完后就没用了
        ListNode tempNode = tempHead;

        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                tempNode.next = l1;
                l1 = l1.next;
            } else {
                tempNode.next = l2;
                l2 = l2.next;
            }
            //
            tempNode = tempNode.next;
        }

        //合并后l1和l2 最多只有一个还未被合并完，直接将链表末尾指向未合并完的链表即可
        tempNode.next = (l1==null)?l2:l1;

        ListNode head = tempHead.next;
        return head;
    }
}