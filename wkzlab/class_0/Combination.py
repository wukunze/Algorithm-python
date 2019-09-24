class Combination():
    '''
    组合排列  C n m
    '''
    def __init__(self, total:int, choose: int): # eliteCount: int
        self.__total = total
        self.__choose = choose
        self.__elite = []  #初始化一个 int[eliteCount]的数组

        for num in range(0, self.__choose):
            self.__elite.append(num)


    # next 完成功能： 5个数字中取得3个： 0 1 2(true) -> 0 1 3(true) -> 0 2 4(true) ->.......... ->2 3 4(false)
    # 从 total 中取出3个
    # 把当前数组内容按照字典序求得下一个数组内容
    def next(self) -> bool:
        '''
        # 把当前数组内容按照字典序求得下一个数组内容
        :return: bool 是否可以求的下一个数组，如果可以返回True并求得下一个数组
        '''
        max_value = self.__total - 1
        for num in range(len(self.__elite)-1, -1, -1):
            if self.__elite[num] != max_value:
                self.__elite[num] += 1
                return True
            max_value -= 1
        return False

    def getElite(self) -> list :
        return self.__elite
