from .BinarySearchTree二叉搜索树 import BinarySearchTree二叉搜索树
from .BinaryTrees import BinaryTrees


class StudyEntry005(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def run(*, execute: bool):
        if (not execute):
            return

        obj = StudyEntry005()

        # ----简单的添加数字到二叉树中------
        obj.example1(isWork=True)

        print("")

    # --------------普通单向链表的实现---------------
    def example1(self, *, isWork: bool):
        if (not isWork):
            return

        data: list = [7, 4, 9, 2, 5, 8, 11, 3, 12, 1]
        bst: BinarySearchTree二叉搜索树 = BinarySearchTree二叉搜索树[int]()
        for index, element in enumerate(data):
            # todo:niu 写不下去了。。先这样把。。
            bst.addElement(ele=element)
            
        BinaryTrees.println(bst)
