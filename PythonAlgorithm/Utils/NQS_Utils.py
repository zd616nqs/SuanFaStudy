
import time
import inspect


class Utils(object):
    
    
    # ----------函数的执行耗时打印--------
    @staticmethod
    def func_cal_time(func):
        # print('耗时计算方法被调用了！！')
        # print('func={}'.format(func))  # func=<function demo at 0x107988720>
        
        # 入参需要占位写上，传入的func如果有入参时有用
        def innerFunc(*nqs_args, **kwarg):
            startTime = time.time()
            nqsResult = func(*nqs_args, **kwarg)
            endTime = time.time()
            print('方法耗时：%.2f秒' % (endTime-startTime)) 
            return nqsResult
        return innerFunc
    
    # ---------函数的入参类型校验-----------
    # 使用方式：
    #    @param_type_validate
    #    def exampleFunc(para1:int, para2: str) {}
    @staticmethod
    def param_type_validate(func):
        def inner(*args, **kwargs):
            full_args_spec = inspect.getfullargspec(func)
            if args:
                new_func_args = full_args_spec.args
                if len(full_args_spec.args) != len(full_args_spec.annotations.keys()):
                    args = args[1:]
                    new_func_args = full_args_spec.args[1:]
                for i, v in enumerate(args):
                    if not isinstance(v, full_args_spec.annotations[new_func_args[i]]):
                        raise TypeError(f"{v}不是{full_args_spec.annotations[new_func_args[i]]}")
            if kwargs:
                for k, v in kwargs.items():
                    if not isinstance(v, full_args_spec.annotations[k]):
                        raise TypeError(f"{v}不是{full_args_spec.annotations[k]}")
            func(*args, **kwargs)
        return inner
    
    # 强制校验所有的抽象方法有没有被实现
    def check_implement(cls):
        for abstract_method in cls.__abstractmethods__:
            if not hasattr(cls, abstract_method):
                raise NotImplementedError(f"牛牛警报！！自定义的抽象方法没有实现：{abstract_method} ")