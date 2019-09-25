class MaxList():

    def __init__(self, int_list: list):
        self.int_list = int_list #正整数list , 一定会有整数 ： [-2, 11, -4, 13, -5, -2]



    def answer(self):
        '''
        基于两个事实的结题思路
        1.最大子段开头不可能是负数
        2.如果一个子段的加和变成了负数，之前的字段都不可能是最大字段（也就是所 这个子段不管作为哪一个子段中的子子段，都不可能是最大）
        :return: 结果
                 最小子段 list
        '''
        ans = 0
        begin_index = 0
        end_index = 0

        if 0 == len(self.int_list):
            return None, []

        for index,item in enumerate(self.int_list):
            new_ans = ans + item
            if new_ans < 0:
                begin_index = index + 1 #下一个索引
                ans = 0 #清空结果
                continue
            if new_ans:
                pass

        return


    def dp_answer(self):

        return
