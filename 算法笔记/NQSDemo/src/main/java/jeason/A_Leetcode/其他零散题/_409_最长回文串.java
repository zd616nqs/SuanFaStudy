package jeason.A_Leetcode.其他零散题;

// https://leetcode.cn/problems/longest-palindrome/

public class _409_最长回文串 {

//思路：遍历字符串，得到数量为奇数个的字符，结果为:（字符总长-奇数字符个数+1）
    public int longestPalindrome(String s) {
        //创建int数组
        int[] arr = new int[128];

        int length = s.length();
        for (int i = 0; i < length; ++i) {
            char c = s.charAt(i);
            arr[c] += 1;
        }

        int count = 0;
        //for in遍历
        for (int nnn : arr) {
            count += (nnn%2);
        }

        //如果count为0：所有字符都是偶数个，长度就为整个字符串的长度
        //如果count不为0：标识有count奇数个的字符，所有需要总长-count+1
        count = (count==0)?s.length():(s.length()-count+1);
        return count;
    }
}