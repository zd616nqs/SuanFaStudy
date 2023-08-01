# 把当前根目录路径添加大sys.path内，所有的子文件夹内的文件就可以直接import根目录的文件了
# 比如内层的文件，可以这么使用：from Utils.NQS_Utils import Utils
import sys
import os
RootDirPath = os.path.abspath(os.path.dirname(os.getcwd())) + "/PythonAlgorithm"
sys.path.append(RootDirPath)


from Study.a线性表.a动态数组.StudyEntry001 import StudyEntry001



def main_study():
    try:
        print("\n\n\n--------程序开始执行---------\n\n")
        StudyEntry001.run(execute=True)
        
        
        
        
        
        
    except Exception as e:
        print('程序执行出错了,原因：', e)
    finally:
        print('主程序结束')




if __name__ == '__main__':
    main_study()
