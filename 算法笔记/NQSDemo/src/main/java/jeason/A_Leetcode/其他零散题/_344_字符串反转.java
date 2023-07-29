package jeason.A_Leetcode.其他零散题;


// https://leetcode.cn/problems/reverse-string/


public class _344_字符串反转 {

   //思路：双指针法，一个从前到后，一个后到前，替换两个字符串
    public void reverseString(char[] s) {
        int n = s.length;
        for (int left = 0, right = n - 1; left < right; ++left, --right) {
            char tmp = s[left];//临时存储左边的字符串
            s[left] = s[right];//右侧的移动到左侧
            s[right] = tmp;//左侧的移动到右侧
        }
    }
}
