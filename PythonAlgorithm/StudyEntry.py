# 把当前根目录路径添加大sys.path内，所有的子文件夹内的文件就可以直接import根目录的文件了
# 比如内层的文件，可以这么使用：from Utils.NQS_Utils import Utils
import sys
import os
RootDirPath = os.path.abspath(os.path.dirname(os.getcwd())) + "/PythonAlgorithm"
sys.path.append(RootDirPath)

from Utils.NQS_Utils import Utils


from Study.a线性表.a动态数组.StudyEntry001 import StudyEntry001
from Study.a线性表.b链表.StudyEntry002 import StudyEntry002
from Study.a线性表.c栈.StudyEntry003 import StudyEntry003
from Study.a线性表.d队列.StudyEntry004 import StudyEntry004


@Utils.func_cal_time
def main_study():
    try:
        print("--------程序开始执行---------\n\n")
        
        # ************************线性表*******************
        
        # ----动态数组---------
        StudyEntry001.run(execute=False)

        # -----链表----------
        StudyEntry002.run(execute=False)

        # -----栈----------
        StudyEntry003.run(execute=False)
        # -----队列----------
        StudyEntry004.run(execute=True)

        # ***********************树形结构********************
        # ----二叉搜索树-------
        # StudyEntry005.run(false)
        
        
        
        
        
    except Exception as e:
        print(f'\n--------程序执行出错了,原因：{e}')
    finally:
        print("\n\n--------程序结束执行---------")




if __name__ == '__main__':
    main_study()
