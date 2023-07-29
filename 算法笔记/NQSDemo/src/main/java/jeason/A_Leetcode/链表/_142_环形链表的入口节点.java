package jeason.A_Leetcode.链表;


// https://leetcode.cn/problems/c32eOV/
class _142_环形链表的入口节点 {
//思路：从头结点出发一个指针，从相遇节点也出发一个指针，这两个指针每次只走一个节点，那么当这两个指针相遇的时候就是 环形入口的节点

    public ListNode detectCycle(ListNode head) {
        if(head == null || head.next == null) return null;

        //快慢指针起始点错开
        ListNode slow = head;
        ListNode fast = head.next;

        while(fast != null && fast.next != null){
            slow = slow.next;//慢指针一次走1步
            fast = fast.next.next;//快指针一次走2步
            if(fast == slow) {
                //------这里找确定了该链表是环形链表--------
                ListNode index1 = fast;//相遇的节点为一个点
                ListNode index2 = head;//头节点为另外一个点
                while (index1 != index2) {
                    //index1和index2每次都走1步，相遇的点就为环的入口
                    index1 = index1.next;
                    index2 = index2.next;
                }
                return index2; // 返回环的入口

            };
        }
        return null;
    }

}