package jeason.A_Leetcode.链表;

// https://leetcode.cn/problems/remove-nth-node-from-end-of-list/


class _19_删除链表的倒数第N个结点 {

   //方法一：快慢指针法   fast指针比slow指针超前N个节点
    public ListNode removeNthFromEnd1(ListNode head, int n) {
        ListNode tempHead = head;
        ListNode fast = head;
        ListNode slow = head;
        //s指针比first指针领先n个节点
        for (int i = 0; i < n; ++i) {
            fast = fast.next;
        }
        //fast指针循环走到链表最后
        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;
        ListNode resultNode = tempHead.next;
        return resultNode;
    }


    // 方法二：遍历搜索法  时间复杂度O(n)，空间复杂度O(1)
    public ListNode removeNthFromEnd2(ListNode head, int n) {
        ListNode tempHead = head;
        int length = getLength(head);
        ListNode cur = tempHead;
        for (int i = 1; i < length - n + 1; ++i) {
            cur = cur.next;
        }
        cur.next = cur.next.next;

        ListNode resultNode = tempHead.next;
        return resultNode;
    }
    //计算整个链表的长度
    public int getLength(ListNode head) {
        int length = 0;
        while (head != null) {
            ++length;
            head = head.next;
        }
        return length;
    }
}

