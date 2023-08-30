
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/

""" 
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

题解：
"""


class Solution(object):
    
    # 思路:使用滑动窗口来判断
    # 1.窗口左侧先不动，窗口右侧依次向右，直至右侧值=左侧值
    # 2.窗口左侧向右移一位后不动，窗口右侧继续依次向右移动，跟窗口左侧进行比较
    # 3.直至窗口右侧移动到字符串最后
    def lengthOfLongestSubstring(self, inpuStr: str) -> int:
        if not inpuStr:
            return 0

        maxLength: int = 0
        start: int = 0
        tempMap: dict = {}
        for index, ele in enumerate(inpuStr):
            ch: str = ele
            
            # 如果存在相同的字符，窗口左侧指针向右移动1位
            indexOfChar: int = tempMap.get(ch, "找不到对应的字符")
            if indexOfChar and (type(indexOfChar) is int):
                start = max(start, indexOfChar)
            
            # 窗口右侧不停向右移动，找到最大的窗口长度
            maxLength = max(maxLength, index - start)
            
            # 把当前循环拿到的字符串放到map内，会覆盖之前重复字符串对应的下标
            tempMap[ch] = index
        
        return maxLength
        
        



def run():
    tempStr: str = "joijweonfiouo"
    result: int = Solution().lengthOfLongestSubstring(tempStr)
    print(f"{result}")

run()

