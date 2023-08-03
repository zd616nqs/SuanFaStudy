def caculateFrontIndex(self, step: int) -> int:
        # step:1 front指针向右走一步
        # step:-1 front指针向左走一步
        newFrontPos = self.frontPos + step
        if newFrontPos < 0:
            # 到达左边界，移动到右边界
            return newFrontPos + len(self.__elements)
        else:
            if newFrontPos > len(self.__elements):
                # 到达右边界，移动到左边界
                return newFrontPos - len(self.__elements)
            else:
                # 正常左右移动
                return newFrontPos