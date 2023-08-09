
# https://leetcode.cn/problems/longest-valid-parentheses/

""" 
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"

输入：s = "(()())"
输出：6
解释：最长有效括号子串是 "(()())"

题解：https://leetcode.cn/problems/longest-valid-parentheses/solutions/762279/32-zui-chang-you-xiao-gua-hao-fu-zhu-zha-1cqq/
"""


class Solution(object):
    
    def longestValidParentheses(self, s: str) -> int:
        if not s: 
            return 0
        
        stack: list = []
        ans = 0
        for i in range(len(s)):
            # 入栈条件
            if not stack or s[i] == '(' or s[stack[-1]] == ')':
                # 下标入栈
                stack.append(i)   
            else:
                # 计算结果
                stack.pop()
                tempLength: int = i - (stack[-1] if stack else -1)
                ans = max(ans, tempLength)
        return ans



def run():
    tempStr: str = "(()()(()"
    result: int = Solution().longestValidParentheses(tempStr)
    print(f"{result}")

run()

