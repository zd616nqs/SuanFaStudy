
# https://leetcode.cn/problems/reverse-string/

""" 
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题


输入：strList: List[str] = ["n", "q", "s", "6", "7", "3", "666"]
输出：['666', '3', '7', '6', 's', 'q', 'n']

题解：https://leetcode.cn/problems/reverse-string/solutions/2376308/python3javacgorust-yi-ti-yi-jie-shuang-z-f8dw/
"""
from typing import List

class Solution(object):
    
    # 双指针方法：一个从头往后，一个从尾往前
    def reverseString222(self, s: List[str]) -> None:
        
        headIndex: int = 0
        tailIndex: int = len(s) - 1
        while (headIndex < tailIndex):
            # 不停的交换两个元素，直到中间
            tempEle = s[headIndex]
            s[headIndex] = s[tailIndex]
            s[tailIndex] = tempEle
            # 前后各走一步
            headIndex += 1
            tailIndex -= 1



def run():
    strList: List[str] = ["n", "q", "s", "6", "7", "3", "666"]
    Solution().reverseString222(strList)
    print(f"{strList}")

run()

