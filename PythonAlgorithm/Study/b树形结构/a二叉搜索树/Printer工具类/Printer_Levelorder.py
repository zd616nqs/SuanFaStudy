# from abc import ABC, abstractmethod
from .Printer import Printer
from .BinaryTree_AbstractInfo import BinaryTree_AbstractInfo
from .StringTool import StringTool
import sys
from typing import List

#    ┌───381────┐
#    │          │
# ┌─12─┐     ┌─410─┐
# │    │     │     │
# 9  ┌─40─┐ 394 ┌─540─┐
#    │    │     │     │
#   35 ┌─190 ┌─476 ┌─760─┐
#      │     │     │     │
#     146   445   600   800


# 实现中序打印器
class Printer_Levelorder(Printer):
    """
    按层序遍历顺序打印二叉树
    """

    def __init__(self, tree: BinaryTree_AbstractInfo):
        super().__init__(tree)

        self.root = Node(tree.root(), tree)
        self.max_width = self.root.width
        self.min_x = 0
        self.MIN_SPACE = 1  # 节点之间允许的最小间距（最小只能填1）

    def print_string(self) -> str:
        """
        生成整个树状图的字符串  
        """
        # nodes用于存放所有节点
        nodes = List[List[Node]]()
        self.fillNodes(nodes)
        self.cleanNodes(nodes)
        self.compressNodes(nodes)
        self.addLineNodes(nodes)

        row_count = len(nodes)

        # 构建字符串
        string = ""
        for i in range(row_count):
            if i != 0:
                string += "\n"
            row_nodes: [Node] = nodes[i]
            row_sb = ""
            for index, tempNode in enumerate(row_nodes):
                left_space = tempNode.x - len(row_sb) - self.min_x
                row_sb += StringTool.blank(left_space)
                row_sb += tempNode.string
            string += row_sb
        return string

    def addNode(self, nodes: List[List['Node']], bt_node: object) -> None:
        """
        添加一个元素节点
        """
        tempNode = None
        if bt_node is not None:
            tempNode = Node(bt_node, self)
            self.max_width = max(self.max_width, tempNode.width)
            nodes.append(tempNode)
        else:
            nodes.append(None)
        return tempNode

    def fillNodes(self, nodes: List[List['Node']]) -> None:
        """
        以满二叉树的形式填充节点信息，生成节点列表
        """

        firstRowNodes: List[Node] = List[Node]()
        firstRowNodes.append(self.root)
        nodes.append(firstRowNodes)

        while (True):
            preRowNodes: List[Node] = nodes[:-1]
            rowNodes = List[Node]()

            notNull: bool = False
            for index, tempNode in enumerate(preRowNodes):
                if tempNode is None:
                    rowNodes.append(None)
                    rowNodes.append(None)
                else:
                    leftNode: Node = self.addNode(
                        rowNodes, self.tree.left(tempNode.btNode))
                    if leftNode is not None:
                        tempNode.left = leftNode
                        notNull = True
                    rightNode: Node = self.addNode(
                        rowNodes,  self.tree.right(tempNode.btNode))
                    if rightNode is not None:
                        tempNode.right = rightNode
                        notNull = True
            if not notNull:
                nodes.add(rowNodes)
                break

    def cleanNodes(self, nodes: List[List['Node']]) -> None:
        """
        删除二叉树中所有的空节点，并更新每个节点的坐标
        """

        if nodes is None:
            return

        row_count: int = len(nodes)
        if row_count < 2:
            return

        # 最后一行的节点数量
        last_row_node_count: int = len(nodes[-1])

        # 每个节点之间的间距
        node_space: int = self.max_width + 2

        # 最后一行的长度
        last_row_length: int = last_row_node_count * self.max_width + node_space * (last_row_node_count - 1)

        # 空集合
        null_set = {None}

        for i in range(row_count):
            row_nodes: List[Node] = nodes[i]

            row_node_count: int = len(row_nodes)
            # 节点左右两边的间距
            all_space: int = last_row_length - (row_node_count - 1) * node_space
            corner_space: int = all_space // row_node_count - self.max_width
            corner_space >>= 1

            row_length: int = 0
            for j in range(row_node_count):
                if j != 0:
                    # 每个节点之间的间距
                    row_length += node_space

                row_length += corner_space
                node: Node = row_nodes[j]
                if node is not None:
                    # 居中（由于奇偶数的问题，可能有1个符号的误差）
                    delta_x = (self.max_width - node.width) >> 1
                    node.x = row_length + delta_x
                    node.y = i

                row_length += self.max_width
                row_length += corner_space

            # 删除所有的null
            row_nodes[:] = [node for node in row_nodes if (node not in null_set)]


    def compressNodes(self, nodes: List[List['Node']]):
        """
        压缩二叉树中相邻节点之间的空格
        """
        if nodes is None:
            return

        row_count: int = len(nodes)
        if row_count < 2:
            return
        # for (int i = rowCount - 2; i >= 0; i--) {
        for i in range(row_count - 2, -1, -1):
            row_nodes: List[Node] = nodes[i]
            row_node_count: int = len(row_nodes)
            for j in range(row_node_count):
                node: Node = row_nodes[j]
                left: Node = node.left
                right = node.right
                if left is None and right is None:
                    continue

                if left is not None and right is not None:
                    # 让左右节点对称
                    node.balance(left, right)

                    # left和right之间可以挪动的最小间距
                    left_empty: int = node.left_bound_empty_length()
                    right_empty: int = node.right_bound_empty_length()
                    empty: int = min(left_empty, right_empty)
                    empty = min(empty, (right.x - left.right_x()) >> 1)

                    # left、right的子节点之间可以挪动的最小间距
                    space: int = left.min_level_space_to_right(right) - self.MIN_SPACE
                    space = min(space >> 1, empty)

                    # left、right往中间挪动
                    if space > 0:
                        left.translate_x(space)
                        right.translate_x(-space)

                    # 继续挪动
                    space = left.min_level_space_to_right(right) - self.MIN_SPACE
                    if space < 1:
                        continue

                    # 可以继续挪动的间距
                    left_empty = node.left_bound_empty_length()
                    right_empty = node.right_bound_empty_length()
                    if left_empty < 1 and right_empty < 1:
                        continue

                    if left_empty > right_empty:
                        left.translate_x(min(left_empty, space))
                    else:
                        right.translate_x(-min(right_empty, space))

                elif left is not None:
                    left.translate_x(node.left_bound_empty_length())

                else:  # right is not None
                    right.translate_x(-node.right_bound_empty_length())

    def addLineNodes(self, nodes: List[List['Node']]) -> None:
        new_nodes: List[List['Node']] = [[]]

        row_count: int = len(nodes)
        if row_count < 2:
            return

        
        self.min_x = self.root.x

        for i in range(row_count):
            row_nodes: List[Node] = nodes[i]
            if i == row_count - 1:
                new_nodes.append(row_nodes)
                continue

            new_row_nodes: List[Node] = []
            new_nodes.append(new_row_nodes)

            line_nodes: List[Node] = []
            new_nodes.append(line_nodes)

            for node in row_nodes:
                self.add_line_node(new_row_nodes, line_nodes, node, node.left)
                new_row_nodes.append(node)
                self.add_line_node(new_row_nodes, line_nodes, node, node.right)

        nodes.clear()
        nodes.extend(new_nodes)
        
        

    def add_xline_node(self, cur_row: List['Node'], parent: 'Node', x: int):
        line: Node = Node(string="─")
        line.x = x
        line.y = parent.y
        cur_row.append(line)


    def add_line_node(self, cur_row: List['Node'], next_row: List['Node'], parent: 'Node', child: 'Node'):
        """在当前行和下一行之间添加连线节点"""
        if child is None:
            return None

        top: Node = None
        top_x: int = child.top_line_x()
        if child is parent.left:
            top = Node(string="┌")
            cur_row.append(top)

            for x in range(top_x + 1, parent.x):
                self.add_xline_node(cur_row, parent, x)

        else:
            for x in range(parent.right_x(), top_x):
                self.add_xline_node(cur_row, parent, x)

            top = Node(string="┐")
            cur_row.append(top)

        # 坐标
        top.x = top_x
        top.y = parent.y
        child.y = parent.y + 2
        self.min_x = min(self.min_x, child.x)

        # 竖线
        bottom: Node = Node(string="│")
        bottom.x = top_x
        bottom.y = parent.y + 1
        next_row.append(bottom)

        return top


    














class LevelInfo(object):
    def __init__(self, leftX: int, rightX: int) -> None:
        self.leftX: int = leftX
        self.rightX: int = rightX

    def generateLevelInfo(self, left: 'Node', right: 'Node'):
        self.leftX = left.leftBound()
        self.rightX = right.rightBound()


class Node(object):
    """树节点类，用于存储树节点信息和坐标信息"""

    # 顶部符号距离父节点的最小距离（最小能填0）
    TOP_LINE_SPACE: int = 1

    def __init__(self, string: str,  btNode: object, opetaionTree: BinaryTree_AbstractInfo) -> None:
        """默认参数初始化"""
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None
        self.x: int = 0  # 首字符的位置
        self.y: int = 0  # 首字符的位置
        self.getTreeHeight: int = 0
        self.width: int = 0
        """接受的初始化参数逻辑"""
        if string is not None:
            # 单纯添加符号
            self.createInit(tempStr=string)
        elif btNode is not None and opetaionTree is not None:
            # 添加节点信息
            btnNodeInfoStr = f"{opetaionTree.printStr(node=btNode)}"
            self.createInit(tempStr=btnNodeInfoStr)
            self.btNode: object = btNode

    def createInit(self, tempStr: str) -> None:
        """判空和判空字符串"""
        tempStr: str = "null" if tempStr is None else tempStr
        tempStr: str = " " if tempStr == "" else tempStr
        self.width: int = len(tempStr)
        self.string: str = tempStr

    def __repr__(self):
        # Node的实例对象被打印
        return f"<Node: {self.string}>"

    def topLineX(self) -> int:
        """顶部方向字符的X（极其重要）"""
        """计算节点上面的线的x坐标"""
        # 宽度的一半
        delta: int = self.width
        if delta % 2 == 0:
            delta -= 1
        delta >>= 1
        if (self.parent is not None) and (self is self.parent.left):
            return self.rightX() - 1 - delta
        else:
            return self.x + delta

    def rightBound(self) -> int:
        """右边界的位置（rightX 或者 右子节点topLineX的下一个位置）（极其重要）"""
        if self.right is None:
            return self.rightX()
        return self.right.topLineX() + 1

    def leftBound(self) -> int:
        """左边界的位置（x 或者 左子节点topLineX）（极其重要）"""
        if self.left is None:
            return self.x
        return self.left.topLineX()

    def leftBoundLength(self) -> int:
        """x ~ 左边界之间的长度（包括左边界字符）"""
        return self.x - self.leftBound()

    def rightBoundLength(self) -> int:
        """rightX ~ 右边界之间的长度（包括右边界字符）"""
        return self.rightBound() - self.rightX()

    def leftBoundEmptyLength(self) -> int:
        """计算节点左边的空缺长度"""
        return self.leftBoundLength() - 1 - self.TOP_LINE_SPACE

    def rightBoundEmptyLength(self) -> int:
        """计算节点右边的空缺长度"""
        return self.rightBoundLength() - 1 - self.TOP_LINE_SPACE

    def balance(self, tempLeftNode: 'Node', tempRightNode: 'Node') -> None:
        """让left和right基于this对称"""
        if tempLeftNode is None or tempRightNode is None:
            return
        # 【left的尾字符】与【this的首字符】之间的间距
        deltaLeft: int = self.x - tempLeftNode.rightX()
        # 【this的尾字符】与【this的首字符】之间的间距
        deltaRight: int = tempRightNode.x - self.rightX()

        delta: int = max(deltaLeft, deltaRight)
        newRightX: int = self.rightX() + delta
        tempRightNode.translateX(newRightX - tempRightNode.x)

        newLeftX: int = self.x - delta - tempLeftNode.width
        tempLeftNode.translateX(newLeftX - tempLeftNode.x)

    def getTreeHeight(self, tempNode: 'Node') -> int:
        """和右节点之间的最小层级距离"""
        if tempNode is None:
            return 0
        if tempNode.treeHeight != 0:
            return tempNode.treeHeight
        tempNode.treeHeight: int = 1 + \
            max(self.getTreeHeight(tempNode.left),
                self.getTreeHeight(tempNode.right))
        return tempNode.treeHeight

    def minLevelSpaceToRight(self, right: 'Node') -> int:
        """和右节点之间的最小层级距离"""
        thisHeight: int = self.getTreeHeight(self)
        rightHeight: int = self.getTreeHeight(right)
        minSpace: int = sys.maxsize
        for i in range(min(thisHeight, rightHeight)):
            space: int = right.levelInfo(i).leftX - self.levelInfo(i).rightX
            minSpace: int = min(minSpace, space)
        return minSpace

    def levelInfo(self, level: int) -> LevelInfo:
        """获取层数的信息"""
        if level < 0:
            return None
        levelY: int = self.y + level
        if level >= self.getTreeHeight(self):
            return None

        list_: list = []
        queue: list = []
        queue.append(self)

        # 层序遍历找出第level行的所有节点
        while queue:
            node: Node = queue.pop(0)
            if levelY == node.y:
                list_.append(node)
            elif node.y > levelY:
                break

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        left: Node = list_[0]
        right: Node = list_[-1]
        return LevelInfo(left, right)

    def rightX(self) -> int:
        """尾字符的下一个位置"""
        return self.x + self.width

    def translateX(self, deltaX: int) -> None:
        """将节点的x坐标平移delta单位"""
        if deltaX == 0:
            return
        self.x += deltaX

        # 如果是LineNode
        if self.btNode is None:
            return

        if self.left is not None:
            self.left.translateX(deltaX)
        if self.right is not None:
            self.right.translateX(deltaX)
