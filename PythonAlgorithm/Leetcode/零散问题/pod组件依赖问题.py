

""" 
抖音社交面试题

- cocoapods查找依赖树
- 问题1：从最深层打印，最后打印根节点app
- 问题2：如果podB和podC都依赖podD，怎么处理
- 问题3：若果podB依赖podC，podC依赖podB，中间又隔着几十个依赖，怎么防止循环依赖

"""

class Solution(object):
    
    # -------没有循环依赖的case------
    def handle1(self, deps: dict, root: str) -> list:
        # 结果数组
        result: list = []
        # 入口
        stack = []
        stack.append(root)
        
        while stack:
            # 弹出当前节点
            current = stack.pop()
            
            # 如果当前节点有依赖
            if current in deps:  
                # 遍历依赖节点
                for depPod in deps[current]:
                    # 加入栈     
                    stack.append(depPod)

            # 弹出节点后加入结果数组    
            result.append(current)

        return result
        
    # -------有循环依赖的问题--------
    def handle2(self, deps: dict, root: str) -> list:
        # 结果数组
        result = []  
        # 已访问节点集合 
        visited = set()
        
        def dfs(deps, node):
            # 已经添加过，不再重复添加
            if node in visited:
                return
            
            visited.add(node)  # 标识添加过
            result.append(node) # 往结果里添加一个依赖的pod
            
            if node in deps:
                childPod: list = deps[node]
                for childPodDep in childPod:  
                    dfs(deps, childPodDep)
                    
        dfs(deps, root)
        return result


def run():
    
    # -------没有循环依赖的case------
    dependencies1: dict = {
        'App': ['PODA'],
        'PODA': ['PODB', 'PODC', 'PODD'], 
        'PODC': ['PODE'],
        'PODE': [],
    }
    result1: int = Solution().handle1(deps=dependencies1, root="App")
    print(f"{result1}") 
    # ['App', 'PODA', 'PODD', 'PODC', 'PODE', 'PODB']
    
    # -------有循环依赖的问题--------
    dependencies2: dict = {
        'App': ['PODA'],
        'PODA': ['PODB', 'PODC', 'PODD'], 
        'PODC': ['PODB'],
        'PODB': ['PODC'],
    }
    result2: int = Solution().handle2(deps=dependencies2, root='App')
    print(f"{result2}") 
    # ['App', 'PODA', 'PODB', 'PODC', 'PODD']

run()

