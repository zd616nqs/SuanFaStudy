
# 26 https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
# 80 https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/

""" 
给你一个有序数组nums，请你【原地】删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。

输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。 不需要考虑数组中超出新长度后面的元素。

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
            # 当前slow指针-1对应的值 != fast指针对应的值
            # 1.慢指针向后挪1位
            # 2.用来存储fast指针对应的值
            if (slow < 1) or (nums[fast] != nums[slow-1]):
                slow += 1
                nums[slow] = nums[fast]
            # 3.存储完后，fast指针向后挪一位，继续下轮对比
            fast += 1
            
        # 当前slow指针的下标就是最终数组的最大index，+1表示数组的容量
        return slow + 1
        


def run():
    tempList: list = [1, 1, 1, 2, 3, 4, 5, 5, 5, 6]
    
    result: int = Solution().removeDuplicates(tempList)
    print(f"{result}--{tempList}") # 8--[1, 1, 2, 3, 4, 5, 5, 6, 5, 6]

run()

