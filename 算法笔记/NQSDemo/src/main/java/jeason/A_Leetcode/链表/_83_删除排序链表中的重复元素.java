package jeason.A_Leetcode.链表;

// https://leetcode.cn/problems/remove-duplicates-from-sorted-list/


class _83_删除排序链表中的重复元素 {
    // 输入：head = [1,1,2,3,3]
    // 输出：[1,2,3]

    //思路一次遍历   连续两个元素相同就删除一个
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return head;
        }

        ListNode cur = head;
        while (cur.next != null) {
            if (cur.val == cur.next.val) {
                cur.next = cur.next.next;
            } else {
                cur = cur.next;
            }
        }
        return head;
    }
}