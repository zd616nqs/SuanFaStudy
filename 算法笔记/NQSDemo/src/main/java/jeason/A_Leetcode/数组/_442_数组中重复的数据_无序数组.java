package jeason.A_Leetcode.数组;
import java.util.ArrayList;
import java.util.List;

// https://leetcode-cn.com/problems/implement-queue-using-stacks/


public class _442_数组中重复的数据_无序数组 {

    // 输入:[4,3,2,7,8,2,3,1]     输出:[2,3]

    // 思路：
    // 1.首先将出现的元素作为数组的下标，每出现一次就加上一个数组的长度
    // 2.然后再筛选出数组中的值在(2n,3n+1)之间，就是出现两次的数据了，
    // 3.如果要出现三次就筛选(3n,4ñ+1)就行了
    public List<Integer> findDuplicates(int[] nums) {
        int n = nums.length;
        
        List<Integer> ans = new ArrayList<>();

        for(int i:nums){
            nums[(i-1)%n]=nums[(i-1)%n]+n;

        }
        for(int i=0;i<n;i++){
            if(nums[i]<3*n+1 && nums[i]>2*n){
                ans.add(i+1);
            }
        }
        return ans;
    }
}