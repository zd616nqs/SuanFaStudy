package jeason.A_Leetcode.链表;
// https://leetcode.cn/problems/merge-in-between-linked-lists/


class _1669_合并两个有序链表_将一个链表插入替换到另一个链表的中间{

   //list1找到a、b两个节点，删除a-b中间的元素，将list2放进去

    //思路：遍历找到链表1保留部分的尾节点和链表2的尾节点。将两链表连接起来。

    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        //创建头部、中部、尾部的node节点
        ListNode headNode = list1, tempNode = list1, endNode = list2;
        
        int i = 0, j = 0;
        while(headNode != null && tempNode != null && j < b){
            //遍历找到入口a的节点，赋值给头部node
            if(i != a - 1){
                headNode = headNode.next;
                i++;
            } 
            //遍历找到出口b的节点，赋值给tempNode
            if(j != b){
                tempNode = tempNode.next;
                j++;
            } 
        }
        //-----------入口a连接到list2的头部----------
        headNode.next = list2;

        //-----------出口b连接到list2的尾部----------
        //tempMode移动到出口b的下一个节点
        tempNode = tempNode.next;
        //寻找list2的尾节点
        while(endNode.next != null){
            endNode = endNode.next;
        }
        endNode.next = tempNode;

        return list1;
    }
}