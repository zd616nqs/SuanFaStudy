package jeason.A_Leetcode.数组;



// https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
// https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/


public class _26_80_删除数组重复项_有序数组 {

    //有序数组  删除重复项
    //思路：双指针方法
    public int removeDuplicates1(int[] nums) {
        int n = nums.length;
        if (n == 0) {
            return 0;
        }

        int fast = 1, slow = 1;
        while (fast < n) {
            if (nums[fast] != nums[fast - 1]) {
                nums[slow] = nums[fast];
                ++slow;
            }
            ++fast;
        }
        return slow;
    }

}