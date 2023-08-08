
# 26 https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
# 80 https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/

""" 
给你一个升序排列的数组 nums ，请你【原地】删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的相对顺序应该保持一致 。然后返回nums中唯一元素的个数。

考虑 nums 的唯一元素的数量为k，你需要做以下事情确保你的题解可以被通过：
1.更改数组nums，使nums的前k个元素包含唯一元素，并按照它们最初在nums中出现的顺序排列。nums的其余元素与 nums 的大小不重要。
2.返回k

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。


题解：
"""

class Solution(object):
    # 思路：使用快慢指针,不停的把fast指针对应的内容赋值到slow+1的位置
    def removeDuplicates(self, nums: list) -> int:
        n: int = len(nums)
        if n == 0:
            return 0
        # 初始位置：快指针index=1，慢指针index=0
        fast: int = 1
        slow: int = 0
        
        # 依次移动fast指针，直至最后一个节点
        while fast < n:
            # 当前slow指针对应的值 != fast指针对应的值
            # 1.慢指针向后挪1位
            # 2.用来存储fast指针对应的值
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            # 3.存储完后，fast指针向后挪一位，继续下轮对比
            fast += 1
            
        # 当前slow指针的下标就是最终数组的最大index，+1表示数组的容量
        return slow + 1
        



def run():
    tempList: list = [1, 1, 2, 3, 4, 5, 5, 6]
    
    result: int = Solution().removeDuplicates(tempList)
    print(f"{result}--{tempList}") # 6--[1, 2, 3, 4, 5, 6, 5, 6]

run()

