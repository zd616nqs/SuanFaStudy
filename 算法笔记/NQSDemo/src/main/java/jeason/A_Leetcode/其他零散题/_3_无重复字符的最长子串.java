package jeason.A_Leetcode.其他零散题;


// https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
// 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
// 输入: s = "abcabcbb"
// 输出: 3 
// 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
import java.util.HashMap;

public class _3_无重复字符的最长子串 {

    //思路：使用滑动窗口来判断
    public int lengthOfLongestSubstring2(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        int max = 0, start = 0;
        for (int end = 0; end < s.length(); end++) {
            char ch = s.charAt(end);

            //如果存过相同的字符，滑动窗口到end+1的位置重新计算
            if (map.containsKey(ch)){
                start = Math.max(map.get(ch)+1,start);
            }
            //得到本地循环的最大值
            max = Math.max(max,  end-start+1);
            //将当前循序拿到的字符串放到map里面，会覆盖掉之前重复的元素
            map.put(ch,end);
        }
        return max;
    }
}