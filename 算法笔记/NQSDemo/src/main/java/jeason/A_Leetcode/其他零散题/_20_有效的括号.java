package jeason.A_Leetcode.其他零散题;
import java.util.HashMap;
import java.util.Stack;

// https://leetcode-cn.com/problems/valid-parentheses/
// 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
// 有效字符串需满足：
// 左括号必须用相同类型的右括号闭合。
// 左括号必须以正确的顺序闭合。

class _20_有效的括号 {

    private static HashMap<Character, Character> map = new HashMap<>();
    static {
        // key - value
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');
    }
    
    //-------解法1：使用map存取来匹配----------
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        int len = s.length();
        for (int i = 0; i < len; i++) {
            char c = s.charAt(i);
            if (map.containsKey(c)) { 
                // 匹配：左括号
                stack.push(c);
            } else { 
                // 匹配：右括号

                //1.没有左括号，无效
                if (stack.isEmpty()) return false;
                
                //2.左右括号匹配不上，无效
                char left = stack.pop();
                if (c != map.get(left)) return false;
            }
        }
        return stack.isEmpty();
    }
    

    //-------解法2：手动判断字符串来匹配----------
    public boolean isValid1(String s) {
        Stack<Character> stack = new Stack<>();
        
        int len = s.length();
        for (int i = 0; i < len; i++) {
            char c = s.charAt(i);
            if (c == '(' || c == '{' || c == '[') { // 左括号
                stack.push(c);
            } else { // 右括号
                if (stack.isEmpty()) return false;
                
                char left = stack.pop();
                if (left == '(' && c != ')') return false;
                if (left == '{' && c != '}') return false;
                if (left == '[' && c != ']') return false;
            }
        }
        return stack.isEmpty();
    }

    //-------解法3：偷懒的解法，while循环删除成对的，最后如果为空就标识是有效的---------
    public boolean isValid2(String s) {
        while (s.contains("{}")
                || s.contains("[]")
                || s.contains("()")) {
            s = s.replace("{}", "");
            s = s.replace("()", "");
            s = s.replace("[]", "");
        }
        return s.isEmpty();
    }
}