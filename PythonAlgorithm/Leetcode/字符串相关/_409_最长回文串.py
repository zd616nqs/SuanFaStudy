
# https://leetcode.cn/problems/reverse-string/

""" 
给定一个包含大写字母和小写字母的字符串 s ，返回 通过这些字母构造成的 最长的回文串 。
在构造过程中，请注意 区分大小写 。比如 "Aa" 不能当做一个回文字符串。

输入:s = "abccccdd"
输出:7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

输入:s = "aaaaaccc"
输出:7

题解：
"""

class Solution(object):
    # 思路：遍历字符串，得到数量为奇数个的字符，结果为:（字符总长-奇数字符个数+1）
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        tempMap: dict = {}
        for index, ele in enumerate(s):
            if ele in tempMap.keys():
                tempCount: int = tempMap[ele]
                tempCount += 1
                tempMap[ele] = tempCount
            else:
                tempMap[ele] = 1
                
        result: int = 0
        haveOdd: bool = False
        for temp in tempMap.keys():
            tempCount: int = tempMap[temp]
            # 允许最多一个奇数的字符，放在最中间
            if (tempCount % 2) and not haveOdd:
                result += 1
                haveOdd = True
            # 偶数时全部添加count，奇数时-1后再添加count
            result += ((tempCount-1) if (tempCount % 2) else tempCount)
        return result


def run():
    tempStr: str = "abccccdd"
    # tempStr: str = "ccc"
    result: int = Solution().longestPalindrome(tempStr)
    print(f"{result}")

run()

