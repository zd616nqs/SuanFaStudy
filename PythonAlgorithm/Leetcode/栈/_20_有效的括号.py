
# https://leetcode.cn/problems/valid-parentheses/

""" 
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：
1.左括号必须用相同类型的右括号闭合。
2.左括号必须以正确的顺序闭合。
3.每个右括号都有一个对应的相同类型的左括号。

输入：s = "()"
输出：true

输入：s = "()[]{}"
输出：true

输入：s = "(]"
输出：false

题解：https://leetcode.cn/problems/find-all-duplicates-in-an-array/solutions/404530/yuan-di-xiu-gai-yuan-su-wei-fu-shu-zuo-fang-wen-bi/
"""

class Solution(object):

    def isValid(self, s: str) -> bool:
        result: bool = False
        # result = self.isValid1(s)
        # result = self.isValid2(s)
        result = self.isValid3(s)
        return result
    
    # 方法1: 使用字典(哈希表)出入栈判断
    def isValid1(self, s: str) -> bool:
        map: dict = {"{": "}", "[": "]", "(": ")"}
        stack: list = []
        for ch in s:
            if ch in map.keys():
                # 匹配左括号内容(key)
                stack.append(ch)
            else:
                # 匹配右括号内容
                if len(stack) <= 0:
                    return False
                tempItem = stack.pop()
                tempValue: str = map[tempItem]
                if tempValue != ch:
                    return False
        return len(stack) == 0 # 最终一定是栈为空的
    
    # 方法2:手动判断字符串来匹配（太蠢了）
    def isValid2(self, s: str) -> bool:
        stack: list = []
        for ch in s:
            isMatchLeft: bool = (ch == "(") or (ch == "{") or (ch == "[")
            if isMatchLeft:
                # 匹配左括号内容(key)
                stack.append(ch)
            else:
                # 匹配右括号内容
                if len(stack) <= 0:
                    return False
                
                leftItem = stack.pop()
                if (leftItem == "(" and ch != ")") or (leftItem == "[" and ch != "]") or (leftItem == "{" and ch != "}"):
                    return False  
        return len(stack) == 0 # 最终一定是栈为空的
    
    # 方法3:偷懒的解法，while循环删除成对的，最后如果为空就标识是有效的
    def isValid3(self, s: str) -> bool:
        # while条件为非0，就会一直执行
        # find语句找不到时返回-1
        while ((s.find("{}") != -1) or (s.find("[]") != -1) or (s.find("()") != -1)):
            res1 = s.find("{}")
            res2 = s.find("[]")
            res3 = s.find("()")
            print(f"{res1},{res2},{res3}")
            
            s = s.replace("{}", "")
            s = s.replace("[]", "")
            s = s.replace("()", "")
        return len(s) == 0

def run():
    
    tempStr1: str = "{}[]()"
    tempStr2: str = "[]"
    tempStr3: str = "((}}"
    tempStr4: str = "("
    result1: list = Solution().isValid(tempStr1)
    result2: list = Solution().isValid(tempStr2)
    result3: list = Solution().isValid(tempStr3)
    result4: list = Solution().isValid(tempStr4)
    print(f"result1:{result1}\nresult2:{result2}\nresult3:{result3}\nresult4:{result4}")

run()

