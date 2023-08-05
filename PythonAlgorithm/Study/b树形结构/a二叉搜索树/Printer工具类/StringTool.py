
class StringTool(object):
    @staticmethod
    def repeat(string: str, count: int) -> str:
        """重复一个字符串N次"""
        if not string:
            return None
        
        result = ""
        while count > 0:
            result += string    
            count -= 1
        return result
        
    @staticmethod    
    def blank(length: int) -> str:
        """添加空格"""
        if length < 0:
            return None
        if length == 0:     
            return ""
            
        return " " * length
