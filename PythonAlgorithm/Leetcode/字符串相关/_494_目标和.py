
# https://leetcode.cn/problems/target-sum/

""" 
给你一个 非负整数 数组nums和一个整数target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。


输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3


输入：nums = [1], target = 1
输出：1

题解：https://leetcode.cn/problems/target-sum/solutions/18548/python-dfs-xiang-jie-by-jimmy00745/

参考视频：https://www.bilibili.com/video/BV16Y411v7Y6/?vd_source=f440158b433224a55ef2b6efcb013d5b
"""
from typing import List

class Solution(object):
    
    """ 
    分解：
    * 找到nums一个正子集和一个负子集，使得总和等于target，统计这种可能性的总数。
    * 假设P是正子集，N是负子集
        1.sum(P) - sum(N) = target
        2.两边同时加上sum(P)+sum(N)
        3.sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
        4.因为 sum(P) + sum(N) = sum(nums)
        5. 2*sum(P) = target+sum(nums)
    所以，问题变成，找到一个子集P，使其满足
        sum(P) = (target+sum(nums))//2   （target+sum(nums)的和一定要符合为偶数）
        
    """
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        if (sum(nums) < abs(target)) or ((sum(nums) + target) % 2 == 1): 
            return 0
        sumP = int(sum(nums) + target) // 2
        
        dp = [1] + [0 for _ in range(sumP)]
        for num in nums:
            for j in range(sumP, num-1, -1):
                dp[j] += dp[j - num]
        return dp[sumP]


def run():
    # tempList: List[int] = [1, 1, 1, 1, 1]
    tempList: List[int] = [100]
    result: int = Solution().findTargetSumWays(nums=tempList, target=-200)
    print(f"{result}")

run()

