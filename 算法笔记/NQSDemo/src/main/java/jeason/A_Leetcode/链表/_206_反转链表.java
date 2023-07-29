package jeason.A_Leetcode.链表;

// https://leetcode-cn.com/problems/reverse-linked-list/
// 输入：head = [1,2,3,4,5]
// 输出：[5,4,3,2,1]

class _206_反转链表 {

    //方法1：使用递归方式反转
    public ListNode reverseList1(ListNode head) {
        if(head == null) return null;
        if(head.next == null) return head;

        ListNode newHead = reverseList1(head);
        head.next.next = head;
        head.next = null;//此处置null，防止相互指向行程环形链表
        return newHead;
    }



    //方法2：使用头插法反转
    public ListNode reverseList2(ListNode head) {
        if(head == null) return null;
        if(head.next == null) return head;

        ListNode finalHead = null;
        while(head != null){//还没循环到链表的最后，即null
            ListNode tempNode = head.next;//提前存好下一个需要反转的node
            head.next = finalHead;//指定反转后的next
            finalHead = head;
            head = tempNode;//向前推进一位
        }
        return finalHead;
    }

}