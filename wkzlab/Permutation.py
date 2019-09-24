class Permutation():
    '''
    组合排列 A n m ->
    '''

    def __init__(self, total:int, choose: int): # eliteCount: int
        self.__total = total
        self.__choose = choose
        self.__choosed_list = []

        '''
        0 1 2 3 4 
        
        __choosed_list : 012 013 014 023 024 034 123 124 134 234  （）
        
        '''
        self.__elite = []  #初始化一个 int[eliteCount]的数组

        for num in range(0, self.__choose):
            self.__choosed_list.append(num)  # 5选3： 012
            self.__elite.append(num)  # 5选3： 012

    def __if_permutation_finish(self):
        # 判断当前的 __elite 是否为该组（__choosed_list）的最后一个排列
        pass

    def __combination_(self):
        #
        pass


    def next(self) -> bool:
        '''
        # 根据__choosed_list 和  __elite 生成下一个__elite的排列结果
        :return: bool 是否可以求的下一个数组，如果可以返回True并求得下一个数组
        '''




    def getElite(self) -> list :
        return self.__elite
