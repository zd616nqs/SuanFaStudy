package jeason.A_Leetcode.其他零散题;


import java.util.HashMap;
import java.util.Map;

// https://leetcode.cn/problems/target-sum/
// 输入：nums = [2,7,11,15], target = 9
// 输出：[0,1]
// 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。


public class _494_目标和 {

    //思路：使用哈希表读写，减少次数
    public int[] twoSum(int[] nums, int target) {

        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        for (int i = 0; i < nums.length; i++) {
            if(map.containsKey(target-nums[i])){
                Integer index1 = map.get(target-nums[i]);
                Integer index2 = i;
                return new int[]{index1,index2};
            }
            map.put(nums[i], i);
        }
        return new int[0];
    }
}
