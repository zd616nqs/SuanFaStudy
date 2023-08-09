
# https://leetcode.cn/problems/count-primes/

""" 
给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

题解：https://leetcode.cn/problems/count-primes/solutions/36629/pythonzui-you-jie-fa-mei-you-zhi-yi-liao-ba-by-bru/
"""


class Solution(object):
    
    def countPrimes(self, n: int) -> int:
        # result = self.countPrimes1(n)
        result = self.countPrimes2(n)
        return result
    
    # --------方法1:暴力遍历方法----------
    def countPrimes1(self, n: int) -> int:
        if n < 2:
            return 0
        count: int = 0
        for i in range(2, n):
            isPrime: bool = True
            for j in range(2, i):
                if i % j == 0:
                    isPrime = False
                    break
            count += int(isPrime)
        return count
        
    # --------方法2：埃氏筛选--------
    # 思路:素数的量少，合数的量大，开始默认都为素数，把合数遍历标记完后，剩下的都是素数了
    def countPrimes2(self, n: int) -> int:
        if n < 2:
            return 0
        
        # 默认都是质数
        flagList: list = [1] * n
        
        # 0和1不是质数，先排除掉
        flagList[0] = flagList[1] = 0
        
        # 遍历范围：2到n的开根号，减少遍历次数
        for i in range(2, int(n ** 0.5)+1):
            if flagList[i]:
                flagList[i*i: n: i] = [0] * ((n - 1 - i * i) // i + 1)
        return sum(flagList)
            



def run():
    result: int = Solution().countPrimes(20)
    print(f"{result}")

run()

