package jeason.A_Leetcode.链表;

//https://leetcode-cn.com/problems/delete-node-in-a-linked-list/
// 输入：head = [4,5,1,9], node = 5
// 输出：[4,1,9]
// 解释：给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.


class _237_删除链表中的节点 {

    public void deleteNode(ListNode node) {
        if(node == null) return;

        node.val = node.next.val;
        node.next = node.next.next;
    }
}