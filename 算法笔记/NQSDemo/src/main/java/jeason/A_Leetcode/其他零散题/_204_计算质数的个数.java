package jeason.A_Leetcode.其他零散题;


// https://leetcode-cn.com/problems/count-primes/
// 统计所有小于非负整数 n 的质数的数量。
// 输入：n = 10
// 输出：4
// 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

public class _204_计算质数的个数 {
    //--------方法1:暴力方法----------
    public int countPrimes(int n) {
        int count = 0;
        for (int i = 2; i < n; ++i) {
            count += isPrime(i) ? 1 : 0;
        }
        return count;
    }
    public boolean isPrime(int x) {
        //这里使用i*i相当于对x开平方，减少一半重复的遍历
        for (int i = 2; i * i <= x; ++i) {
            if (x % i == 0) {
                return false;
            }
        }
        return true;
    }

    //--------方法2：埃氏筛选--------
    //思路:素数的量少，合数的量大，开始默认都为素数，把合数遍历标记完后，剩下的都是素数了
    public int countPrimes2(int n) {
        boolean[] isPrime = new boolean[n];//默认都是false标识素数
        int count = 0;
        for(int i=2; i<n; i++){

            if(!isPrime[i]){ //bool数组没有标记为素数，就往下进行
                count++;

                //写法1：每次i递增之后，都会从2开始到n-1去乘i。有重复遍历的部分
                for (int t=2*i; t<n; t+=i){
                    // 2*i+i 之后每次t+=i,相当于2*i 3*i 4*i 5*i...了
                    isPrime[t] = true;
                }

                //写法2：每次不再从2开始遍历去乘i，避免重复遍历
                for (int t=i*i; t<n; t+=i){
                    // 2*i+i 之后每次t+=i,相当于2*i 3*i 4*i 5*i...了
                    isPrime[t] = true;
                }
                
            }
        }
        return count;
    }

}