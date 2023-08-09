
# https://leetcode.cn/problems/find-all-duplicates-in-an-array/

""" 
给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 一次 或 两次 。请你找出所有出现 两次 的整数，并以数组形式返回。

你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间的算法解决此问题。

输入：nums = [4,3,2,7,8,2,3,1]
输出：[2,3]

输入：nums = [1,1,2]
输出：[1]

思路：要不使用额外内存空间，则只能原地修改数组元素来标记是否访问过 原理：如果是相同的元素，那么以他们为索引的元素值一定是同一个值，因此可以修改该值来标记是否被访问过 注意：既要原地修改元素，就不能影响其自身作为索引的访问，那么只有一种办法，那就是将该元素取反，或者加减某个数，在访问的时候，再通过取正或者加减某个数还原回来


题解：https://leetcode.cn/problems/find-all-duplicates-in-an-array/solutions/404530/yuan-di-xiu-gai-yuan-su-wei-fu-shu-zuo-fang-wen-bi/
"""

class Solution(object):

    def findDuplicates(self, nums: list) -> list:
        if not nums: 
            return []
        
        resultList: list = []
        
        for tempNum in nums:
            # 如果是重复的元素，计算得到的index值是相同的
            # 此处-1是数组最大数量是n，最大值也是n，所以n-1能满足取值不越界
            tempIndex = abs(tempNum) - 1 
            tempValue: int = nums[tempIndex]
            
            if tempValue < 0:
                # 如果取到负数，说明这个数字之前遇到过，被赋值为负数存起来了
                resultList.append(abs(tempNum))
            else:
                # 说明第一次碰到这个元素，将其变为负值
                nums[tempIndex] = -nums[tempIndex]
            
        return resultList
        


def run():
    # tempList: list = [4, 3, 2, 7, 8, 2, 3, 1] # 预期结果[3, 2]
    tempList2: list = [10, 2, 5, 10, 9, 1, 1, 4, 3, 7]# 预期结果[10, 1]

    # result: list = Solution().findDuplicates(tempList)
    result2: list = Solution().findDuplicates(tempList2)
    # print(f"{result}")
    print(f"{result2}")

run()

