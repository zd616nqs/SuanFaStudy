
# https://leetcode.cn/problems/longest-valid-parentheses/

""" 
快速排序
参考链接：https://blog.csdn.net/qq_35344198/article/details/106785849
"""

class Solution(object):
    
    # 时间复杂度：O(nlogn)
    # 空间复杂度  O(logN)
    def quicksort(self, arr):
        # 如果数组长度小于2直接返回
        if len(arr) < 2:  
            return arr

        # 取数组的第一个元素作为基准值
        pivot = arr[0]

        # 创建两个列表,用于存放比基准值小和大的元素
        less = []  
        greater = []

        # 从索引1开始遍历数组其他元素
        for i in range(1, len(arr)):             
            if arr[i] <= pivot:  
                # 如果元素小于等于基准值,添加到less列表
                less.append(arr[i])
            else:
                # 否则添加到greater列表    
                greater.append(arr[i])

        # 对两个子列表递归调用快速排序
        
        less = self.quicksort(less)
        greater = self.quicksort(greater)

        # 将三个有序列表合并返回
        return less + [pivot] + greater


def run():
    dataArr: list = [5, 3, 6, 2, 10, 1, 4]
    result: list = Solution().quicksort(dataArr)
    print(f"{result}") # [1, 2, 3, 4, 5, 6, 10]

run()

