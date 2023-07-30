

from Study.a线性表 import ArrayList 
# from Study.b树形结构 import NodeTree 

def main_study():
    try:
        ArrayList.exampleFun("牛牛", 222)
        return 111
    except Exception as e:
        print('程序出错了,原因：', e)
    finally:
        print('结束111')




if __name__ == '__main__':
    main_study()
